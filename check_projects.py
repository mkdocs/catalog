import concurrent.futures
import configparser
import subprocess
import sys
import tempfile
import textwrap
from pathlib import Path

import yaml


def _get_as_list(mapping, key):
    names = mapping.get(key, ())
    if isinstance(names, str):
        names = (names,)
    return names


_kind_to_label = {
    "mkdocs_plugin": "plugin",
    "mkdocs_theme": "theme",
    "markdown_extension": "markdown",
}

projects = yaml.safe_load(Path("projects.yaml").read_text())["projects"]


def check_install_project(project, install_name, errors=None):
    if errors is None:
        errors = []

    with tempfile.TemporaryDirectory(prefix="best-of-mkdocs-") as directory:
        try:
            result = subprocess.run(
                ["pip", "install", "-U", "--ignore-requires-python", "--no-deps", "--target", directory, install_name],
                stdin=subprocess.DEVNULL,
                capture_output=True,
                text=True,
                check=True,
                timeout=30,
            )
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
            errors.append(f"Failed {e.cmd}:\n{e.stderr}")
            return

        entry_points = configparser.ConfigParser()
        try:
            [entry_points_file] = Path(directory).glob(f"*.dist-info/entry_points.txt")
            entry_points.read_string(entry_points_file.read_text())
        except ValueError:
            pass
        entry_points = {sect: list(entry_points[sect]) for sect in entry_points.sections()}

        for item in _get_as_list(project, "mkdocs_plugin"):
            if item not in entry_points.get("mkdocs.plugins", ()):
                errors.append(f"Missing entry point [mkdocs.plugins] '{item}'.\nInstead got {entry_points}")

        for item in _get_as_list(project, "mkdocs_theme"):
            if item not in entry_points.get("mkdocs.themes", ()):
                errors.append(f"Missing entry point [mkdocs.themes] '{item}'.\nInstead got {entry_points}")

        for item in _get_as_list(project, "markdown_extension"):
            if item not in entry_points.get("markdown.extensions", ()):
                base_path = item.replace(".", "/")
                for pattern in base_path + ".py", base_path + "/__init__.py":
                    path = Path(directory, pattern)
                    if path.is_file() and "makeExtension" in path.read_text():
                        break
                else:
                    errors.append(
                        f"Missing entry point [markdown.extensions] '{item}'.\n"
                        f"Instead got {entry_points}.\n"
                        f"Also not found as a direct import."
                    )

    return errors


pool = concurrent.futures.ThreadPoolExecutor(4)

# Tracks shadowing: projects earlier in the list take precedence.
available = {k: {} for k in _kind_to_label}

futures = []

for project in projects:
    errors = []

    if not project.get("name"):
        errors.append("Project must have a 'name:'")
        continue
    if not project.get("category"):
        errors.append("Project must have a 'category:'")

    for kind, label in _kind_to_label.items():
        items = _get_as_list(project, kind)

        if (label in project.get("labels", ())) != bool(items):
            errors.append(f"'{label}' label should be present if and only if '{kind}:' is present")

        for item in items:
            already_available = available[kind].get(item) or (
                kind == "mkdocs_plugin" and available[kind].get(item.split("/")[-1])
            )
            if already_available:
                if kind not in project.get("shadowed", ()):
                    errors.append(
                        f"{kind} '{item.split('/')[-1]}' is present in both project '{already_available}' and '{project['name']}'.\n"
                        f"If that is expected, the later of the two projects will be ignored, "
                        f"and to indicate this, it should contain 'shadowed: [{kind}]'"
                    )
            else:
                available[kind][item] = project["name"]

    install_name = None
    if any(key in project for key in _kind_to_label):
        if "pypi_id" in project:
            install_name = project["pypi_id"]
        elif "github_id" in project:
            install_name = f"git+https://github.com/{project['github_id']}"
        else:
            errors.append("Missing 'pypi_id:'")

    if install_name:
        fut = pool.submit(check_install_project, project, install_name, errors)
    else:
        fut = concurrent.futures.Future()
        fut.set_result(errors)
    futures.append((project["name"], fut))


error_count = 0

for project_name, fut in futures:
    result = fut.result()
    if result:
        error_count += len(result)
        print()
        print(f"{project_name}:")
        for error in result:
            print(textwrap.indent(error.rstrip(), "     "))
            print()
    else:
        print(".", end="")
        sys.stdout.flush()

if error_count:
    print()
    sys.exit(f"Exited with {error_count} errors")
