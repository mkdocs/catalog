import re
from pathlib import Path

line_re = re.compile(r"^(?P<details><details><summary>)?(?P<link>[^(]+)\((?P<metrics>[^)]+)\) - (?P<summary>.+) (?P<markers><code>(<a|❗).*)$")

if __name__ == "__main__":
    new_lines = []
    readme = Path(__file__).parent / "README.md"
    with readme.open() as fh:
        for line in fh:
            line = line.rstrip()
            match = line_re.match(line)
            if match:
                groups = match.groupdict()
                link = groups["link"]
                metrics = groups["metrics"]
                summary = groups["summary"]
                markers = groups["markers"]
                markers = markers.replace("</summary>", "")
                markers = markers.replace("</code> <code>", "</code> · <code>")
                details_start = groups["details"] or ""
                details_end = "</summary>" if details_start else ""
                new_line = f"{details_start}{link} - {metrics} · {markers}<br>{summary}{details_end}"
                new_lines.append(new_line)
            else:
                new_lines.append(line)
    readme.write_text("\n".join(new_lines))
