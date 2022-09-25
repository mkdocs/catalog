import concurrent.futures
import configparser
import subprocess
import sys
import tempfile
import textwrap
from pathlib import Path

import yaml


def check_project(project):
    key_to_label = {
        "mkdocs_plugin": "plugin",
        "mkdocs_theme": "theme",
        "markdown_extension": "markdown",
    }

    if not any(key in project for key in key_to_label):
        return

    if "pypi_id" in project:
        install_name = project["pypi_id"]
    elif "github_id" in project:
        install_name = f"git+https://github.com/{project['github_id']}"
    else:
        return "Missing 'pypi_id:'"

    with tempfile.TemporaryDirectory(prefix="best-of-mkdocs-") as directory:
        result = subprocess.run(
            ["pip", "install", "-U", "--ignore-requires-python", "--no-deps", "--target", directory, install_name],
            capture_output=True,
            text=True,
        )
        if result.returncode:
            return f"Failed {result.args}:\n{result.stderr}"

        entry_points = configparser.ConfigParser()
        try:
            [entry_points_file] = Path(directory).glob(f"*.dist-info/entry_points.txt")
            entry_points.read_string(entry_points_file.read_text())
        except ValueError:
            pass
        entry_points = {sect: list(entry_points[sect]) for sect in entry_points.sections()}

        if "mkdocs_plugin" in project:
            if project["mkdocs_plugin"] not in entry_points.get("mkdocs.plugins", ()):
                return f"Missing entry point [mkdocs.plugins] '{project['mkdocs_plugin']}'.\nInstead got {entry_points}"

        if "mkdocs_theme" in project:
            if project["mkdocs_theme"] not in entry_points.get("mkdocs.themes", ()):
                return f"Missing entry point [mkdocs.themes] '{project['mkdocs_theme']}'.\nInstead got {entry_points}"

        if "markdown_extension" in project:
            if project["markdown_extension"] not in entry_points.get("markdown.extensions", ()):
                base_path = project["markdown_extension"].replace(".", "/")
                for pattern in base_path + ".py", base_path + "/__init__.py":
                    path = Path(directory, pattern)
                    if path.is_file() and "makeExtension" in path.read_text():
                        break
                else:
                    return (
                        f"Missing entry point [markdown.extensions] '{project['markdown_extension']}'.\n"
                        f"Instead got {entry_points}.\n"
                        f"Also not found as a direct import."
                    )

    for key, label in key_to_label.items():
        if (label in project.get("labels", ())) != (key in project):
            return f"'{label}' label should be present if and only if '{key}:' is present"


projects = yaml.safe_load(Path("projects.yaml").read_text())["projects"]


error_count = 0

with concurrent.futures.ThreadPoolExecutor(4) as pool:
    for project, result in zip(projects, pool.map(check_project, projects)):
        if result:
            error_count += 1
            print()
            print(f"{project['name']}:")
            print(textwrap.indent(result, "     "))
        else:
            print(".", end="")
            sys.stdout.flush()

if error_count:
    sys.exit(f"Exited with {error_count} errors")
