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


def _check_project(project):
    key_to_label = {
        "mkdocs_plugin": "plugin",
        "mkdocs_theme": "theme",
        "markdown_extension": "markdown",
    }

    if not any(key in project for key in key_to_label):
        return

    for key, label in key_to_label.items():
        if (label in project.get("labels", ())) != (key in project):
            yield f"'{label}' label should be present if and only if '{key}:' is present"

    if "pypi_id" in project:
        install_name = project["pypi_id"]
    elif "github_id" in project:
        install_name = f"git+https://github.com/{project['github_id']}"
    else:
        yield "Missing 'pypi_id:'"
        return

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
            yield f"Failed {e.cmd}:\n{e.stderr}"
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
                yield f"Missing entry point [mkdocs.plugins] '{item}'.\nInstead got {entry_points}"

        for item in _get_as_list(project, "mkdocs_theme"):
            if item not in entry_points.get("mkdocs.themes", ()):
                yield f"Missing entry point [mkdocs.themes] '{item}'.\nInstead got {entry_points}"

        for item in _get_as_list(project, "markdown_extension"):
            if item not in entry_points.get("markdown.extensions", ()):
                base_path = item.replace(".", "/")
                for pattern in base_path + ".py", base_path + "/__init__.py":
                    path = Path(directory, pattern)
                    if path.is_file() and "makeExtension" in path.read_text():
                        break
                else:
                    yield (
                        f"Missing entry point [markdown.extensions] '{item}'.\n"
                        f"Instead got {entry_points}.\n"
                        f"Also not found as a direct import."
                    )


def check_project(project):
    return list(_check_project(project))


projects = yaml.safe_load(Path("projects.yaml").read_text())["projects"]


error_count = 0

with concurrent.futures.ThreadPoolExecutor(4) as pool:
    for project, result in zip(projects, pool.map(check_project, projects)):
        if result:
            error_count += 1
            print()
            print(f"{project['name']}:")
            for error in result:
                print(textwrap.indent(error.rstrip(), "     "))
                print()
        else:
            print(".", end="")
            sys.stdout.flush()

if error_count:
    sys.exit(f"Exited with {error_count} errors")
