<!-- markdownlint-disable -->
<h1 align="center">
    catalog
    <br>
</h1>

<p align="center">
    <strong>:trophy: :books: A list of awesome <a href="https://github.com/mkdocs/mkdocs">MkDocs</a> projects and plugins.</strong>
</p>

<p align="center">
    <a href="https://best-of.org" title="Best-of Badge"><img src="http://bit.ly/3o3EHNN"></a>
    <a href="#Contents" title="Project Count"><img src="https://img.shields.io/badge/projects-300-blue.svg?color=5ac4bf"></a>
    <a href="#Contribution" title="Contributions are welcome"><img src="https://img.shields.io/badge/contributions-welcome-green.svg"></a>
    <a href="https://github.com/mkdocs/catalog/releases" title="Catalog Updates"><img src="https://img.shields.io/github/release-date/mkdocs/catalog?color=green&label=updated"></a>
</p>

This list contains 300 awesome open-source projects grouped into 17 categories. All projects are ranked by a project-quality score, which is calculated based on various metrics automatically collected from GitHub and different package managers. If you want to add or update projects, feel free to open an [issue](https://github.com/mkdocs/catalog/issues/new/choose), submit a [pull request](https://github.com/mkdocs/catalog/pulls), or directly edit the [projects.yaml](https://github.com/mkdocs/catalog/edit/main/projects.yaml). Contributions are very welcome!

> 🧙‍♂️  Discover other [best-of lists](https://best-of.org) or [create your own](https://github.com/best-of-lists/best-of/blob/main/create-best-of-list.md).

## Contents

- [🎨 Theming](#-theming) _31 projects_
- [💻 API documentation building](#-api-documentation-building) _26 projects_
- [💬 Blogging](#-blogging) _7 projects_
- [📊 Charts, Images, Tables & Graphs](#-charts-images-tables--graphs) _40 projects_
- [🤖 Code execution, variables & templating](#-code-execution-variables--templating) _22 projects_
- [🌲 Git repos & info](#-git-repos--info) _12 projects_
- [🌈 HTML processing & CSS styling](#-html-processing--css-styling) _16 projects_
- [📎 Integrations with other tools](#-integrations-with-other-tools) _13 projects_
- [🌍 Internationalization & localization](#-internationalization--localization) _3 projects_
- [🔗 Links & references](#-links--references) _24 projects_
- [🧩 Markdown extensions](#-markdown-extensions) _28 projects_
- [🧭 Navigation & page building](#-navigation--page-building) _28 projects_
- [✅ Quality checks (code blocks, spelling, etc.)](#-quality-checks-code-blocks-spelling-etc) _6 projects_
- [🔍 Search & tables of content](#-search--tables-of-content) _5 projects_
- [🍱 Site conversion (PDF/ePUB/etc.)](#-site-conversion-pdfepubetc) _11 projects_
- [🔧 Site building, site management](#-site-building-site-management) _22 projects_
- [📁 Snippets & includes (reusing contents)](#-snippets--includes-reusing-contents) _9 projects_

## Explanation
- 🥇🥈🥉&nbsp; Combined project-quality score
- ⭐️&nbsp; Star count from GitHub
- 🐣&nbsp; New project _(less than 6 months old)_
- 💤&nbsp; Inactive project _(12 months no activity)_
- 💀&nbsp; Dead project _(99999 months no activity)_
- 📈📉&nbsp; Project is trending up or down
- ➕&nbsp; Project was recently added
- ❗️&nbsp; Warning _(e.g. missing/risky license)_
- 👨‍💻&nbsp; Contributors count from GitHub
- 🔀&nbsp; Fork count from GitHub
- 📋&nbsp; Issue count from GitHub
- ⏱️&nbsp; Last update timestamp on package manager
- 📥&nbsp; Download count from package manager
- 📦&nbsp; Number of dependent projects
- <img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13">&nbsp; MkDocs plugin
- <img src="https://cdn.icon-icons.com/icons2/1495/PNG/32/preferencesdesktoptheme_102980.png" style="display:inline;" width="13" height="13">&nbsp; MkDocs theme
- <img src="https://cdn.icon-icons.com/icons2/1448/PNG/32/42498factory_99134.png" style="display:inline;" width="13" height="13">&nbsp; Mkdocs-based project (website, templates, etc.)
- <img src="https://cdn.icon-icons.com/icons2/1459/PNG/32/2799201-jigsaw-processing_99781.png" style="display:inline;" width="13" height="13">&nbsp; Markdown extension(s)

<br>

## 🎨 Theming

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://github.com/squidfunk/mkdocs-material">Material for MkDocs</a></b>  - 🥇42 ·  ⭐ 27K · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1495/PNG/32/preferencesdesktoptheme_102980.png" style="display:inline;" width="13" height="13"></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Documentation that simply works.</summary>

<a href="https://pawamoy.github.io/mkdocs-gallery/themes/material/">
<img src="https://pawamoy.github.io/mkdocs-gallery/assets/img/material.png" width="400" align="right">
</a>

- [GitHub](https://github.com/squidfunk/mkdocs-material) (👨‍💻 330 · 🔀 4K · 📦 88K · 📋 2.7K - 0% open · ⏱️ 10.06.2026)
- [PyPi](https://pypi.org/project/mkdocs-material) (📥 16M / month):
	```
	pip install mkdocs-material
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#theme):
   ```yaml
   theme: material
   ```
   Extras:
   ```yaml
   plugins:
     - blog
     - group
     - offline
     - search
     - social
     - tags
   ```
</details>
<details><summary><b><a href="https://github.com/asiffer/mkdocs-shadcn">Shadcn</a></b>  - 🥇24 ·  ⭐ 180 · 📈 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1495/PNG/32/preferencesdesktoptheme_102980.png" style="display:inline;" width="13" height="13"></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Documentation that also shines.</summary>

<a href="https://pawamoy.github.io/mkdocs-gallery/themes/shadcn/">
<img src="https://pawamoy.github.io/mkdocs-gallery/assets/img/shadcn.png" width="400" align="right">
</a>

- [GitHub](https://github.com/asiffer/mkdocs-shadcn) (👨‍💻 4 · 🔀 21 · 📥 330 · 📦 82 · 📋 47 - 14% open · ⏱️ 20.05.2026)
- [PyPi](https://pypi.org/project/mkdocs-shadcn) (📥 32K / month):
	```
	pip install mkdocs-shadcn
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#theme):
   ```yaml
   theme: shadcn
   ```
   Extras:
   ```yaml
   plugins:
     - search
     - excalidraw
   ```
</details>
<details><summary><b><a href="https://github.com/ntno/mkdocs-terminal">Terminal for MkDocs</a></b>  - 🥇20 ·  ⭐ 320 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1495/PNG/32/preferencesdesktoptheme_102980.png" style="display:inline;" width="13" height="13"></code><br>monospace theme for MkDocs.</summary>

<a href="https://pawamoy.github.io/mkdocs-gallery/themes/terminal/">
<img src="https://pawamoy.github.io/mkdocs-gallery/assets/img/terminal.png" width="400" align="right">
</a>

- [GitHub](https://github.com/ntno/mkdocs-terminal) (👨‍💻 4 · 🔀 21 · 📦 160 · 📋 68 - 41% open · ⏱️ 26.03.2026)
- [PyPi](https://pypi.org/project/mkdocs-terminal) (📥 6.6K / month):
	```
	pip install mkdocs-terminal
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#theme):
   ```yaml
   theme: terminal
   ```
   Extras:
   ```yaml
   plugins:
     - md-to-html
   ```
</details>
<details><summary><b><a href="https://github.com/chrissimpkins/cinder">Cinder</a></b>  - 🥇19 ·  ⭐ 220 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1495/PNG/32/preferencesdesktoptheme_102980.png" style="display:inline;" width="13" height="13"></code><br>A clean, responsive MkDocs theme.</summary>

<a href="https://pawamoy.github.io/mkdocs-gallery/themes/cinder/">
<img src="https://pawamoy.github.io/mkdocs-gallery/assets/img/cinder.png" width="400" align="right">
</a>

- [GitHub](https://github.com/chrissimpkins/cinder) (👨‍💻 23 · 🔀 98 · 📥 1K · 📦 710 · 📋 51 - 31% open · ⏱️ 05.01.2021)
- [PyPi](https://pypi.org/project/mkdocs-cinder):
	```
	pip install mkdocs-cinder
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#theme):
   ```yaml
   theme: cinder
   ```
</details>
<details><summary><b><a href="https://github.com/FernandoCelmer/mkdocs-simple-blog">Simple Blog</a></b>  - 🥈18 ·  ⭐ 120 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1495/PNG/32/preferencesdesktoptheme_102980.png" style="display:inline;" width="13" height="13"></code><br>Blog Template for Mkdocs.</summary>

<a href="https://pawamoy.github.io/mkdocs-gallery/themes/simple-blog/">
<img src="https://pawamoy.github.io/mkdocs-gallery/assets/img/simple-blog.png" width="400" align="right">
</a>

- [GitHub](https://github.com/FernandoCelmer/mkdocs-simple-blog) (👨‍💻 5 · 🔀 13 · 📦 97 · 📋 38 - 7% open · ⏱️ 18.03.2026)
- [PyPi](https://pypi.org/project/mkdocs-simple-blog) (📥 1K / month):
	```
	pip install mkdocs-simple-blog
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#theme):
   ```yaml
   theme: simple-blog
   ```
</details>
<details><summary><b><a href="https://github.com/dracula/mkdocs">Dracula</a></b>  - 🥈18 ·  ⭐ 120 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1495/PNG/32/preferencesdesktoptheme_102980.png" style="display:inline;" width="13" height="13"></code><br>Dark theme for Mkdocs.</summary>

<a href="https://pawamoy.github.io/mkdocs-gallery/themes/dracula/">
<img src="https://pawamoy.github.io/mkdocs-gallery/assets/img/dracula.png" width="400" align="right">
</a>

- [GitHub](https://github.com/dracula/mkdocs) (👨‍💻 5 · 🔀 14 · 📦 150 · 📋 17 - 11% open · ⏱️ 10.03.2026)
- [PyPi](https://pypi.org/project/mkdocs-dracula-theme) (📥 9.3K / month):
	```
	pip install mkdocs-dracula-theme
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#theme):
   ```yaml
   theme: dracula
   ```
</details>
<details><summary><b><a href="https://github.com/mkdocs/mkdocs-bootstrap">Bootstrap</a></b>  - 🥈17 ·  ⭐ 95 · 💤 · <code><a href="http://bit.ly/3rqEWVr">BSD-2</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1495/PNG/32/preferencesdesktoptheme_102980.png" style="display:inline;" width="13" height="13"></code><br>MkDocs Bootstrap Theme.</summary>

<a href="https://pawamoy.github.io/mkdocs-gallery/themes/bootstrap/">
<img src="https://pawamoy.github.io/mkdocs-gallery/assets/img/bootstrap.png" width="400" align="right">
</a>

- [GitHub](https://github.com/mkdocs/mkdocs-bootstrap) (👨‍💻 6 · 🔀 34 · 📦 520 · 📋 16 - 6% open · ⏱️ 29.12.2023)
- [PyPi](https://pypi.org/project/mkdocs-bootstrap) (📥 15K / month):
	```
	pip install mkdocs-bootstrap
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#theme):
   ```yaml
   theme: bootstrap
   ```
</details>
<details><summary><b><a href="https://github.com/mkdocs/mkdocs-bootswatch">Bootswatch</a></b>  - 🥈15 ·  ⭐ 150 · 💤 · <code><a href="http://bit.ly/3rqEWVr">BSD-2</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1495/PNG/32/preferencesdesktoptheme_102980.png" style="display:inline;" width="13" height="13"></code><br>MkDocs Bootswatch Themes.</summary>

<a href="https://pawamoy.github.io/mkdocs-gallery/themes/cerulean/">
<img src="https://pawamoy.github.io/mkdocs-gallery/assets/img/cerulean.png" width="400" align="right">
</a>

- [GitHub](https://github.com/mkdocs/mkdocs-bootswatch) (👨‍💻 10 · 🔀 58 · 📦 1.3K · 📋 33 - 9% open · ⏱️ 29.12.2023)
- [PyPi](https://pypi.org/project/mkdocs-bootswatch):
	```
	pip install mkdocs-bootswatch
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#theme):
   ```yaml
   theme: cerulean
   theme: cosmo
   theme: cyborg
   theme: darkly
   theme: flatly
   theme: journal
   theme: litera
   theme: lumen
   theme: lux
   theme: materia
   theme: minty
   theme: pulse
   theme: sandstone
   theme: simplex
   theme: slate
   theme: solar
   theme: spacelab
   theme: superhero
   theme: united
   theme: yeti
   ```
</details>
<details><summary><b><a href="https://github.com/buvis/mkdocs-zettelkasten">Zettelkasten</a></b>  - 🥈15 ·  ⭐ 27 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1495/PNG/32/preferencesdesktoptheme_102980.png" style="display:inline;" width="13" height="13"></code><br>This is a Zettelkasten theme and plugin for MkDocs. It renders the MkDocs pages as cards (zettels).</summary>

<a href="https://pawamoy.github.io/mkdocs-gallery/themes/zettelkasten-solarized-light/">
<img src="https://pawamoy.github.io/mkdocs-gallery/assets/img/zettelkasten-solarized-light.png" width="400" align="right">
</a>

- [GitHub](https://github.com/buvis/mkdocs-zettelkasten) (👨‍💻 5 · 🔀 3 · 📥 57 · 📦 6 · ⏱️ 08.06.2026)
- [PyPi](https://pypi.org/project/mkdocs-zettelkasten):
	```
	pip install mkdocs-zettelkasten
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#theme):
   ```yaml
   theme: zettelkasten-solarized-light
   ```
   Extras:
   ```yaml
   plugins:
     - zettelkasten
   ```
</details>
<details><summary><b><a href="https://github.com/gristlabs/mkdocs-windmill">Windmill</a></b>  - 🥈13 ·  ⭐ 130 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1495/PNG/32/preferencesdesktoptheme_102980.png" style="display:inline;" width="13" height="13"></code><br>Outstanding mkdocs theme with a focus on navigation and usability.</summary>

<a href="https://pawamoy.github.io/mkdocs-gallery/themes/windmill/">
<img src="https://pawamoy.github.io/mkdocs-gallery/assets/img/windmill.png" width="400" align="right">
</a>

- [GitHub](https://github.com/gristlabs/mkdocs-windmill) (👨‍💻 8 · 🔀 52 · 📦 370 · 📋 31 - 48% open · ⏱️ 11.03.2022)
- [PyPi](https://pypi.org/project/mkdocs-windmill):
	```
	pip install mkdocs-windmill
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#theme):
   ```yaml
   theme: windmill
   ```
</details>
<details><summary><b><a href="https://github.com/wsoft-ws/lantana">Lantana</a></b>  - 🥈13 ·  ⭐ 25 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1495/PNG/32/preferencesdesktoptheme_102980.png" style="display:inline;" width="13" height="13"></code><br>Lantana MKDocsHTML.</summary>

<a href="https://pawamoy.github.io/mkdocs-gallery/themes/lantana/">
<img src="https://pawamoy.github.io/mkdocs-gallery/assets/img/lantana.png" width="400" align="right">
</a>

- [GitHub](https://github.com/wsoft-ws/lantana) (👨‍💻 6 · 🔀 2 · 📥 430 · 📦 8 · 📋 20 - 10% open · ⏱️ 03.07.2025)
- [PyPi](https://pypi.org/project/lantana) (📥 430 / month):
	```
	pip install lantana
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#theme):
   ```yaml
   theme: lantana
   ```
</details>
<details><summary><b><a href="https://github.com/kpn/mkdocs-kpn-theme">KPN for MkDocs</a></b>  - 🥈13 ·  ⭐ 9 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1495/PNG/32/preferencesdesktoptheme_102980.png" style="display:inline;" width="13" height="13"></code><br>KPN theme for MkDocs, ProperDocs and Zensical | owner=des.</summary>

<a href="https://pawamoy.github.io/mkdocs-gallery/themes/kpn/">
<img src="https://pawamoy.github.io/mkdocs-gallery/assets/img/kpn.png" width="400" align="right">
</a>

- [GitHub](https://github.com/kpn/mkdocs-kpn-theme) (👨‍💻 9 · 📦 8 · ⏱️ 12.05.2026)
- [PyPi](https://pypi.org/project/mkdocs-kpn):
	```
	pip install mkdocs-kpn
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#theme):
   ```yaml
   theme: kpn
   ```
</details>
<details><summary><b><a href="https://github.com/TEParsons/torillic">Torillic</a></b>  - 🥈11 ·  ⭐ 130 · 💤 · <code><a href="https://tldrlegal.com/search?query=CC0-1.0">❗️CC0-1.0</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1495/PNG/32/preferencesdesktoptheme_102980.png" style="display:inline;" width="13" height="13"></code><br>A D&D inspired theme for styling TTRPG notes and resources.</summary>

<a href="https://pawamoy.github.io/mkdocs-gallery/themes/torillic/">
<img src="https://pawamoy.github.io/mkdocs-gallery/assets/img/torillic.png" width="400" align="right">
</a>

- [GitHub](https://github.com/TEParsons/torillic) (👨‍💻 4 · 🔀 83 · 📥 8K · 📋 13 - 15% open · ⏱️ 21.04.2025)
- [PyPi](https://pypi.org/project/mkdocs-torillic):
	```
	pip install mkdocs-torillic
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#theme):
   ```yaml
   theme: torillic
   ```
</details>
<details><summary><b><a href="https://github.com/swan-cern/mkdocs-swan">SWAN</a></b>  - 🥈11 ·  ⭐ 7 · <code><a href="http://bit.ly/3pwmjO5">❗️AGPL-3.0</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1495/PNG/32/preferencesdesktoptheme_102980.png" style="display:inline;" width="13" height="13"></code><br>SWAN MkDocs theme.</summary>

<a href="https://pawamoy.github.io/mkdocs-gallery/themes/swan/">
<img src="https://pawamoy.github.io/mkdocs-gallery/assets/img/swan.png" width="400" align="right">
</a>

- [GitHub](https://github.com/swan-cern/mkdocs-swan) (👨‍💻 5 · 🔀 4 · 📦 12 · ⏱️ 23.01.2026)
- [PyPi](https://pypi.org/project/mkdocs-swan) (📥 330 / month):
	```
	pip install mkdocs-swan
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#theme):
   ```yaml
   theme: swan
   ```
</details>
<details><summary><b><a href="https://github.com/Paul-Riviere/mkdocs-curriculum-vitae">mkdocs-curriculum-vitae</a></b>  - 🥈11 ·  ⭐ 7 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1495/PNG/32/preferencesdesktoptheme_102980.png" style="display:inline;" width="13" height="13"></code><br>A simple MkDocs theme, designed to make your curriculum vitae (CV) with minimal configuration, and several themes.</summary>

<a href="https://pawamoy.github.io/mkdocs-gallery/themes/curriculum-vitae/">
<img src="https://pawamoy.github.io/mkdocs-gallery/assets/img/curriculum-vitae.png" width="400" align="right">
</a>

- [GitHub](https://github.com/Paul-Riviere/mkdocs-curriculum-vitae) (👨‍💻 3 · 🔀 1 · 📦 3 · 📋 47 - 23% open · ⏱️ 12.11.2025)
- [PyPi](https://pypi.org/project/mkdocs-curriculum-vitae) (📥 220 / month):
	```
	pip install mkdocs-curriculum-vitae
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#theme):
   ```yaml
   theme: curriculum-vitae
   ```
</details>
<details><summary><b><a href="https://github.com/LukeCarrier/mkdocs-theme-bootstrap4">Bootstrap 4</a></b>  - 🥉10 ·  ⭐ 7 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1495/PNG/32/preferencesdesktoptheme_102980.png" style="display:inline;" width="13" height="13"></code><br>A vanilla Bootstrap 4 theme for MkDocs.</summary>

<a href="https://pawamoy.github.io/mkdocs-gallery/themes/bootstrap4/">
<img src="https://pawamoy.github.io/mkdocs-gallery/assets/img/bootstrap4.png" width="400" align="right">
</a>

- [GitHub](https://github.com/LukeCarrier/mkdocs-theme-bootstrap4) (👨‍💻 3 · 📋 6 - 16% open · ⏱️ 23.11.2024)
- [PyPi](https://pypi.org/project/mkdocs-theme-bootstrap4) (📥 760 / month):
	```
	pip install mkdocs-theme-bootstrap4
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#theme):
   ```yaml
   theme: bootstrap4
   ```
   Extras:
   ```yaml
   plugins:
     - bootstrap4-blockquotes
     - bootstrap4-tables
   ```
</details>
<details><summary><b><a href="https://github.com/waylan/mkdocs-nature">Nature</a></b>  - 🥉9 ·  ⭐ 5 · <code>❗Unlicensed</code> · <code><img src="https://cdn.icon-icons.com/icons2/1495/PNG/32/preferencesdesktoptheme_102980.png" style="display:inline;" width="13" height="13"></code><br>A MkDocs theme.</summary>

<a href="https://pawamoy.github.io/mkdocs-gallery/themes/nature/">
<img src="https://pawamoy.github.io/mkdocs-gallery/assets/img/nature.png" width="400" align="right">
</a>

- [GitHub](https://github.com/waylan/mkdocs-nature) (👨‍💻 3 · 🔀 1 · 📦 52 · ⏱️ 04.09.2025)
- [PyPi](https://pypi.org/project/mkdocs-nature) (📥 2K / month):
	```
	pip install mkdocs-nature
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#theme):
   ```yaml
   theme: nature
   ```
</details>
<details><summary><b><a href="https://github.com/Siphalor/mkdocs-custommill">CustomMill</a></b>  - 🥉7 ·  ⭐ 18 · 💤 · <code>❗Unlicensed</code> · <code><img src="https://cdn.icon-icons.com/icons2/1495/PNG/32/preferencesdesktoptheme_102980.png" style="display:inline;" width="13" height="13"></code><br>Outstanding mkdocs theme with a focus on navigation, customization and usability.</summary>

<a href="https://pawamoy.github.io/mkdocs-gallery/themes/custommill/">
<img src="https://pawamoy.github.io/mkdocs-gallery/assets/img/custommill.png" width="400" align="right">
</a>

- [GitHub](https://github.com/Siphalor/mkdocs-custommill) (👨‍💻 8 · 🔀 7 · 📦 24 · ⏱️ 10.03.2022)
- [PyPi](https://pypi.org/project/mkdocs-custommill):
	```
	pip install mkdocs-custommill
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#theme):
   ```yaml
   theme: custommill
   ```
</details>
<details><summary><b><a href="https://github.com/byrnereese/mkdocs-moonstone">Moonstone</a></b>  - 🥉7 ·  ⭐ 8 · 💤 · <code>❗Unlicensed</code> · <code><img src="https://cdn.icon-icons.com/icons2/1495/PNG/32/preferencesdesktoptheme_102980.png" style="display:inline;" width="13" height="13"></code><br>A documentation theme for mkdocs.</summary>

<a href="https://pawamoy.github.io/mkdocs-gallery/themes/moonstone/">
<img src="https://pawamoy.github.io/mkdocs-gallery/assets/img/moonstone.png" width="400" align="right">
</a>

- [GitHub](https://github.com/byrnereese/mkdocs-moonstone) (🔀 1 · 📦 18 · ⏱️ 15.06.2021)
- [PyPi](https://pypi.org/project/mkdocs-moonstone) (📥 300 / month):
	```
	pip install mkdocs-moonstone
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#theme):
   ```yaml
   theme: moonstone
   ```
</details>
<details><summary><b><a href="https://github.com/TEParsons/mkdocs-landing">Landing</a></b>  - 🥉6 ·  ⭐ 26 · 💤 · <code><a href="https://tldrlegal.com/search?query=CC0-1.0">❗️CC0-1.0</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1495/PNG/32/preferencesdesktoptheme_102980.png" style="display:inline;" width="13" height="13"></code><br>An mkdocs theme geared towards making a personal landing page, with simpler navigation and heavily customisable style..</summary>

<a href="https://pawamoy.github.io/mkdocs-gallery/themes/landing/">
<img src="https://pawamoy.github.io/mkdocs-gallery/assets/img/landing.png" width="400" align="right">
</a>

- [GitHub](https://github.com/TEParsons/mkdocs-landing) (👨‍💻 4 · 🔀 2 · 📥 6 · 📦 8 · 📋 2 - 50% open · ⏱️ 16.02.2025)
- [PyPi](https://pypi.org/project/mkdocs-landing):
	```
	pip install mkdocs-landing
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#theme):
   ```yaml
   theme: landing
   ```
</details>
<details><summary><b><a href="https://github.com/kuri65536/mkdocs-theme-topdf">mkdocs-theme-topdf</a></b>  - 🥉6 ·  ⭐ 15 · 💤 · <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1495/PNG/32/preferencesdesktoptheme_102980.png" style="display:inline;" width="13" height="13"></code><br>A mkdocs theme for create PDF and printing with paged.js.</summary>

<a href="https://pawamoy.github.io/mkdocs-gallery/themes/topdf/">
<img src="https://pawamoy.github.io/mkdocs-gallery/assets/img/topdf.png" width="400" align="right">
</a>

- [GitHub](https://github.com/kuri65536/mkdocs-theme-topdf) (🔀 1 · 📦 4 · ⏱️ 22.05.2025)
- [PyPi](https://pypi.org/project/mkdocs-theme-topdf) (📥 93 / month):
	```
	pip install mkdocs-theme-topdf
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#theme):
   ```yaml
   theme: topdf
   ```
</details>
<details><summary><b><a href="https://github.com/g3xx/mkdocs-Github">GitHub</a></b>  - 🥉6 ·  ⭐ 6 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1495/PNG/32/preferencesdesktoptheme_102980.png" style="display:inline;" width="13" height="13"></code><br>Theme Mkdocs Like a Github. DEMO =.</summary>

<a href="https://pawamoy.github.io/mkdocs-gallery/themes/github/">
<img src="https://pawamoy.github.io/mkdocs-gallery/assets/img/github.png" width="400" align="right">
</a>

- [GitHub](https://github.com/g3xx/mkdocs-Github) (📦 13 · ⏱️ 25.02.2020)
- [PyPi](https://pypi.org/project/mkdocs-github):
	```
	pip install mkdocs-github
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#theme):
   ```yaml
   theme: github
   ```
</details>
<details><summary><b><a href="https://github.com/unverbuggt/mkdocs-risonia-theme">Risonia</a></b>  - 🥉6 ·  ⭐ 4 · <code>❗Unlicensed</code> · <code><img src="https://cdn.icon-icons.com/icons2/1495/PNG/32/preferencesdesktoptheme_102980.png" style="display:inline;" width="13" height="13"></code><br>A simple theme for MkDocs, using the w3.css framework and configurable color schemes.</summary>

<a href="https://pawamoy.github.io/mkdocs-gallery/themes/risonia/">
<img src="https://pawamoy.github.io/mkdocs-gallery/assets/img/risonia.png" width="400" align="right">
</a>

- [GitHub](https://github.com/unverbuggt/mkdocs-risonia-theme) (🔀 1 · 📦 4 · ⏱️ 31.12.2025)
- [PyPi](https://pypi.org/project/mkdocs-risonia-theme):
	```
	pip install mkdocs-risonia-theme
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#theme):
   ```yaml
   theme: risonia
   ```
   Extras:
   ```yaml
   plugins:
     - color-theme
     - w3css-classes
   ```
</details>
<details><summary><b><a href="https://github.com/noraj/mkdocs-windmill-dark">Windmill Dark</a></b>  - 🥉5 ·  ⭐ 38 · 💤 · <code>❗Unlicensed</code> · <code><img src="https://cdn.icon-icons.com/icons2/1495/PNG/32/preferencesdesktoptheme_102980.png" style="display:inline;" width="13" height="13"></code><br>Outstanding mkdocs theme with a focus on navigation and usability.</summary>

<a href="https://pawamoy.github.io/mkdocs-gallery/themes/windmill-dark/">
<img src="https://pawamoy.github.io/mkdocs-gallery/assets/img/windmill-dark.png" width="400" align="right">
</a>

- [GitHub](https://github.com/noraj/mkdocs-windmill-dark) (👨‍💻 4 · 🔀 11 · ⏱️ 12.05.2022)
- [PyPi](https://pypi.org/project/mkdocs-windmill-dark):
	```
	pip install mkdocs-windmill-dark
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#theme):
   ```yaml
   theme: windmill-dark
   ```
</details>
<details><summary><b><a href="https://github.com/notpushkin/mkdocs-alabaster">Alabaster</a></b>  - 🥉5 ·  ⭐ 36 · 💤 · <code>❗Unlicensed</code> · <code><img src="https://cdn.icon-icons.com/icons2/1495/PNG/32/preferencesdesktoptheme_102980.png" style="display:inline;" width="13" height="13"></code><br>Alabaster port for MkDocs.</summary>

<a href="https://pawamoy.github.io/mkdocs-gallery/themes/alabaster/">
<img src="https://pawamoy.github.io/mkdocs-gallery/assets/img/alabaster.png" width="400" align="right">
</a>

- [GitHub](https://github.com/notpushkin/mkdocs-alabaster) (👨‍💻 10 · 🔀 11 · 📋 17 - 17% open · ⏱️ 16.06.2020)
- [PyPi](https://pypi.org/project/mkdocs-alabaster):
	```
	pip install mkdocs-alabaster
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#theme):
   ```yaml
   theme: alabaster
   ```
</details>
<details><summary><b><a href="https://github.com/hfagerlund/mkdocs-docskimmer">docSkimmer</a></b>  - 🥉5 ·  ⭐ 20 · <code>❗Unlicensed</code> · <code><img src="https://cdn.icon-icons.com/icons2/1495/PNG/32/preferencesdesktoptheme_102980.png" style="display:inline;" width="13" height="13"></code><br>An accessible, skimmable theme for MkDocs.</summary>

<a href="https://pawamoy.github.io/mkdocs-gallery/themes/docskimmer/">
<img src="https://pawamoy.github.io/mkdocs-gallery/assets/img/docskimmer.png" width="400" align="right">
</a>

- [GitHub](https://github.com/hfagerlund/mkdocs-docskimmer) (⏱️ 17.12.2025)
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#theme):
   ```yaml
   theme: docskimmer
   ```
</details>
<details><summary><b><a href="https://github.com/daizutabi/mkdocs-ivory">Ivory</a></b>  - 🥉5 ·  ⭐ 10 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1495/PNG/32/preferencesdesktoptheme_102980.png" style="display:inline;" width="13" height="13"></code><br>Ivory theme for MkDocs.</summary>

<a href="https://pawamoy.github.io/mkdocs-gallery/themes/ivory/">
<img src="https://pawamoy.github.io/mkdocs-gallery/assets/img/ivory.png" width="400" align="right">
</a>

- [GitHub](https://github.com/daizutabi/mkdocs-ivory) (👨‍💻 2 · 🔀 6 · 📋 6 - 50% open · ⏱️ 16.06.2020)
- [PyPi](https://pypi.org/project/mkdocs-ivory):
	```
	pip install mkdocs-ivory
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#theme):
   ```yaml
   theme: ivory
   ```
</details>
<details><summary><b><a href="https://gitlab.com/lramage/mkdocs-bootstrap386">BOOTSTRAP386</a></b>  - 🥉4 ·  ⭐ 37 · 💤 · <code>❗Unlicensed</code> · <code><img src="https://cdn.icon-icons.com/icons2/1495/PNG/32/preferencesdesktoptheme_102980.png" style="display:inline;" width="13" height="13"></code><br>A vintage 1980s DOS inspired Twitter Bootstrap theme for MkDocs https://lramage.gitlab.io/mkdocs-bootstrap386.</summary>

<a href="https://pawamoy.github.io/mkdocs-gallery/themes/bootstrap386/">
<img src="https://pawamoy.github.io/mkdocs-gallery/assets/img/bootstrap386.png" width="400" align="right">
</a>

- [PyPi](https://pypi.org/project/mkdocs-bootstrap386):
	```
	pip install mkdocs-bootstrap386
	```
- [GitLab](https://gitlab.com/lramage/mkdocs-bootstrap386) (🔀 3 · 📋 7 - 57% open · ⏱️ 06.06.2018)
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#theme):
   ```yaml
   theme: bootstrap386
   ```
</details>
<details><summary><b><a href="https://gitlab.com/lramage/mkdocs-gitbook-theme">GitBook</a></b>  - 🥉4 ·  ⭐ 31 · 💤 · <code>❗Unlicensed</code> · <code><img src="https://cdn.icon-icons.com/icons2/1495/PNG/32/preferencesdesktoptheme_102980.png" style="display:inline;" width="13" height="13"></code><br>Default theme for GitBook for Mkdocs https://lramage.gitlab.io/mkdocs-gitbook-theme.</summary>

<a href="https://pawamoy.github.io/mkdocs-gallery/themes/gitbook/">
<img src="https://pawamoy.github.io/mkdocs-gallery/assets/img/gitbook.png" width="400" align="right">
</a>

- [PyPi](https://pypi.org/project/mkdocs-gitbook):
	```
	pip install mkdocs-gitbook
	```
- [GitLab](https://gitlab.com/lramage/mkdocs-gitbook-theme) (🔀 15 · 📋 19 - 47% open · ⏱️ 17.12.2018)
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#theme):
   ```yaml
   theme: gitbook
   ```
</details>
<details><summary><b><a href="https://github.com/mberneti/mkdocs-rtl">mkdocs-rtl</a></b>  - 🥉4 ·  ⭐ 25 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code><br>mkdocs rtl theme based on mkdocs-material.</summary>

- [GitHub](https://github.com/mberneti/mkdocs-rtl) (👨‍💻 2 · 🔀 4 · 📋 2 - 50% open · ⏱️ 22.10.2017)
</details>
<details><summary><b><a href="https://gitlab.com/kaliko/mkdocs-cluster">Cluster</a></b>  - 🥉1 ·  ⭐ 6 · 💤 · <code>❗Unlicensed</code> · <code><img src="https://cdn.icon-icons.com/icons2/1495/PNG/32/preferencesdesktoptheme_102980.png" style="display:inline;" width="13" height="13"></code><br>Another bootstrap theme for MkDocs.</summary>

<a href="https://pawamoy.github.io/mkdocs-gallery/themes/cluster/">
<img src="https://pawamoy.github.io/mkdocs-gallery/assets/img/cluster.png" width="400" align="right">
</a>

- [PyPi](https://pypi.org/project/mkdocs-cluster):
	```
	pip install mkdocs-cluster
	```
- [GitLab](https://gitlab.com/kaliko/mkdocs-cluster) (🔀 2 · ⏱️ 02.06.2016)
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#theme):
   ```yaml
   theme: cluster
   ```
</details>
<br>

## 💻 API documentation building

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://github.com/mkdocstrings/mkdocstrings">mkdocstrings</a></b>  - 🥇33 ·  ⭐ 2.1K · <code><a href="http://bit.ly/3hkKRql">ISC</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Automatic documentation from sources, for MkDocs.</summary>

- [GitHub](https://github.com/mkdocstrings/mkdocstrings) (👨‍💻 55 · 🔀 120 · 📦 28K · 📋 470 - 1% open · ⏱️ 15.04.2026)
- [PyPi](https://pypi.org/project/mkdocstrings) (📥 7M / month):
	```
	pip install mkdocstrings
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - mkdocstrings
   ```
</details>
<details><summary><b><a href="https://github.com/mkdocstrings/python">mkdocstrings-python</a></b>  - 🥇23 ·  ⭐ 270 · <code><a href="http://bit.ly/3hkKRql">ISC</a></code><br>A Python handler for mkdocstrings.</summary>

- [GitHub](https://github.com/mkdocstrings/python) (👨‍💻 29 · 🔀 51 · 📋 210 - 4% open · ⏱️ 05.06.2026)
- [PyPi](https://pypi.org/project/mkdocstrings-python) (📥 9.9M / month):
	```
	pip install mkdocstrings-python
	```
</details>
<details><summary><b><a href="https://github.com/mkdocs/mkdocs-click">mkdocs-click</a></b>  - 🥇23 ·  ⭐ 150 · <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1459/PNG/32/2799201-jigsaw-processing_99781.png" style="display:inline;" width="13" height="13"></code><br>An MkDocs extension to generate documentation for Click command line applications.</summary>

- [GitHub](https://github.com/mkdocs/mkdocs-click) (👨‍💻 16 · 🔀 22 · 📦 1.2K · 📋 35 - 54% open · ⏱️ 18.06.2025)
- [PyPi](https://pypi.org/project/mkdocs-click) (📥 920K / month):
	```
	pip install mkdocs-click
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#markdown_extensions):
   ```yaml
   markdown_extensions:
     - mkdocs-click
   ```
</details>
<details><summary><b><a href="https://github.com/Neoteroi/mkdocs-plugins">MkDocsOAD</a></b>  - 🥈20 ·  ⭐ 170 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code> · <code><img src="https://cdn.icon-icons.com/icons2/1459/PNG/32/2799201-jigsaw-processing_99781.png" style="display:inline;" width="13" height="13"></code><br>Plugin for MkDocs to generate human readable documentation from OpenAPI Documentation Version 3 (also known as Swagger..</summary>

- [GitHub](https://github.com/Neoteroi/mkdocs-plugins) (👨‍💻 13 · 🔀 13 · 📥 22K · 📦 510 · 📋 47 - 44% open · ⏱️ 23.11.2025)
- [PyPi](https://pypi.org/project/neoteroi-mkdocs) (📥 150K / month):
	```
	pip install neoteroi-mkdocs
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - neoteroi.mkdocsoad
     - neoteroi.contribs
   markdown_extensions:
     - neoteroi.cards
     - neoteroi.timeline
     - neoteroi.projects
     - neoteroi.spantable
   ```
</details>
<details><summary><b><a href="https://github.com/daizutabi/mkapi">MkApi</a></b>  - 🥈19 ·  ⭐ 120 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>MkDocs plugin for automatic API documentation generation from Python docstrings.</summary>

- [GitHub](https://github.com/daizutabi/mkapi) (👨‍💻 6 · 🔀 17 · 📦 270 · 📋 150 - 2% open · ⏱️ 30.03.2026)
- [PyPi](https://pypi.org/project/mkapi) (📥 9.7K / month):
	```
	pip install mkapi
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - mkapi
   ```
</details>
<details><summary><b><a href="https://github.com/JakubAndrysek/MkDoxy">mkdoxy</a></b>  - 🥈16 ·  ⭐ 120 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Automatically generates API documentation for your project based on Doxygen comments and code snippets in your..</summary>

- [GitHub](https://github.com/JakubAndrysek/MkDoxy) (👨‍💻 18 · 🔀 34 · 📦 72 · 📋 74 - 32% open · ⏱️ 29.08.2025)
- [PyPi](https://pypi.org/project/mkdoxy):
	```
	pip install mkdoxy
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - mkdoxy
   ```
</details>
<details><summary><b><a href="https://github.com/mkdocstrings/crystal">mkdocstrings-crystal</a></b>  - 🥈15 ·  ⭐ 31 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code><br>Crystal language doc generator for https://github.com/mkdocstrings/mkdocstrings.</summary>

- [GitHub](https://github.com/mkdocstrings/crystal) (👨‍💻 3 · 🔀 3 · 📋 8 - 37% open · ⏱️ 08.11.2025)
- [PyPi](https://pypi.org/project/mkdocstrings-crystal) (📥 32K / month):
	```
	pip install mkdocstrings-crystal
	```
</details>
<details><summary><b><a href="https://github.com/jcayers20/mkdocs-autoapi">mkdocs-autoapi</a></b>  - 🥈15 ·  ⭐ 21 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>MkDocs plugin providing automatic API reference generation.</summary>

- [GitHub](https://github.com/jcayers20/mkdocs-autoapi) (👨‍💻 2 · 🔀 1 · 📥 10 · 📦 130 · 📋 37 - 21% open · ⏱️ 29.01.2026)
- [PyPi](https://pypi.org/project/mkdocs-autoapi) (📥 29K / month):
	```
	pip install mkdocs-autoapi
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - mkdocs-autoapi
   ```
</details>
<details><summary><b><a href="https://github.com/syn54x/mkdocs-typer2">mkdocs-typer2</a></b>  - 🥈15 ·  ⭐ 19 · <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Mkdocs Plugin For Typer CLIs.</summary>

- [GitHub](https://github.com/syn54x/mkdocs-typer2) (🔀 1 · 📦 41 · ⏱️ 27.05.2026)
- [PyPi](https://pypi.org/project/mkdocs-typer2) (📥 9.6K / month):
	```
	pip install mkdocs-typer2
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - mkdocs-typer2
   ```
</details>
<details><summary><b><a href="https://github.com/bruce-szalwinski/mkdocs-typer">mkdocs-typer</a></b>  - 🥈13 ·  ⭐ 33 · 💤 · <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1459/PNG/32/2799201-jigsaw-processing_99781.png" style="display:inline;" width="13" height="13"></code><br>An MkDocs extension to generate documentation for Typer command line applications.</summary>

- [GitHub](https://github.com/bruce-szalwinski/mkdocs-typer) (🔀 4 · 📋 10 - 70% open · ⏱️ 21.06.2023)
- [PyPi](https://pypi.org/project/mkdocs-typer) (📥 16K / month):
	```
	pip install mkdocs-typer
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#markdown_extensions):
   ```yaml
   markdown_extensions:
     - mkdocs-typer
   ```
</details>
<details><summary><b><a href="https://github.com/watermarkhu/mkdocstrings-matlab">mkdocstrings-matlab</a></b>  - 🥈13 ·  ⭐ 15 · <code><a href="http://bit.ly/3hkKRql">ISC</a></code><br>A MATLAB handler for mkdocstrings, automatic documentation from sources.</summary>

- [GitHub](https://github.com/watermarkhu/mkdocstrings-matlab) (👨‍💻 5 · 🔀 2 · 📥 17 · 📦 2 · 📋 14 - 35% open · ⏱️ 07.06.2026)
- [PyPi](https://pypi.org/project/mkdocstrings-matlab) (📥 580 / month):
	```
	pip install mkdocstrings-matlab
	```
</details>
<details><summary><b><a href="https://github.com/tlambert03/mkdocs-api-autonav">mkdocs-api-autonav</a></b>  - 🥉12 ·  ⭐ 43 · <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>MkDocs plugin for autogenerating API docs with navigation.</summary>

- [GitHub](https://github.com/tlambert03/mkdocs-api-autonav) (👨‍💻 2 · 🔀 3 · 📥 61 · 📦 260 · 📋 17 - 17% open · ⏱️ 04.06.2026)
- [PyPi](https://pypi.org/project/mkdocs-api-autonav):
	```
	pip install mkdocs-api-autonav
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - api-autonav
   ```
</details>
<details><summary><b><a href="https://github.com/lovelydinosaur/mkautodoc">MkAutoDoc</a></b>  - 🥉11 ·  ⭐ 230 · 💤 · <code><a href="https://tldrlegal.com/search?query=BSD">❗️BSD</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1459/PNG/32/2799201-jigsaw-processing_99781.png" style="display:inline;" width="13" height="13"></code><br>Auto documentation for MkDocs.</summary>

- [GitHub](https://github.com/lovelydinosaur/mkautodoc) (👨‍💻 7 · 🔀 18 · 📋 18 - 38% open · ⏱️ 26.09.2022)
- [PyPi](https://pypi.org/project/mkautodoc) (📥 18K / month):
	```
	pip install mkautodoc
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#markdown_extensions):
   ```yaml
   markdown_extensions:
     - mkautodoc
   ```
</details>
<details><summary><b><a href="https://github.com/greenape/mktheapidocs">mktheapidocs</a></b>  - 🥉10 ·  ⭐ 12 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Numpydocs - mkdocs friendly markdown.</summary>

- [GitHub](https://github.com/greenape/mktheapidocs) (👨‍💻 6 · 🔀 3 · 📋 16 - 62% open · ⏱️ 10.06.2022)
- [PyPi](https://pypi.org/project/mktheapidocs) (📥 700 / month):
	```
	pip install mktheapidocs
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - mktheapidocs
   ```
</details>
<details><summary><b><a href="https://github.com/mkdocstrings/shell">mkdocstrings-shell</a></b>  - 🥉10 ·  ⭐ 5 · <code><a href="http://bit.ly/3hkKRql">ISC</a></code><br>A shell scripts/libraries handler for mkdocstrings.</summary>

- [GitHub](https://github.com/mkdocstrings/shell) (📦 74 · 📋 5 - 20% open · ⏱️ 19.09.2025)
</details>
<details><summary><b><a href="https://github.com/mkdocstrings/vba">mkdocstrings-vba</a></b>  - 🥉10 ·  ⭐ 4 · <code><a href="http://bit.ly/3hkKRql">ISC</a></code><br>VBA handler for mkdocstrings.</summary>

- [GitHub](https://github.com/mkdocstrings/vba) (👨‍💻 3 · 🔀 1 · 📦 3 · 📋 9 - 22% open · ⏱️ 01.09.2025)
- [PyPi](https://pypi.org/project/mkdocstrings-vba) (📥 200 / month):
	```
	pip install mkdocstrings-vba
	```
</details>
<details><summary><b><a href="https://github.com/Wesztman/mkdocs-azure-pipelines">mkdocs-azure-pipelines</a></b>  - 🥉9 ·  ⭐ 11 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Generate mkdocs documentation from Azure Pipelines yaml files.</summary>

- [GitHub](https://github.com/Wesztman/mkdocs-azure-pipelines) (👨‍💻 3 · 🔀 1 · 📦 2 · 📋 2 - 50% open · ⏱️ 30.04.2026)
- [PyPi](https://pypi.org/project/mkdocs-azure-pipelines) (📥 160 / month):
	```
	pip install mkdocs-azure-pipelines
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - mkdocs-azure-pipelines
   ```
</details>
<details><summary><b><a href="https://github.com/obegron/mkdocs-pipeline-visualizer">mkdocs-pipeline-visualizer</a></b>  - 🥉8 ·  ⭐ 2 · <code><a href="http://bit.ly/3rqEWVr">BSD-2</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Generates MD documentation from tekton pipelines and tasks.</summary>

- [GitHub](https://github.com/obegron/mkdocs-pipeline-visualizer) (👨‍💻 4 · 📦 3 · ⏱️ 14.04.2026)
- [PyPi](https://pypi.org/project/mkdocs-pipeline-visualizer) (📥 290 / month):
	```
	pip install mkdocs-pipeline-visualizer
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - pipeline-visualizer
   ```
</details>
<details><summary><b><a href="https://github.com/AlexandreKempf/automacdoc">automacdoc</a></b>  - 🥉7 ·  ⭐ 44 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code><br>Automatic generation of documentation for mkdocs.</summary>

- [GitHub](https://github.com/AlexandreKempf/automacdoc) (👨‍💻 6 · 🔀 10 · 📋 5 - 80% open · ⏱️ 29.12.2020)
- [PyPi](https://pypi.org/project/automacdoc) (📥 180 / month):
	```
	pip install automacdoc
	```
</details>
<details><summary><b><a href="https://github.com/Kl0ven/mkdocs-material-adr">mkdocs-material-adr</a></b>  - 🥉6 ·  ⭐ 17 · 💤 · <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>ADR for MkDocss Material Theme.</summary>

- [GitHub](https://github.com/Kl0ven/mkdocs-material-adr) (👨‍💻 2 · 🔀 2 · 📦 12 · 📋 5 - 60% open · ⏱️ 03.04.2025)
- [PyPi](https://pypi.org/project/mkdocs-material-adr):
	```
	pip install mkdocs-material-adr
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - mkdocs-material-adr/adr
   ```
</details>
<details><summary><b><a href="https://github.com/JakubAndrysek/mkdocs-typedoc">mkdocs-typedoc</a></b>  - 🥉6 ·  ⭐ 9 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>The MkDocs-Typedoc Plugin is a MkDocs plugin that allows you to include TypeDoc documentation in your MkDocs site.</summary>

- [GitHub](https://github.com/JakubAndrysek/mkdocs-typedoc) (👨‍💻 2 · 🔀 2 · 📋 3 - 33% open · ⏱️ 03.05.2024)
- [PyPi](https://pypi.org/project/mkdocs-typedoc) (📥 930 / month):
	```
	pip install mkdocs-typedoc
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - typedoc
   ```
</details>
<details><summary><b><a href="https://github.com/tkamenoko/inari">inari</a></b>  - 🥉6 ·  ⭐ 5 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Write docstrings in markdown!.</summary>

- [GitHub](https://github.com/tkamenoko/inari) (📦 9 · 📋 2 - 50% open · ⏱️ 10.07.2021)
- [PyPi](https://pypi.org/project/inari) (📥 140 / month):
	```
	pip install inari
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - inari
   ```
</details>
<details><summary><b><a href="https://github.com/pieterdavid/mkdocs-doxygen-plugin">doxygen</a></b>  - 🥉5 ·  ⭐ 18 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>A Doxygen plugin for MkDocs.</summary>

- [GitHub](https://github.com/pieterdavid/mkdocs-doxygen-plugin) (👨‍💻 3 · 🔀 5 · ⏱️ 04.12.2020)
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - doxygen
   ```
</details>
<details><summary><b><a href="https://github.com/idlesign/mkdocs-apidescribed-plugin">mkdocs-apidescribed-plugin</a></b>  - 🥉4 ·  ⭐ 1 · 💤 · <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>mkdocs plugin to generate API documentation for Python programs.</summary>

- [GitHub](https://github.com/idlesign/mkdocs-apidescribed-plugin) (⏱️ 24.05.2025)
- [PyPi](https://pypi.org/project/mkdocs-apidescribed-plugin):
	```
	pip install mkdocs-apidescribed-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - apidescribed
   ```
</details>
<details><summary><b><a href="https://github.com/g6123/mkdocs-yaarg-plugin">mkdocs-yaarg-plugin</a></b>  - 🥉2 ·  ⭐ 2 · 💤 · <code>❗Unlicensed</code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Yet Another API Reference Generator plugin for MKDocs.</summary>

- [GitHub](https://github.com/g6123/mkdocs-yaarg-plugin) (📦 2 · ⏱️ 14.03.2021)
- [PyPi](https://pypi.org/project/mkdocs-yaarg-plugin) (📥 77 / month):
	```
	pip install mkdocs-yaarg-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - yaarg
   ```
</details>
<details><summary><b><a href="https://pypi.org/project/ansible-mkdocs/">ansible-document</a></b>  - 🥉1 · <code>❗Unlicensed</code><br>Auto-generate ansible role documentation.</summary>

- [PyPi](https://pypi.org/project/ansible-mkdocs):
	```
	pip install ansible-mkdocs
	```
</details>
<br>

## 💬 Blogging

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://github.com/Guts/mkdocs-rss-plugin">rss</a></b>  - 🥇22 ·  ⭐ 130 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>MkDocs plugin to generate a RSS feeds for created and updated pages, using git log and YAML frontmatter (page.meta).</summary>

- [GitHub](https://github.com/Guts/mkdocs-rss-plugin) (👨‍💻 20 · 🔀 30 · 📥 450 · 📋 62 - 22% open · ⏱️ 03.06.2026)
- [PyPi](https://pypi.org/project/mkdocs-rss-plugin) (📥 180K / month):
	```
	pip install mkdocs-rss-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - rss
   ```
</details>
<details><summary><b><a href="https://github.com/liang2kl/mkdocs-blogging-plugin">mkdocs-blogging-plugin</a></b>  - 🥈19 ·  ⭐ 91 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Add blogging feature to your MkDocs site.</summary>

- [GitHub](https://github.com/liang2kl/mkdocs-blogging-plugin) (👨‍💻 7 · 🔀 15 · 📥 25 · 📦 320 · 📋 41 - 12% open · ⏱️ 21.07.2023)
- [PyPi](https://pypi.org/project/mkdocs-blogging-plugin) (📥 24K / month):
	```
	pip install mkdocs-blogging-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - blogging
   ```
</details>
<details><summary><b><a href="https://github.com/mkdocs-publisher/mkdocs-publisher">Publisher for MkDocs - blog</a></b>  - 🥈13 ·  ⭐ 130 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Blogging engine with support for categories, tags and archive.</summary>

- [GitHub](https://github.com/mkdocs-publisher/mkdocs-publisher) (👨‍💻 4 · 🔀 11 · 📥 140 · 📦 99 · 📋 31 - 25% open · ⏱️ 26.11.2025)
- [PyPi](https://pypi.org/project/mkdocs-publisher):
	```
	pip install mkdocs-publisher
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - pub-blog
   ```
</details>
<details><summary><b><a href="https://github.com/lyz-code/mkdocs-newsletter">newsletter</a></b>  - 🥉11 ·  ⭐ 35 · 💤 · <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Automatically create newsletters from the changes in a mkdocs repository.</summary>

- [GitHub](https://github.com/lyz-code/mkdocs-newsletter) (👨‍💻 3 · 🔀 2 · 📦 81 · 📋 10 - 30% open · ⏱️ 27.05.2024)
- [PyPi](https://pypi.org/project/mkdocs-newsletter) (📥 390 / month):
	```
	pip install mkdocs-newsletter
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - mkdocs-newsletter
   ```
</details>
<details><summary><b><a href="https://github.com/fmaida/mkdocs-blog-plugin">Blogs for MkDocs</a></b>  - 🥉9 ·  ⭐ 19 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>This plugin for MkDocs allows to keeps a really simple blog section inside your documentation site.</summary>

- [GitHub](https://github.com/fmaida/mkdocs-blog-plugin) (🔀 3 · 📦 220 · 📋 2 - 50% open · ⏱️ 13.04.2020)
- [PyPi](https://pypi.org/project/mkdocs-blog-plugin):
	```
	pip install mkdocs-blog-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - blog
   ```
</details>
<details><summary><b><a href="https://github.com/derJD/python-mkblog">python-mkblog</a></b>  - 🥉3 ·  ⭐ 3 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>This is a MkDocs Plugin adding basic blogging functionality by parsing a `blog` directory ontop of your usual `docs`..</summary>

- [GitHub](https://github.com/derJD/python-mkblog) (👨‍💻 2 · 🔀 1 · ⏱️ 14.04.2021)
- [PyPi](https://pypi.org/project/mkblog):
	```
	pip install mkblog
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - mkblog
   ```
</details>
<details><summary><b><a href="https://github.com/andyoakley/mkdocs-blog">blog</a></b>  - 🥉2 ·  ⭐ 15 · 💤 · <code>❗Unlicensed</code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Blogging in mkdocs.</summary>

- [GitHub](https://github.com/andyoakley/mkdocs-blog) (🔀 6 · 📋 6 - 83% open · ⏱️ 02.11.2020)
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - blog
   ```
</details>
<br>

## 📊 Charts, Images, Tables & Graphs

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://github.com/mikitex70/plantuml-markdown">plantuml-markdown</a></b>  - 🥇27 ·  ⭐ 220 · <code><a href="http://bit.ly/3rqEWVr">BSD-2</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1459/PNG/32/2799201-jigsaw-processing_99781.png" style="display:inline;" width="13" height="13"></code><br>PlantUML plugin for Python-Markdown.</summary>

- [GitHub](https://github.com/mikitex70/plantuml-markdown) (👨‍💻 30 · 🔀 54 · 📦 1.8K · 📋 72 - 1% open · ⏱️ 18.04.2026)
- [PyPi](https://pypi.org/project/plantuml-markdown) (📥 770K / month):
	```
	pip install plantuml-markdown
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#markdown_extensions):
   ```yaml
   markdown_extensions:
     - plantuml_markdown
   ```
</details>
<details><summary><b><a href="https://github.com/blueswen/mkdocs-glightbox">MkDocs GLightbox</a></b>  - 🥇25 ·  ⭐ 190 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>A MkDocs plugin supports image lightbox (zoom effect) with GLightbox.</summary>

- [GitHub](https://github.com/blueswen/mkdocs-glightbox) (👨‍💻 9 · 🔀 22 · 📥 46 · 📦 6.1K · 📋 58 - 43% open · ⏱️ 08.03.2026)
- [PyPi](https://pypi.org/project/mkdocs-glightbox) (📥 1.4M / month):
	```
	pip install mkdocs-glightbox
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - glightbox
   ```
</details>
<details><summary><b><a href="https://github.com/fralau/mkdocs-mermaid2-plugin">mermaid2</a></b>  - 🥇23 ·  ⭐ 280 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>A Mermaid graphs plugin for mkdocs.</summary>

- [GitHub](https://github.com/fralau/mkdocs-mermaid2-plugin) (👨‍💻 17 · 🔀 33 · 📦 3.8K · 📋 88 - 17% open · ⏱️ 14.05.2026)
- [PyPi](https://pypi.org/project/mkdocs-mermaid2-plugin) (📥 840K / month):
	```
	pip install mkdocs-mermaid2-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - mermaid2
   ```
</details>
<details><summary><b><a href="https://github.com/MikhailKravets/mkdocs_puml">mkdocs_puml</a></b>  - 🥇20 ·  ⭐ 63 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Inline PlantUML diagrams in your MkDocs documentation.</summary>

- [GitHub](https://github.com/MikhailKravets/mkdocs_puml) (👨‍💻 10 · 🔀 18 · 📦 79 · 📋 34 - 32% open · ⏱️ 03.03.2026)
- [PyPi](https://pypi.org/project/mkdocs-puml) (📥 61K / month):
	```
	pip install mkdocs-puml
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - plantuml
   ```
</details>
<details><summary><b><a href="https://github.com/AVATEAM-IT-SYSTEMHAUS/mkdocs-kroki-plugin">kroki</a></b>  - 🥈19 ·  ⭐ 63 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>MkDocs plugin for Kroki-Diagrams.</summary>

- [GitHub](https://github.com/AVATEAM-IT-SYSTEMHAUS/mkdocs-kroki-plugin) (👨‍💻 19 · 🔀 27 · 📦 93 · ⏱️ 13.04.2026)
- [PyPi](https://pypi.org/project/mkdocs-kroki-plugin):
	```
	pip install mkdocs-kroki-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - kroki
   ```
</details>
<details><summary><b><a href="https://github.com/soulless-viewer/mkdocs-video">MkDocs Video</a></b>  - 🥈18 ·  ⭐ 83 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>MkDocs Video plugin.</summary>

- [GitHub](https://github.com/soulless-viewer/mkdocs-video) (👨‍💻 5 · 🔀 13 · 📥 76 · 📦 1.1K · ⏱️ 04.01.2024)
- [PyPi](https://pypi.org/project/mkdocs-video) (📥 190K / month):
	```
	pip install mkdocs-video
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - mkdocs-video
   ```
</details>
<details><summary><b><a href="https://github.com/landmaj/mkdocs-d2-plugin">mkdocs-d2-plugin</a></b>  - 🥈17 ·  ⭐ 38 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>A plugin for embedding D2 diagrams in MkDocs.</summary>

- [GitHub](https://github.com/landmaj/mkdocs-d2-plugin) (👨‍💻 4 · 🔀 8 · 📦 34 · 📋 20 - 5% open · ⏱️ 09.04.2026)
- [PyPi](https://pypi.org/project/mkdocs-d2-plugin) (📥 49K / month):
	```
	pip install mkdocs-d2-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - d2
   ```
</details>
<details><summary><b><a href="https://github.com/gisce/markdown-blockdiag">Markdown blockdiag</a></b>  - 🥈16 ·  ⭐ 30 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1459/PNG/32/2799201-jigsaw-processing_99781.png" style="display:inline;" width="13" height="13"></code><br>blockdiag extension for Python Markdown.</summary>

- [GitHub](https://github.com/gisce/markdown-blockdiag) (👨‍💻 5 · 🔀 8 · 📦 140 · 📋 6 - 50% open · ⏱️ 22.11.2023)
- [PyPi](https://pypi.org/project/markdown-blockdiag) (📥 3K / month):
	```
	pip install markdown-blockdiag
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#markdown_extensions):
   ```yaml
   markdown_extensions:
     - markdown_blockdiag
   ```
</details>
<details><summary><b><a href="https://github.com/christo-ph/mkdocs_build_plantuml">build-plantuml</a></b>  - 🥈15 ·  ⭐ 78 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>MkDocs plugin to help generate your plantuml images locally or remotely as files (NOT inline).</summary>

- [GitHub](https://github.com/christo-ph/mkdocs_build_plantuml) (👨‍💻 14 · 🔀 16 · 📦 150 · 📋 27 - 3% open · ⏱️ 24.02.2026)
- [PyPi](https://pypi.org/project/mkdocs-build-plantuml-plugin):
	```
	pip install mkdocs-build-plantuml-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - build_plantuml
   ```
</details>
<details><summary><b><a href="https://github.com/daxcore/mkdocs-obsidian-interactive-graph-plugin">Interactive Graph</a></b>  - 🥈15 ·  ⭐ 35 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>interactive graph for Material for MkDocs like Obsidian, refer demo:.</summary>

- [GitHub](https://github.com/daxcore/mkdocs-obsidian-interactive-graph-plugin) (👨‍💻 4 · 🔀 7 · 📦 52 · 📋 6 - 16% open · ⏱️ 10.02.2026)
- [PyPi](https://pypi.org/project/mkdocs-obsidian-interactive-graph-plugin) (📥 600 / month):
	```
	pip install mkdocs-obsidian-interactive-graph-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - obsidian-interactive-graph
   ```
</details>
<details><summary><b><a href="https://github.com/timvink/mkdocs-table-reader-plugin">table-reader</a></b>  - 🥈13 ·  ⭐ 160 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>MkDocs plugin that enables a markdown tag like {{ read_csv(table.csv) }} to directly insert various table formats into..</summary>

- [GitHub](https://github.com/timvink/mkdocs-table-reader-plugin) (👨‍💻 9 · 🔀 27 · 📋 57 - 7% open · ⏱️ 19.04.2025)
- [PyPi](https://pypi.org/project/mkdocs-table-reader-plugin):
	```
	pip install mkdocs-table-reader-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - table-reader
   ```
</details>
<details><summary><b><a href="https://github.com/PLAYG0N/mkdocs-panzoom">panzoom</a></b>  - 🥈13 ·  ⭐ 66 · 📉 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>MkDocs Plugin to enable pan & zoom on images and mermaid/d2 diagrams.</summary>

- [GitHub](https://github.com/PLAYG0N/mkdocs-panzoom) (👨‍💻 7 · 🔀 2 · 📥 70 · 📦 65 · 📋 34 - 17% open · ⏱️ 22.12.2025)
- [PyPi](https://pypi.org/project/mkdocs-panzoom-plugin):
	```
	pip install mkdocs-panzoom-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - panzoom
   ```
</details>
<details><summary><b><a href="https://github.com/g-provost/lightgallery-markdown">Lightgallery</a></b>  - 🥈11 ·  ⭐ 27 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1459/PNG/32/2799201-jigsaw-processing_99781.png" style="display:inline;" width="13" height="13"></code><br>Markdown extension to wrap images in a lightbox.</summary>

- [GitHub](https://github.com/g-provost/lightgallery-markdown) (👨‍💻 6 · 🔀 5 · 📦 110 · 📋 11 - 54% open · ⏱️ 07.10.2023)
- [PyPi](https://pypi.org/project/lightgallery):
	```
	pip install lightgallery
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#markdown_extensions):
   ```yaml
   markdown_extensions:
     - lightgallery
   ```
</details>
<details><summary><b><a href="https://github.com/LukeCarrier/mkdocs-drawio-exporter">drawio-exporter</a></b>  - 🥈10 ·  ⭐ 85 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Exports your Draw.io diagrams at build time for easier embedding into your documentation.</summary>

- [GitHub](https://github.com/LukeCarrier/mkdocs-drawio-exporter) (👨‍💻 5 · 🔀 9 · 📋 35 - 14% open · ⏱️ 25.05.2025)
- [PyPi](https://pypi.org/project/mkdocs-drawio-exporter):
	```
	pip install mkdocs-drawio-exporter
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - drawio-exporter
   ```
</details>
<details><summary><b><a href="https://github.com/timvink/mkdocs-charts-plugin">charts</a></b>  - 🥈9 ·  ⭐ 92 · 📉 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Mkdocs plugin to add plots from data using vegalite.</summary>

- [GitHub](https://github.com/timvink/mkdocs-charts-plugin) (👨‍💻 5 · 🔀 7 · 📋 20 - 15% open · ⏱️ 02.09.2025)
- [PyPi](https://pypi.org/project/mkdocs-charts-plugin):
	```
	pip install mkdocs-charts-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - charts
   ```
</details>
<details><summary><b><a href="https://github.com/bczsalba/Termage">Termage</a></b>  - 🥈9 ·  ⭐ 30 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Generate SVGs from any Python code, even in your documentation.</summary>

- [GitHub](https://github.com/bczsalba/Termage) (🔀 1 · 📦 3 · 📋 5 - 20% open · ⏱️ 23.08.2022)
- [PyPi](https://pypi.org/project/Termage):
	```
	pip install Termage
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - termage
   ```
</details>
<details><summary><b><a href="https://github.com/axiros/docutools">docutools</a></b>  - 🥈9 ·  ⭐ 27 · <code><a href="http://bit.ly/3rqEWVr">BSD-2</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Dev Centric Tools for Mkdocs Based Documentation.</summary>

- [GitHub](https://github.com/axiros/docutools) (👨‍💻 5 · 📋 2 - 50% open · ⏱️ 09.11.2025)
- [PyPi](https://pypi.org/project/docutools) (📥 230 / month):
	```
	pip install docutools
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - lcd-find-pages
     - lcd-custom-dir
     - lcd-blacklist
     - lcd-lp
     - lcd-md-replace
     - lcd-page-tree
     - lcd-stats
   ```
</details>
<details><summary><b><a href="https://github.com/six-two/mkdocs-badges">badges</a></b>  - 🥈9 ·  ⭐ 17 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Add badges to your mkdocs page.</summary>

- [GitHub](https://github.com/six-two/mkdocs-badges) (👨‍💻 2 · 🔀 3 · ⏱️ 23.05.2026)
- [PyPi](https://pypi.org/project/mkdocs-badges) (📥 3.9K / month):
	```
	pip install mkdocs-badges
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - badges
   ```
</details>
<details><summary><b><a href="https://oembedpy.readthedocs.io/en/stable/integrations/mkdocs/">oEmbedPy</a></b>  - 🥈9 ·  ⭐ 8 · 📉 · <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>MkDocs plugin to render rich contents from URL by oEmbed API.</summary>

- [GitHub](https://github.com/attakei/oEmbedPy) (👨‍💻 2 · 🔀 1 · 📥 45 · 📦 17 · 📋 8 - 62% open · ⏱️ 27.12.2025)
- [PyPi](https://pypi.org/project/oEmbedPy):
	```
	pip install oEmbedPy
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - oembedpy
   ```
</details>
<details><summary><b><a href="https://github.com/JakubAndrysek/mkdocs-resize-images">mkdocs-resize-images</a></b>  - 🥈9 ·  ⭐ 5 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>MkDocs plugin to resize images according to the configuration.</summary>

- [GitHub](https://github.com/JakubAndrysek/mkdocs-resize-images) (🔀 1 · 📦 13 · ⏱️ 04.11.2023)
- [PyPi](https://pypi.org/project/mkdocs-resize-images) (📥 710 / month):
	```
	pip install mkdocs-resize-images
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - resize-images
   ```
</details>
<details><summary><b><a href="https://github.com/AnH0ang/mkdocs-matplotlib">mkdocs-matplotlib</a></b>  - 🥈9 ·  ⭐ 4 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>A mkdocs plugin to automatically render matplotlib figure in your documenation.</summary>

- [GitHub](https://github.com/AnH0ang/mkdocs-matplotlib) (👨‍💻 2 · 🔀 2 · 📥 160 · ⏱️ 20.06.2022)
- [PyPi](https://pypi.org/project/mkdocs-matplotlib) (📥 1.8K / month):
	```
	pip install mkdocs-matplotlib
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - mkdocs_matplotlib
   ```
</details>
<details><summary><b><a href="https://github.com/madebyherzblut/mkdocs-bpmn-js">mkdocs-bpmn-js</a></b>  - 🥈9 ·  ⭐ 3 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>MkDocs plugin to embed BPMN diagrams.</summary>

- [GitHub](https://github.com/madebyherzblut/mkdocs-bpmn-js) (🔀 1 · 📥 4 · 📦 1 · ⏱️ 01.08.2025)
- [PyPi](https://pypi.org/project/mkdocs-bpmn-js) (📥 1.8K / month):
	```
	pip install mkdocs-bpmn-js
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - bpmn-js
   ```
</details>
<details><summary><b><a href="https://github.com/zoni/mkdocs-diagrams">mkdocs-diagrams</a></b>  - 🥉8 ·  ⭐ 33 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>MkDocs plugin to render Diagrams files.</summary>

- [GitHub](https://github.com/zoni/mkdocs-diagrams) (🔀 3 · 📦 85 · 📋 3 - 33% open · ⏱️ 04.09.2020)
- [PyPi](https://pypi.org/project/mkdocs-diagrams):
	```
	pip install mkdocs-diagrams
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - diagrams
   ```
</details>
<details><summary><b><a href="https://github.com/pugong/mkdocs-mermaid-plugin">markdownmermaid</a></b>  - 🥉8 ·  ⭐ 27 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>A MkDocs plugin that support mermaid graph in markdown file.</summary>

- [GitHub](https://github.com/pugong/mkdocs-mermaid-plugin) (👨‍💻 2 · 🔀 15 · 📦 130 · 📋 6 - 33% open · ⏱️ 26.05.2019)
- [PyPi](https://pypi.org/project/mkdocs-mermaid-plugin):
	```
	pip install mkdocs-mermaid-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - markdownmermaid
   ```
</details>
<details><summary><b><a href="https://github.com/haoda-li/mkdocs-plotly-plugin">plotly charts</a></b>  - 🥉8 ·  ⭐ 13 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Mkdocs plugin to add interactive charts with Plotly.js.</summary>

- [GitHub](https://github.com/haoda-li/mkdocs-plotly-plugin) (👨‍💻 4 · 🔀 1 · 📋 4 - 25% open · ⏱️ 02.06.2026)
- [PyPi](https://pypi.org/project/mkdocs-plotly-plugin) (📥 4.2K / month):
	```
	pip install mkdocs-plotly-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - plotly
   ```
</details>
<details><summary><b><a href="https://github.com/stuebersystems/mkdocs-img2fig-plugin">MkDocs Img2Fig Plugin</a></b>  - 🥉7 ·  ⭐ 23 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>A MkDocs plugin that converts markdown encoded images into figure elements.</summary>

- [GitHub](https://github.com/stuebersystems/mkdocs-img2fig-plugin) (👨‍💻 2 · 🔀 6 · 📋 3 - 66% open · ⏱️ 14.07.2020)
- [PyPi](https://pypi.org/project/mkdocs-img2fig-plugin) (📥 1.6K / month):
	```
	pip install mkdocs-img2fig-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - img2fig
   ```
</details>
<details><summary><b><a href="https://github.com/Evidlo/markdown_captions">markdown-captions</a></b>  - 🥉7 ·  ⭐ 12 · 💤 · <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1459/PNG/32/2799201-jigsaw-processing_99781.png" style="display:inline;" width="13" height="13"></code><br>Python-Markdown plugin for image captions.</summary>

- [GitHub](https://github.com/Evidlo/markdown_captions) (👨‍💻 2 · 🔀 5 · 📦 200 · 📋 8 - 12% open · ⏱️ 24.05.2023)
- [PyPi](https://pypi.org/project/markdown-captions):
	```
	pip install markdown-captions
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#markdown_extensions):
   ```yaml
   markdown_extensions:
     - markdown_captions
   ```
</details>
<details><summary><b><a href="https://github.com/kuri65536/mkdocs-wavedrom-plugin">markdownwavedrom</a></b>  - 🥉7 ·  ⭐ 10 · 💤 · <code><a href="http://bit.ly/3postzC">MPL-2.0</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>A MkDocs plugin for support wavedrom charts in markdown file.</summary>

- [GitHub](https://github.com/kuri65536/mkdocs-wavedrom-plugin) (🔀 3 · 📦 16 · 📋 3 - 33% open · ⏱️ 02.05.2025)
- [PyPi](https://pypi.org/project/mkdocs-wavedrom-plugin):
	```
	pip install mkdocs-wavedrom-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - markdownwavedrom
   ```
</details>
<details><summary><b><a href="https://github.com/mbarkhau/markdown-svgbob">svgbob extension for Python Markdown</a></b>  - 🥉6 ·  ⭐ 8 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1459/PNG/32/2799201-jigsaw-processing_99781.png" style="display:inline;" width="13" height="13"></code><br>svgbob extension for Python Markdown.</summary>

- [GitHub](https://github.com/mbarkhau/markdown-svgbob) (👨‍💻 2 · 🔀 2 · 📦 10 · 📋 3 - 66% open · ⏱️ 21.06.2024)
- [PyPi](https://pypi.org/project/markdown-svgbob):
	```
	pip install markdown-svgbob
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#markdown_extensions):
   ```yaml
   markdown_extensions:
     - markdown_svgbob
   ```
</details>
<details><summary><b><a href="https://github.com/Rj40x40/mkdocs-import-statement-plugin">import-statement</a></b>  - 🥉5 ·  ⭐ 2 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/Rj40x40/mkdocs-import-statement-plugin) (📦 4 · ⏱️ 06.02.2023)
- [PyPi](https://pypi.org/project/mkdocs-import-statement-plugin) (📥 160 / month):
	```
	pip install mkdocs-import-statement-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - import-statement
   ```
</details>
<details><summary><b><a href="https://github.com/fmaida/pico8-mkdocs-plugin">pico-8</a></b>  - 🥉5 ·  ⭐ 2 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>A MKDocs plugin that allows to embed a Pico-8 web player in a page.</summary>

- [GitHub](https://github.com/fmaida/pico8-mkdocs-plugin) (📦 3 · ⏱️ 17.03.2019)
- [PyPi](https://pypi.org/project/pico8-mkdocs-plugin) (📥 45 / month):
	```
	pip install pico8-mkdocs-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - pico-8
   ```
</details>
<details><summary><b><a href="https://github.com/funk1d/markdown-figcap">markdown-figcap</a></b>  - 🥉5 ·  ⭐ 1 · 💤 · <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1459/PNG/32/2799201-jigsaw-processing_99781.png" style="display:inline;" width="13" height="13"></code><br>Extension for Python-Markdown to handle figure and figcaption.</summary>

- [GitHub](https://github.com/funk1d/markdown-figcap) (📦 7 · ⏱️ 09.03.2019)
- [PyPi](https://pypi.org/project/markdown-figcap) (📥 77 / month):
	```
	pip install markdown-figcap
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#markdown_extensions):
   ```yaml
   markdown_extensions:
     - markdown_figcap
   ```
</details>
<details><summary><b><a href="https://github.com/rajguru7/mkdocs-plugin-inline-svg-mod">inline-svg</a></b>  - 🥉5 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/rajguru7/mkdocs-plugin-inline-svg-mod) (👨‍💻 5 · 🔀 1 · 📦 7 · ⏱️ 12.01.2024)
- [PyPi](https://pypi.org/project/mkdocs-plugin-inline-svg-mod) (📥 610 / month):
	```
	pip install mkdocs-plugin-inline-svg-mod
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - inline-svg
   ```
</details>
<details><summary><b><a href="https://github.com/mbarkhau/markdown-aafigure">Markdown aafigure</a></b>  - 🥉4 ·  ⭐ 6 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1459/PNG/32/2799201-jigsaw-processing_99781.png" style="display:inline;" width="13" height="13"></code><br>aafigure extension for Python Markdown.</summary>

- [GitHub](https://github.com/mbarkhau/markdown-aafigure) (👨‍💻 2 · 📋 3 - 33% open · ⏱️ 04.05.2024)
- [PyPi](https://pypi.org/project/markdown-aafigure) (📥 140 / month):
	```
	pip install markdown-aafigure
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#markdown_extensions):
   ```yaml
   markdown_extensions:
     - markdown_aafigure
   ```
</details>
<details><summary><b><a href="https://github.com/normanlorrain/mkdocs-thumbnails">thumbnails</a></b>  - 🥉4 ·  ⭐ 4 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>MkDocs plugin for thumbnail images generated automatically.</summary>

- [GitHub](https://github.com/normanlorrain/mkdocs-thumbnails) (📋 2 - 50% open · ⏱️ 05.06.2023)
- [PyPi](https://pypi.org/project/mkdocs-thumbnails):
	```
	pip install mkdocs-thumbnails
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - thumbnails
   ```
</details>
<details><summary><b><a href="https://github.com/unverbuggt/mkdocs-familytree-example">Family tree example</a></b>  - 🥉4 ·  ⭐ 2 · 💤 · <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code><br>An interactive family tree visualization using d3-dag.</summary>

- [GitHub](https://github.com/unverbuggt/mkdocs-familytree-example) (👨‍💻 6 · 🔀 1 · ⏱️ 04.08.2023)
</details>
<details><summary><b><a href="https://gitlab.com/rod2ik/mkdocs-graphviz">MkDocs Graphviz</a></b>  - 🥉3 ·  ⭐ 6 · 💤 · <code>❗Unlicensed</code> · <code><img src="https://cdn.icon-icons.com/icons2/1459/PNG/32/2799201-jigsaw-processing_99781.png" style="display:inline;" width="13" height="13"></code><br>A mkdocs Extension that automatically renders Graphviz images, in SVG or PNG format, within your markdown file.</summary>

- [PyPi](https://pypi.org/project/mkdocs-graphviz):
	```
	pip install mkdocs-graphviz
	```
- [GitLab](https://gitlab.com/rod2ik/mkdocs-graphviz) (🔀 1 · 📋 11 - 54% open · ⏱️ 03.05.2021)
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#markdown_extensions):
   ```yaml
   markdown_extensions:
     - mkdocs_graphviz
   ```
</details>
<details><summary><b><a href="https://github.com/fcannizzaro/mkdocs-sequence-js-plugin">sequence-js</a></b>  - 🥉3 ·  ⭐ 5 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>MkDocs plugin to render sequence.js blocks.</summary>

- [GitHub](https://github.com/fcannizzaro/mkdocs-sequence-js-plugin) (🔀 2 · 📋 3 - 33% open · ⏱️ 28.02.2020)
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - sequence-js
   ```
</details>
<details><summary><b><a href="https://github.com/ASypula/mkdocs-image-formatter-plugin">image-formatter-plugin</a></b>  - 🥉3 ·  ⭐ 4 · 💤 · <code>❗Unlicensed</code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/ASypula/mkdocs-image-formatter-plugin) (👨‍💻 7 · 📦 2 · ⏱️ 06.12.2023)
- [PyPi](https://pypi.org/project/mkdocs-image-formatter-plugin) (📥 110 / month):
	```
	pip install mkdocs-image-formatter-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - image-formatter
   ```
</details>
<details><summary><b><a href="https://eskool.gitlab.io/mkhack3rs/">MkHack3rs</a></b>  - 🥉2 ·  ⭐ 4 · 💤 · <code>❗Unlicensed</code> · <code><img src="https://cdn.icon-icons.com/icons2/1448/PNG/32/42498factory_99134.png" style="display:inline;" width="13" height="13"></code><br>Hacks & Integrations for Mkdocs / Material Theme.</summary>

- [GitLab](https://gitlab.com/eskool/mkhack3rs) (🔀 1 · ⏱️ 01.05.2021)
</details>
<br>

## 🤖 Code execution, variables & templating

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://github.com/oprypin/mkdocs-gen-files">gen-files</a></b>  - 🥇24 ·  ⭐ 140 · 📈 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>MkDocs plugin to programmatically generate documentation pages during the build.</summary>

- [GitHub](https://github.com/oprypin/mkdocs-gen-files) (👨‍💻 6 · 🔀 12 · 📦 4.4K · 📋 30 - 30% open · ⏱️ 17.04.2026)
- [PyPi](https://pypi.org/project/mkdocs-gen-files) (📥 1.3M / month):
	```
	pip install mkdocs-gen-files
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - gen-files
   ```
</details>
<details><summary><b><a href="https://github.com/fralau/mkdocs-macros-plugin">macros</a></b>  - 🥇22 ·  ⭐ 410 · 📉 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Create richer and more beautiful pages in MkDocs, by using variables and calls to macros in the markdown code.</summary>

- [GitHub](https://github.com/fralau/mkdocs-macros-plugin) (👨‍💻 36 · 🔀 52 · 📦 6.9K · 📋 150 - 2% open · ⏱️ 03.05.2026)
- [PyPi](https://pypi.org/project/mkdocs-macros-plugin):
	```
	pip install mkdocs-macros-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - macros
   ```
</details>
<details><summary><b><a href="https://github.com/pawamoy/markdown-exec">markdown-exec</a></b>  - 🥇22 ·  ⭐ 170 · <code><a href="http://bit.ly/3hkKRql">ISC</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Utilities to execute code blocks in Markdown files.</summary>

- [GitHub](https://github.com/pawamoy/markdown-exec) (👨‍💻 6 · 🔀 15 · 📦 820 · 📋 68 - 23% open · ⏱️ 10.02.2026)
- [PyPi](https://pypi.org/project/markdown-exec) (📥 960K / month):
	```
	pip install markdown-exec
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - markdown-exec
   ```
</details>
<details><summary><b><a href="https://github.com/danielfrg/mkdocs-jupyter">mkdocs-jupyter</a></b>  - 🥈21 ·  ⭐ 500 · <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Use Jupyter Notebook in mkdocs.</summary>

- [GitHub](https://github.com/danielfrg/mkdocs-jupyter) (👨‍💻 39 · 🔀 65 · 📦 5.1K · 📋 160 - 29% open · ⏱️ 17.04.2026)
- [PyPi](https://pypi.org/project/mkdocs-jupyter):
	```
	pip install mkdocs-jupyter
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - mkdocs-jupyter
   ```
</details>
<details><summary><b><a href="https://github.com/rosscdh/mkdocs-markdownextradata-plugin">markdownextradata</a></b>  - 🥈20 ·  ⭐ 90 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>A MkDocs plugin that injects the mkdocs.yml extra variables into the markdown template.</summary>

- [GitHub](https://github.com/rosscdh/mkdocs-markdownextradata-plugin) (👨‍💻 12 · 🔀 17 · 📦 1.6K · 📋 36 - 16% open · ⏱️ 22.08.2024)
- [PyPi](https://pypi.org/project/mkdocs-markdownextradata-plugin) (📥 110K / month):
	```
	pip install mkdocs-markdownextradata-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - markdownextradata
   ```
</details>
<details><summary><b><a href="https://github.com/greenape/mknotebooks">mknotebooks</a></b>  - 🥈16 ·  ⭐ 140 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>A plugin for mkdocs to help you include Jupyter notebooks in your projects.</summary>

- [GitHub](https://github.com/greenape/mknotebooks) (👨‍💻 14 · 🔀 17 · 📦 790 · 📋 41 - 36% open · ⏱️ 11.08.2023)
- [PyPi](https://pypi.org/project/mknotebooks):
	```
	pip install mknotebooks
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - mknotebooks
   ```
</details>
<details><summary><b><a href="https://github.com/marimo-team/mkdocs-marimo">mkdocs-marimo</a></b>  - 🥈16 ·  ⭐ 110 · <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>mkdocs plugin for reactive and interactive docs with marimo.</summary>

- [GitHub](https://github.com/marimo-team/mkdocs-marimo) (👨‍💻 7 · 🔀 6 · 📦 12 · 📋 27 - 55% open · ⏱️ 13.04.2026)
- [PyPi](https://pypi.org/project/mkdocs-marimo) (📥 14K / month):
	```
	pip install mkdocs-marimo
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - marimo
   ```
</details>
<details><summary><b><a href="https://github.com/markmap/mkdocs_markmap">mkdocs-markmap</a></b>  - 🥈15 ·  ⭐ 74 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>MkDocs plugin and extension to create mindmaps from markdown using markmap.</summary>

- [GitHub](https://github.com/markmap/mkdocs_markmap) (👨‍💻 3 · 🔀 7 · 📥 510 · 📋 34 - 11% open · ⏱️ 11.02.2025)
- [PyPi](https://pypi.org/project/mkdocs-markmap) (📥 2.1K / month):
	```
	pip install mkdocs-markmap
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - markmap
   ```
</details>
<details><summary><b><a href="https://github.com/six-two/mkdocs-placeholder-plugin">placeholder</a></b>  - 🥈15 ·  ⭐ 21 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Add placeholders to your MkDocs pages.</summary>

- [GitHub](https://github.com/six-two/mkdocs-placeholder-plugin) (👨‍💻 3 · 🔀 4 · 📦 20 · ⏱️ 31.05.2026)
- [PyPi](https://pypi.org/project/mkdocs-placeholder-plugin) (📥 15K / month):
	```
	pip install mkdocs-placeholder-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - placeholder
   ```
</details>
<details><summary><b><a href="https://github.com/termynal/termynal.py">Termynal</a></b>  - 🥉11 ·  ⭐ 150 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Python markdown terminal. Built for mkdocs.</summary>

- [GitHub](https://github.com/termynal/termynal.py) (👨‍💻 7 · 🔀 11 · 📋 19 - 42% open · ⏱️ 16.03.2026)
- [PyPi](https://pypi.org/project/termynal) (📥 33K / month):
	```
	pip install termynal
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - termynal
   ```
</details>
<details><summary><b><a href="https://github.com/joapuiib/mkdocs-data-plugin">mkdocs-data-plugin</a></b>  - 🥉11 ·  ⭐ 4 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Mkdocs plugin that allows reading data from markup files and use it in your Markdown pages.</summary>

- [GitHub](https://github.com/joapuiib/mkdocs-data-plugin) (📦 5 · ⏱️ 25.03.2026)
- [PyPi](https://pypi.org/project/mkdocs-data-plugin) (📥 1.2K / month):
	```
	pip install mkdocs-data-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - data
   ```
</details>
<details><summary><b><a href="https://github.com/tanbro/mkdocs-nbconvert">nbconvert</a></b>  - 🥉9 ·  ⭐ 13 · <code><a href="http://bit.ly/3rqEWVr">BSD-2</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>A MkDocs plug-in provides a source parser for *.ipynb files.</summary>

- [GitHub](https://github.com/tanbro/mkdocs-nbconvert) (👨‍💻 5 · 📦 11 · ⏱️ 10.10.2025)
- [PyPi](https://pypi.org/project/mkdocs-nbconvert) (📥 2.4K / month):
	```
	pip install mkdocs-nbconvert
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - nbconvert
   ```
</details>
<details><summary><b><a href="https://github.com/NickCrews/mkdocs-jupyterlite">mkdocs-jupyterlite</a></b>  - 🥉8 ·  ⭐ 25 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>A MkDocs plugin for embedding interactive jupyter notebooks in your docs via jupyterlite.</summary>

- [GitHub](https://github.com/NickCrews/mkdocs-jupyterlite) (👨‍💻 3 · 📋 3 - 33% open · ⏱️ 18.12.2025)
- [PyPi](https://pypi.org/project/mkdocs-jupyterlite) (📥 2.3K / month):
	```
	pip install mkdocs-jupyterlite
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - jupyterlite
   ```
</details>
<details><summary><b><a href="https://github.com/timmeinerzhagen/mkdocs-meta-manager">meta-manager</a></b>  - 🥉8 ·  ⭐ 6 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>MkDocs plugin for managing meta tags across folders and files.</summary>

- [GitHub](https://github.com/timmeinerzhagen/mkdocs-meta-manager) (👨‍💻 3 · 🔀 1 · 📦 20 · 📋 4 - 25% open · ⏱️ 20.01.2025)
- [PyPi](https://pypi.org/project/mkdocs-meta-manager):
	```
	pip install mkdocs-meta-manager
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - meta-manager
   ```
</details>
<details><summary><b><a href="https://github.com/rahult/mkdocs-user-defined-values">user-defined-values</a></b>  - 🥉8 ·  ⭐ 4 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>MkDocs User Defined Values.</summary>

- [GitHub](https://github.com/rahult/mkdocs-user-defined-values) (👨‍💻 3 · 🔀 3 · 📥 19 · 📦 15 · 📋 2 - 50% open · ⏱️ 10.07.2022)
- [PyPi](https://pypi.org/project/mkdocs-user-defined-values):
	```
	pip install mkdocs-user-defined-values
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - user-defined-values
   ```
</details>
<details><summary><b><a href="https://github.com/entangled/mkdocs-plugin">Entangled</a></b>  - 🥉8 ·  ⭐ 3 · <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>An MkDocs plugin that lets you do Literate Programming through Entangled.</summary>

- [GitHub](https://github.com/entangled/mkdocs-plugin) (🔀 1 · 📦 14 · ⏱️ 20.11.2025)
- [PyPi](https://pypi.org/project/mkdocs-entangled-plugin):
	```
	pip install mkdocs-entangled-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - entangled
   ```
</details>
<details><summary><b><a href="https://github.com/daizutabi/pheasant">pheasant</a></b>  - 🥉7 ·  ⭐ 16 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Documentation tool for Markdown conversion by Jupyter client.</summary>

- [GitHub](https://github.com/daizutabi/pheasant) (👨‍💻 4 · 🔀 8 · ⏱️ 22.03.2025)
- [PyPi](https://pypi.org/project/pheasant):
	```
	pip install pheasant
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - pheasant
   ```
</details>
<details><summary><b><a href="https://github.com/stadiamaps/mkjsfiddle">mkjsfiddle</a></b>  - 🥉7 ·  ⭐ 5 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>An MkDocs plugin that lets you edit code fences in JSFiddle.</summary>

- [GitHub](https://github.com/stadiamaps/mkjsfiddle) (📦 3 · ⏱️ 07.06.2023)
- [PyPi](https://pypi.org/project/mkjsfiddle):
	```
	pip install mkjsfiddle
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - jsfiddle
   ```
</details>
<details><summary><b><a href="https://github.com/byrnereese/mkdocs-markdown-filter">markdown-filter</a></b>  - 🥉6 ·  ⭐ 5 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Adds a markdown template filter to the jinja templating environment in mkdocs.</summary>

- [GitHub](https://github.com/byrnereese/mkdocs-markdown-filter) (🔀 2 · 📦 41 · ⏱️ 06.02.2019)
- [PyPi](https://pypi.org/project/mkdocs-markdown-filter):
	```
	pip install mkdocs-markdown-filter
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - markdown-filter
   ```
</details>
<details><summary><b><a href="https://github.com/rkoe/mkdocs-jinja2sandbox">jinja2sandbox</a></b>  - 🥉4 ·  ⭐ 5 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>A MkDocs plugin that enables the Jinja2-sandbox.</summary>

- [GitHub](https://github.com/rkoe/mkdocs-jinja2sandbox) (⏱️ 20.03.2019)
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - jinja2sandbox
   ```
</details>
<details><summary><b><a href="https://github.com/textileio/mkdocs-codeyaml-plugin">codeyaml</a></b>  - 🥉3 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Allows for more than one yaml config in mkdocs.</summary>

- [GitHub](https://github.com/textileio/mkdocs-codeyaml-plugin) (📦 2 · ⏱️ 30.04.2019)
- [PyPi](https://pypi.org/project/mkdocs-codeyaml-plugin):
	```
	pip install mkdocs-codeyaml-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - codeyaml
   ```
</details>
<details><summary><b><a href="https://github.com/rymurr/mkdocs-protobuf">mkdocs_protobuf</a></b>  - 🥉2 ·  ⭐ 2 · 💤 · <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Mkdocs plugin to render protobuf messages.</summary>

- [GitHub](https://github.com/rymurr/mkdocs-protobuf) (👨‍💻 2 · 🔀 1 · ⏱️ 30.03.2022)
- [PyPi](https://pypi.org/project/mkdocs-protobuf):
	```
	pip install mkdocs-protobuf
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - mkdocs_protobuf
   ```
</details>
<br>

## 🌲 Git repos & info

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://github.com/timvink/mkdocs-git-revision-date-localized-plugin">git-revision-date-localized</a></b>  - 🥇30 ·  ⭐ 270 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>MkDocs plugin to add a last updated date to your site pages.</summary>

- [GitHub](https://github.com/timvink/mkdocs-git-revision-date-localized-plugin) (👨‍💻 43 · 🔀 54 · 📦 12K · ⏱️ 10.06.2026)
- [PyPi](https://pypi.org/project/mkdocs-git-revision-date-localized-plugin) (📥 1.7M / month):
	```
	pip install mkdocs-git-revision-date-localized-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - git-revision-date-localized
   ```
</details>
<details><summary><b><a href="https://github.com/timvink/mkdocs-git-authors-plugin">git-authors</a></b>  - 🥇23 ·  ⭐ 120 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>MkDocs plugin to display git authors of a page.</summary>

- [GitHub](https://github.com/timvink/mkdocs-git-authors-plugin) (👨‍💻 17 · 🔀 25 · 📦 1.9K · 📋 67 - 14% open · ⏱️ 10.06.2025)
- [PyPi](https://pypi.org/project/mkdocs-git-authors-plugin) (📥 360K / month):
	```
	pip install mkdocs-git-authors-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - git-authors
   ```
</details>
<details><summary><b><a href="https://github.com/jaywhj/mkdocs-document-dates">document-dates</a></b>  - 🥇23 ·  ⭐ 31 · 📈 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>A new generation MkDocs plugin for displaying exact creation date, last update date, authors, email of documents.</summary>

- [GitHub](https://github.com/jaywhj/mkdocs-document-dates) (👨‍💻 4 · 🔀 5 · 📦 55 · ⏱️ 05.06.2026)
- [PyPi](https://pypi.org/project/mkdocs-document-dates) (📥 18K / month):
	```
	pip install mkdocs-document-dates
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - document-dates
   ```
</details>
<details><summary><b><a href="https://github.com/ojacques/mkdocs-git-committers-plugin-2">git-committers-2</a></b>  - 🥈21 ·  ⭐ 69 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>An MkDocs plugin to create a list of contributors on the page.</summary>

- [GitHub](https://github.com/ojacques/mkdocs-git-committers-plugin-2) (👨‍💻 19 · 🔀 26 · 📦 1.6K · 📋 51 - 27% open · ⏱️ 05.06.2025)
- [PyPi](https://pypi.org/project/mkdocs-git-committers-plugin-2) (📥 150K / month):
	```
	pip install mkdocs-git-committers-plugin-2
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - git-committers
   ```
</details>
<details><summary><b><a href="https://github.com/zhaoterryy/mkdocs-git-revision-date-plugin">git-revision-date</a></b>  - 🥈20 ·  ⭐ 61 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>MkDocs plugin for setting revision date from git per markdown file.</summary>

- [GitHub](https://github.com/zhaoterryy/mkdocs-git-revision-date-plugin) (👨‍💻 7 · 🔀 9 · 📦 3K · 📋 14 - 35% open · ⏱️ 08.03.2022)
- [PyPi](https://pypi.org/project/mkdocs-git-revision-date-plugin) (📥 130K / month):
	```
	pip install mkdocs-git-revision-date-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - git-revision-date
   ```
</details>
<details><summary><b><a href="https://github.com/byrnereese/mkdocs-git-committers-plugin">git-committers</a></b>  - 🥉15 ·  ⭐ 46 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>A mkdocs plugin for displaying the last commit and a list of a files contributors.</summary>

- [GitHub](https://github.com/byrnereese/mkdocs-git-committers-plugin) (👨‍💻 7 · 🔀 6 · 📦 350 · 📋 9 - 88% open · ⏱️ 12.12.2024)
- [PyPi](https://pypi.org/project/mkdocs-git-committers-plugin) (📥 16K / month):
	```
	pip install mkdocs-git-committers-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - git-committers
   ```
</details>
<details><summary><b><a href="https://github.com/tombreit/mkdocs-git-latest-changes-plugin">mkdocs-git-latest-changes-plugin</a></b>  - 🥉13 ·  ⭐ 5 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>MkDocs plugin that allows you to display a list of recently modified pages from the Git log.</summary>

- [GitHub](https://github.com/tombreit/mkdocs-git-latest-changes-plugin) (👨‍💻 4 · 🔀 3 · 📦 8 · 📋 19 - 15% open · ⏱️ 05.12.2025)
- [PyPi](https://pypi.org/project/mkdocs-git-latest-changes-plugin) (📥 24K / month):
	```
	pip install mkdocs-git-latest-changes-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - git-latest-changes
   ```
</details>
<details><summary><b><a href="https://github.com/jaywhj/mkdocs-recently-updated-docs">recently-updated</a></b>  - 🥉10 ·  ⭐ 10 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Display a list of recently updated documents anywhere on your MkDocs site with a single line of code.</summary>

- [GitHub](https://github.com/jaywhj/mkdocs-recently-updated-docs) (📋 2 - 50% open · ⏱️ 13.04.2026)
- [PyPi](https://pypi.org/project/mkdocs-recently-updated-docs) (📥 320 / month):
	```
	pip install mkdocs-recently-updated-docs
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - recently-updated
   ```
</details>
<details><summary><b><a href="https://github.com/Python-Markdown/github-links">Github-Links</a></b>  - 🥉9 ·  ⭐ 15 · <code>❗Unlicensed</code> · <code><img src="https://cdn.icon-icons.com/icons2/1459/PNG/32/2799201-jigsaw-processing_99781.png" style="display:inline;" width="13" height="13"></code><br>Python-Markdown GitHub Links Extension.</summary>

- [GitHub](https://github.com/Python-Markdown/github-links) (👨‍💻 5 · 🔀 10 · ⏱️ 04.09.2025)
- [PyPi](https://pypi.org/project/mdx-gh-links) (📥 23K / month):
	```
	pip install mdx-gh-links
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#markdown_extensions):
   ```yaml
   markdown_extensions:
     - mdx_gh_links
   ```
</details>
<details><summary><b><a href="https://github.com/effigies/mkdocs-branchcustomization-plugin">branchcustomization</a></b>  - 🥉7 ·  ⭐ 3 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Customize MkDocs options on a per-branch basis.</summary>

- [GitHub](https://github.com/effigies/mkdocs-branchcustomization-plugin) (📦 28 · ⏱️ 17.04.2022)
- [PyPi](https://pypi.org/project/mkdocs-branchcustomization-plugin) (📥 520 / month):
	```
	pip install mkdocs-branchcustomization-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - branchcustomization
   ```
</details>
<details><summary><b><a href="https://github.com/djpugh/mkdocs_github_changelog">Github Releaase Changelog</a></b>  - 🥉6 ·  ⭐ 9 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>mkdocs extension to autogenerate changelog from github releases.</summary>

- [GitHub](https://github.com/djpugh/mkdocs_github_changelog) (👨‍💻 2 · ⏱️ 02.01.2024)
- [PyPi](https://pypi.org/project/mkdocs-github-changelog) (📥 480 / month):
	```
	pip install mkdocs-github-changelog
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - mkdocs_github_changelog
   ```
</details>
<details><summary><b><a href="https://github.com/agarthetiger/mkdocs_latest_release_plugin">git-latest-release</a></b>  - 🥉4 ·  ⭐ 2 · 💤 · <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Plugin for MKDocs to inject the latest release tag from git into markdown.</summary>

- [GitHub](https://github.com/agarthetiger/mkdocs_latest_release_plugin) (👨‍💻 3 · ⏱️ 29.12.2019)
- [PyPi](https://pypi.org/project/mkdocs-latest-release-plugin) (📥 620 / month):
	```
	pip install mkdocs-latest-release-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - git-latest-release
   ```
</details>
<br>

## 🌈 HTML processing & CSS styling

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://github.com/byrnereese/mkdocs-minify-plugin">minify</a></b>  - 🥇24 ·  ⭐ 190 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>A mkdocs plugin to minify the HTML of a page before it is written to disk.</summary>

- [GitHub](https://github.com/byrnereese/mkdocs-minify-plugin) (👨‍💻 14 · 🔀 31 · 📦 12K · 📋 18 - 27% open · ⏱️ 29.01.2024)
- [PyPi](https://pypi.org/project/mkdocs-minify-plugin) (📥 1M / month):
	```
	pip install mkdocs-minify-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - minify
   ```
</details>
<details><summary><b><a href="https://github.com/monosans/mkdocs-minify-html-plugin">minify-html</a></b>  - 🥇20 ·  ⭐ 11 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>MkDocs plugin for minification using minify-html, an extremely fast and smart HTML + JS + CSS minifier.</summary>

- [GitHub](https://github.com/monosans/mkdocs-minify-html-plugin) (👨‍💻 4 · 🔀 2 · 📦 100 · ⏱️ 11.06.2026)
- [PyPi](https://pypi.org/project/mkdocs-minify-html-plugin) (📥 28K / month):
	```
	pip install mkdocs-minify-html-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - minify_html
   ```
</details>
<details><summary><b><a href="https://github.com/timvink/mkdocs-enumerate-headings-plugin">enumerate-headings</a></b>  - 🥈15 ·  ⭐ 46 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>MkDocs Plugin to enumerate the headings across site pages.</summary>

- [GitHub](https://github.com/timvink/mkdocs-enumerate-headings-plugin) (👨‍💻 6 · 🔀 14 · 📦 390 · 📋 33 - 12% open · ⏱️ 26.03.2026)
- [PyPi](https://pypi.org/project/mkdocs-enumerate-headings-plugin):
	```
	pip install mkdocs-enumerate-headings-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - enumerate-headings
   ```
</details>
<details><summary><b><a href="https://github.com/mkdocs-publisher/mkdocs-publisher">Publisher for MkDocs - social</a></b>  - 🥈13 ·  ⭐ 130 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Social media sharing helper.</summary>

- [GitHub](https://github.com/mkdocs-publisher/mkdocs-publisher) (👨‍💻 4 · 🔀 11 · 📥 140 · 📦 99 · 📋 31 - 25% open · ⏱️ 26.11.2025)
- [PyPi](https://pypi.org/project/mkdocs-publisher):
	```
	pip install mkdocs-publisher
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - pub-social
   ```
</details>
<details><summary><b><a href="https://github.com/mkdocs-publisher/mkdocs-publisher">Publisher for MkDocs - minifier</a></b>  - 🥈13 ·  ⭐ 130 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Size optimization (minification) for HTML, CSS, JS, SVG, PNG and JPEG files.</summary>

- [GitHub](https://github.com/mkdocs-publisher/mkdocs-publisher) (👨‍💻 4 · 🔀 11 · 📥 140 · 📦 99 · 📋 31 - 25% open · ⏱️ 26.11.2025)
- [PyPi](https://pypi.org/project/mkdocs-publisher):
	```
	pip install mkdocs-publisher
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - pub-minifier
   ```
</details>
<details><summary><b><a href="https://github.com/orzih/mkdocs-extra-sass-plugin">mkdocs-extra-sass-plugin</a></b>  - 🥈13 ·  ⭐ 5 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Adds stylesheets to your mkdocs site from Sass/SCSS.</summary>

- [GitHub](https://github.com/orzih/mkdocs-extra-sass-plugin) (🔀 4 · 📦 91 · ⏱️ 13.02.2021)
- [PyPi](https://pypi.org/project/mkdocs-extra-sass-plugin) (📥 11K / month):
	```
	pip install mkdocs-extra-sass-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - extra-sass
   ```
</details>
<details><summary><b><a href="https://github.com/ignorantshr/mkdocs-add-number-plugin">add-number</a></b>  - 🥈12 ·  ⭐ 19 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>MkDocs plugin to automatically number the headings (h1-h6) in each markdown page and the nav.</summary>

- [GitHub](https://github.com/ignorantshr/mkdocs-add-number-plugin) (👨‍💻 3 · 🔀 3 · 📦 53 · 📋 12 - 25% open · ⏱️ 11.06.2020)
- [PyPi](https://pypi.org/project/mkdocs-add-number-plugin) (📥 6.4K / month):
	```
	pip install mkdocs-add-number-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - add-number
   ```
</details>
<details><summary><b><a href="https://github.com/Aetherinox/mkdocs-link-embeds">mkdocs-link-embeds</a></b>  - 🥈12 ·  ⭐ 11 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Mkdocs plugin which displays links in a more elegant way. Links will automatically be populated with an image,..</summary>

- [GitHub](https://github.com/Aetherinox/mkdocs-link-embeds) (🔀 1 · 📥 26 · 📦 11 · ⏱️ 04.05.2025)
- [PyPi](https://pypi.org/project/mkdocs-link-embeds-plugin) (📥 2K / month):
	```
	pip install mkdocs-link-embeds-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - link-embeds
   ```
</details>
<details><summary><b><a href="https://github.com/six-two/mkdocs-toggle-sidebar-plugin">toggle-sidebar</a></b>  - 🥉10 ·  ⭐ 10 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Toggle the navigation and/or TOC sidebars on your MkDocs site.</summary>

- [GitHub](https://github.com/six-two/mkdocs-toggle-sidebar-plugin) (👨‍💻 2 · 🔀 3 · ⏱️ 23.05.2026)
- [PyPi](https://pypi.org/project/mkdocs-toggle-sidebar-plugin) (📥 12K / month):
	```
	pip install mkdocs-toggle-sidebar-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - toggle-sidebar
   ```
</details>
<details><summary><b><a href="https://github.com/raimon49/mkdocs-safe-text-plugin">mkdocs_safe_text</a></b>  - 🥉10 ·  ⭐ 3 · 💤 · <code><a href="http://bit.ly/3rqEWVr">BSD-2</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Plugin for safe text editing with MKDocs.</summary>

- [GitHub](https://github.com/raimon49/mkdocs-safe-text-plugin) (👨‍💻 2 · 📦 10 · ⏱️ 22.07.2024)
- [PyPi](https://pypi.org/project/mkdocs-safe-text-plugin) (📥 750 / month):
	```
	pip install mkdocs-safe-text-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - mkdocs_safe_text
   ```
</details>
<details><summary><b><a href="https://github.com/byrnereese/mkdocs-bootstrap-tables-plugin">bootstrap-tables</a></b>  - 🥉9 ·  ⭐ 13 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>A MkDocs plugin to add bootstrap classes to plan markdown generated tables.</summary>

- [GitHub](https://github.com/byrnereese/mkdocs-bootstrap-tables-plugin) (🔀 2 · 📦 110 · ⏱️ 27.03.2020)
- [PyPi](https://pypi.org/project/mkdocs-bootstrap-tables-plugin) (📥 1.2K / month):
	```
	pip install mkdocs-bootstrap-tables-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - bootstrap-tables
   ```
</details>
<details><summary><b><a href="https://github.com/wilhelmer/mkdocs-add-teaser">mkdocs-add-teaser</a></b>  - 🥉9 ·  ⭐ 4 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>An MkDocs plugin to customize the first paragraph of your pages, and to use it as the pages meta description.</summary>

- [GitHub](https://github.com/wilhelmer/mkdocs-add-teaser) (👨‍💻 3 · 🔀 1 · 📦 8 · ⏱️ 08.11.2022)
- [PyPi](https://pypi.org/project/mkdocs-add-teaser) (📥 270 / month):
	```
	pip install mkdocs-add-teaser
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - mkdocs-add-teaser
   ```
</details>
<details><summary><b><a href="https://github.com/pawamoy/mkdocs-pygments">MkDocs Pygments</a></b>  - 🥉7 ·  ⭐ 8 · <code><a href="http://bit.ly/3hkKRql">ISC</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Highlighting themes for code blocks.</summary>

- [GitHub](https://github.com/pawamoy/mkdocs-pygments) (🔀 2 · 📦 7 · ⏱️ 01.12.2025)
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - pygments
   ```
</details>
<details><summary><b><a href="https://github.com/marcelaodev/mk-append-to-head">mk-append-to-head</a></b>  - 🥉6 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Append some string to a MkDocs pages head.</summary>

- [GitHub](https://github.com/marcelaodev/mk-append-to-head) (⏱️ 18.08.2025)
- [PyPi](https://pypi.org/project/mk-append-to-head) (📥 69 / month):
	```
	pip install mk-append-to-head
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - mk-append-to-head
   ```
</details>
<details><summary><b><a href="https://aiboy996.github.io/mkdocs-ai-summary/">mkdocs-ai-summary</a></b>  - 🥉5 ·  ⭐ 10 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>A mkdocs plugin to generage summary with the help of AI.</summary>

- [GitHub](https://github.com/AIboy996/mkdocs-ai-summary) (📦 4 · 📋 2 - 50% open · ⏱️ 27.12.2024)
- [PyPi](https://pypi.org/project/mkdocs-ai-summary):
	```
	pip install mkdocs-ai-summary
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - ai-summary
   ```
</details>
<details><summary><b><a href="https://github.com/hfagerlund/mkdocs-docstyler-plugin">docstyler</a></b>  - 🥉2 ·  ⭐ 1 · 💤 · <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Plugin to add alternative stylesheets to MkDocs custom themes.</summary>

- [GitHub](https://github.com/hfagerlund/mkdocs-docstyler-plugin) (⏱️ 16.02.2019)
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - docstyler
   ```
</details>
<br>

## 📎 Integrations with other tools

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://github.com/pawamoy/mkdocs-llmstxt">mkdocs-llmstxt</a></b>  - 🥇21 ·  ⭐ 120 · <code><a href="http://bit.ly/3hkKRql">ISC</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>MkDocs plugin to generate an /llms.txt file (https://llmstxt.org/).</summary>

- [GitHub](https://github.com/pawamoy/mkdocs-llmstxt) (👨‍💻 5 · 🔀 12 · 📦 490 · ⏱️ 01.12.2025)
- [PyPi](https://pypi.org/project/mkdocs-llmstxt) (📥 290K / month):
	```
	pip install mkdocs-llmstxt
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - llmstxt
   ```
</details>
<details><summary><b><a href="https://github.com/blueswen/mkdocs-swagger-ui-tag">MkDocs Swagger UI Tag</a></b>  - 🥇21 ·  ⭐ 110 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>A MkDocs plugin supports adding Swagger UI to the page.</summary>

- [GitHub](https://github.com/blueswen/mkdocs-swagger-ui-tag) (👨‍💻 8 · 🔀 15 · 📥 50 · 📦 430 · 📋 33 - 33% open · ⏱️ 22.02.2026)
- [PyPi](https://pypi.org/project/mkdocs-swagger-ui-tag) (📥 230K / month):
	```
	pip install mkdocs-swagger-ui-tag
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - swagger-ui-tag
   ```
</details>
<details><summary><b><a href="https://github.com/pawamoy/mkdocs-coverage">mkdocs-coverage</a></b>  - 🥈17 ·  ⭐ 37 · <code><a href="http://bit.ly/3hkKRql">ISC</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>MkDocs plugin to integrate your coverage HTML report into your site.</summary>

- [GitHub](https://github.com/pawamoy/mkdocs-coverage) (👨‍💻 2 · 🔀 1 · 📦 340 · ⏱️ 01.12.2025)
- [PyPi](https://pypi.org/project/mkdocs-coverage) (📥 78K / month):
	```
	pip install mkdocs-coverage
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - coverage
   ```
</details>
<details><summary><b><a href="https://github.com/pa-decarvalho/mkdocs-asciinema-player">MkDocs asciinema-player</a></b>  - 🥈17 ·  ⭐ 20 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Mkdocs Plugin to include asciinema player in your documentation.</summary>

- [GitHub](https://github.com/pa-decarvalho/mkdocs-asciinema-player) (👨‍💻 6 · 🔀 3 · 📦 20 · 📋 38 - 13% open · ⏱️ 11.05.2026)
- [PyPi](https://pypi.org/project/mkdocs-asciinema-player) (📥 1.4K / month):
	```
	pip install mkdocs-asciinema-player
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - asciinema-player
   ```
</details>
<details><summary><b><a href="https://github.com/mkdocs-publisher/mkdocs-publisher">Publisher for MkDocs - obsidian</a></b>  - 🥈16 ·  ⭐ 130 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Obsidian.md integration including with support for wiki links, callouts, backlinks etc.</summary>

- [GitHub](https://github.com/mkdocs-publisher/mkdocs-publisher) (👨‍💻 4 · 🔀 11 · 📥 140 · 📦 99 · 📋 31 - 25% open · ⏱️ 26.11.2025)
- [PyPi](https://pypi.org/project/mkdocs-publisher) (📥 3.5K / month):
	```
	pip install mkdocs-publisher
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - pub-obsidian
   ```
</details>
<details><summary><b><a href="https://github.com/bharel/mkdocs-render-swagger-plugin">mkdocs-render-swagger-plugin</a></b>  - 🥉14 ·  ⭐ 78 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>A plugin for MKDocs for rendering swagger & openapi schemas using SwaggerUI.</summary>

- [GitHub](https://github.com/bharel/mkdocs-render-swagger-plugin) (👨‍💻 8 · 🔀 14 · 📥 11 · 📋 15 - 20% open · ⏱️ 23.09.2024)
- [PyPi](https://pypi.org/project/mkdocs-render-swagger-plugin) (📥 120K / month):
	```
	pip install mkdocs-render-swagger-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - render_swagger
   ```
</details>
<details><summary><b><a href="https://github.com/leonardocustodio/mkdocs-copy-to-llm">mkdocs-copy-to-llm</a></b>  - 🥉13 ·  ⭐ 16 · 📈 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>A MkDocs plugin that adds a Copy to LLM button to your documentation, making it easy to copy code blocks and entire..</summary>

- [GitHub](https://github.com/leonardocustodio/mkdocs-copy-to-llm) (👨‍💻 4 · 🔀 2 · 📦 5 · 📋 9 - 22% open · ⏱️ 10.03.2026)
- [PyPi](https://pypi.org/project/mkdocs-copy-to-llm) (📥 1.5K / month):
	```
	pip install mkdocs-copy-to-llm
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - copy-to-llm
   ```
</details>
<details><summary><b><a href="https://github.com/foliant-docs/foliantcontrib.mkdocs">MkDocs Backend for Foliant</a></b>  - 🥉9 ·  ⭐ 3 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code><br>MkDocs backend for Foliant.</summary>

- [GitHub](https://github.com/foliant-docs/foliantcontrib.mkdocs) (👨‍💻 5 · 🔀 3 · 📦 35 · ⏱️ 12.12.2022)
- [PyPi](https://pypi.org/project/foliantcontrib.mkdocs):
	```
	pip install foliantcontrib.mkdocs
	```
</details>
<details><summary><b><a href="https://github.com/ubaumann/mkdocs-mcp">mkdocs-mcp</a></b>  - 🥉8 ·  ⭐ 9 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>MkDocs Plugin to serve MCP.</summary>

- [GitHub](https://github.com/ubaumann/mkdocs-mcp) (🔀 2 · ⏱️ 20.09.2025)
- [PyPi](https://pypi.org/project/mkdocs-mcp) (📥 150 / month):
	```
	pip install mkdocs-mcp
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - mcp
   ```
</details>
<details><summary><b><a href="https://github.com/djpugh/mkdocs_licenseinfo">MkDocs Dependency License Information</a></b>  - 🥉8 ·  ⭐ 5 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>mkdocs extension to visualise package dependencies license information.</summary>

- [GitHub](https://github.com/djpugh/mkdocs_licenseinfo) (👨‍💻 2 · ⏱️ 29.03.2026)
- [PyPi](https://pypi.org/project/mkdocs-licenseinfo) (📥 280 / month):
	```
	pip install mkdocs-licenseinfo
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - mkdocs_licenseinfo
   ```
</details>
<details><summary><b><a href="https://github.com/inuits/mkdocs-factsheet">factsheet</a></b>  - 🥉6 ·  ⭐ 5 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Generate overviews from YAML descriptions, intended for micro-services and their deployments.</summary>

- [GitHub](https://github.com/inuits/mkdocs-factsheet) (👨‍💻 4 · 🔀 1 · ⏱️ 08.02.2023)
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - factsheet
   ```
</details>
<details><summary><b><a href="https://github.com/allevo/mkdocs-swagger-plugin">swagger</a></b>  - 🥉5 ·  ⭐ 29 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>MkDocs plugin for render swagger into docs.</summary>

- [GitHub](https://github.com/allevo/mkdocs-swagger-plugin) (🔀 6 · 📋 5 - 60% open · ⏱️ 06.10.2019)
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - swagger
   ```
</details>
<details><summary><b><a href="https://github.com/six-two/mkdocs-vercel-pw-plugin">Vercel Password Protection</a></b>  - 🥉5 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Allows you to password protect your site if it is deployed by Vercel, by adding routes to the vercel.json file.</summary>

- [GitHub](https://github.com/six-two/mkdocs-vercel-pw-plugin) (⏱️ 11.11.2024)
- [PyPi](https://pypi.org/project/mkdocs-vercel-pw-plugin) (📥 81 / month):
	```
	pip install mkdocs-vercel-pw-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - vercel_pw
   ```
</details>
<br>

## 🌍 Internationalization & localization

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://github.com/ultrabug/mkdocs-static-i18n">static-i18n</a></b>  - 🥇23 ·  ⭐ 320 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>MkDocs i18n plugin using static translation markdown files.</summary>

- [GitHub](https://github.com/ultrabug/mkdocs-static-i18n) (👨‍💻 14 · 🔀 50 · 📦 2.5K · 📋 160 - 19% open · ⏱️ 02.03.2026)
- [PyPi](https://pypi.org/project/mkdocs-static-i18n) (📥 490K / month):
	```
	pip install mkdocs-static-i18n
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - i18n
   ```
</details>
<details><summary><b><a href="https://github.com/mondeja/mkdocs-mdpo-plugin">mkdocs-mdpo</a></b>  - 🥉11 ·  ⭐ 11 · 💤 · <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Mkdocs translation plugin using PO files.</summary>

- [GitHub](https://github.com/mondeja/mkdocs-mdpo-plugin) (👨‍💻 4 · 🔀 7 · 📥 260 · 📋 37 - 35% open · ⏱️ 10.06.2024)
- [PyPi](https://pypi.org/project/mkdocs-mdpo-plugin) (📥 160 / month):
	```
	pip install mkdocs-mdpo-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - mdpo
   ```
</details>
<details><summary><b><a href="https://pypi.org/project/mkdocs-translations/">Mkdocs translations plugin</a></b>  - 🥉2 · <code>❗Unlicensed</code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Internationalization plugin for mkdocs.</summary>

- [PyPi](https://pypi.org/project/mkdocs-translations) (📥 100 / month):
	```
	pip install mkdocs-translations
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - translations
   ```
</details>
<br>

## 🔗 Links & references

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://github.com/mkdocs/mkdocs-redirects">mkdocs-redirects</a></b>  - 🥇26 ·  ⭐ 240 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Open source plugin for Mkdocs page redirects.</summary>

- [GitHub](https://github.com/mkdocs/mkdocs-redirects) (👨‍💻 18 · 🔀 35 · 📦 7.7K · 📋 42 - 33% open · ⏱️ 19.05.2025)
- [PyPi](https://pypi.org/project/mkdocs-redirects) (📥 1.6M / month):
	```
	pip install mkdocs-redirects
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - redirects
   ```
</details>
<details><summary><b><a href="https://github.com/manuzhang/mkdocs-htmlproofer-plugin">htmlproofer</a></b>  - 🥇20 ·  ⭐ 48 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>A MkDocs plugin that validates URL in rendered html files.</summary>

- [GitHub](https://github.com/manuzhang/mkdocs-htmlproofer-plugin) (👨‍💻 16 · 🔀 18 · 📦 710 · 📋 39 - 10% open · ⏱️ 23.02.2026)
- [PyPi](https://pypi.org/project/mkdocs-htmlproofer-plugin) (📥 75K / month):
	```
	pip install mkdocs-htmlproofer-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - htmlproofer
   ```
</details>
<details><summary><b><a href="https://github.com/mkdocstrings/autorefs">autorefs</a></b>  - 🥇18 ·  ⭐ 84 · <code><a href="http://bit.ly/3hkKRql">ISC</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Automatically link across pages in MkDocs.</summary>

- [GitHub](https://github.com/mkdocstrings/autorefs) (👨‍💻 9 · 🔀 12 · ⏱️ 10.02.2026)
- [PyPi](https://pypi.org/project/mkdocs-autorefs) (📥 6.8M / month):
	```
	pip install mkdocs-autorefs
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - autorefs
   ```
</details>
<details><summary><b><a href="https://github.com/shyamd/mkdocs-bibtex">bibtex</a></b>  - 🥈17 ·  ⭐ 92 · <code><a href="https://tldrlegal.com/search?query=BSD-3-Clause-LBNL">❗️BSD-3-Clause-LBNL</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>A MkDocs plugin for citation management using bibtex.</summary>

- [GitHub](https://github.com/shyamd/mkdocs-bibtex) (👨‍💻 21 · 🔀 30 · 📋 59 - 10% open · ⏱️ 01.11.2025)
- [PyPi](https://pypi.org/project/mkdocs-bibtex) (📥 43K / month):
	```
	pip install mkdocs-bibtex
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - bibtex
   ```
</details>
<details><summary><b><a href="https://github.com/zachhannum/mkdocs-autolinks-plugin">autolinks</a></b>  - 🥈17 ·  ⭐ 90 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>An MkDocs plugin that automagically generates relative links between markdown pages.</summary>

- [GitHub](https://github.com/zachhannum/mkdocs-autolinks-plugin) (👨‍💻 10 · 🔀 18 · 📦 720 · 📋 18 - 50% open · ⏱️ 04.08.2023)
- [PyPi](https://pypi.org/project/mkdocs-autolinks-plugin) (📥 110K / month):
	```
	pip install mkdocs-autolinks-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - autolinks
   ```
</details>
<details><summary><b><a href="https://github.com/EddyLuten/mkdocs-alias-plugin">mkdocs-alias-plugin</a></b>  - 🥈16 ·  ⭐ 16 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>An MkDocs plugin allowing links to your pages using a custom alias.</summary>

- [GitHub](https://github.com/EddyLuten/mkdocs-alias-plugin) (👨‍💻 6 · 🔀 4 · 📦 39 · ⏱️ 14.05.2026)
- [PyPi](https://pypi.org/project/mkdocs-alias-plugin) (📥 2.8K / month):
	```
	pip install mkdocs-alias-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - alias
   ```
</details>
<details><summary><b><a href="https://github.com/timmeinerzhagen/mkdocs-link-marker">link-marker</a></b>  - 🥈16 ·  ⭐ 9 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>MkDocs plugin for marking links e.g. external ones or mails.</summary>

- [GitHub](https://github.com/timmeinerzhagen/mkdocs-link-marker) (👨‍💻 3 · 🔀 2 · 📦 50 · 📋 5 - 40% open · ⏱️ 04.03.2026)
- [PyPi](https://pypi.org/project/mkdocs-link-marker) (📥 710K / month):
	```
	pip install mkdocs-link-marker
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - link-marker
   ```
</details>
<details><summary><b><a href="https://github.com/orbikm/mkdocs-ezlinks-plugin">ezlinks</a></b>  - 🥈15 ·  ⭐ 42 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Plugin for mkdocs which enables easier linking between pages.</summary>

- [GitHub](https://github.com/orbikm/mkdocs-ezlinks-plugin) (🔀 13 · 📥 230 · 📦 170 · 📋 27 - 44% open · ⏱️ 24.01.2022)
- [PyPi](https://pypi.org/project/mkdocs-ezlinks-plugin) (📥 21K / month):
	```
	pip install mkdocs-ezlinks-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - ezlinks
   ```
</details>
<details><summary><b><a href="https://github.com/makerjackie/mkdocs-roamlinks-plugin">roamlinks</a></b>  - 🥈12 ·  ⭐ 55 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>An MkDocs plugin that automagically generates relative links between markdown pages.</summary>

- [GitHub](https://github.com/makerjackie/mkdocs-roamlinks-plugin) (👨‍💻 10 · 🔀 17 · ⏱️ 03.02.2026)
- [PyPi](https://pypi.org/project/mkdocs-roamlinks-plugin) (📥 26K / month):
	```
	pip install mkdocs-roamlinks-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - roamlinks
   ```
</details>
<details><summary><b><a href="https://github.com/JakubAndrysek/mkdocs-open-in-new-tab">mkdocs-open-in-new-tab</a></b>  - 🥈12 ·  ⭐ 44 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>This plugin adds JS to open outgoing links and PDFs in a new tab.</summary>

- [GitHub](https://github.com/JakubAndrysek/mkdocs-open-in-new-tab) (👨‍💻 2 · 🔀 5 · 📦 700 · 📋 9 - 44% open · ⏱️ 18.11.2024)
- [PyPi](https://pypi.org/project/mkdocs-open-in-new-tab):
	```
	pip install mkdocs-open-in-new-tab
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - open-in-new-tab
   ```
</details>
<details><summary><b><a href="https://github.com/OctoPrint/mkdocs-site-urls">mkdocs-site-urls</a></b>  - 🥈12 ·  ⭐ 24 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>A MkDocs plugin that adds support for site-relative `site:` URLs.</summary>

- [GitHub](https://github.com/OctoPrint/mkdocs-site-urls) (👨‍💻 2 · 🔀 4 · ⏱️ 04.03.2026)
- [PyPi](https://pypi.org/project/mkdocs-site-urls) (📥 21K / month):
	```
	pip install mkdocs-site-urls
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - site-urls
   ```
</details>
<details><summary><b><a href="https://github.com/realtimeprojects/mkdocs-ezglossary">ezglossary</a></b>  - 🥈12 ·  ⭐ 17 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Glossary support for mkdocs.</summary>

- [GitHub](https://github.com/realtimeprojects/mkdocs-ezglossary) (👨‍💻 6 · 📋 25 - 8% open · ⏱️ 11.04.2026)
- [PyPi](https://pypi.org/project/mkdocs-ezglossary-plugin) (📥 12K / month):
	```
	pip install mkdocs-ezglossary-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - ezglossary
   ```
</details>
<details><summary><b><a href="https://github.com/wilhelmer/mkdocs-unused-files">unused-files</a></b>  - 🥈12 ·  ⭐ 17 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>An MkDocs plugin to find unused (orphaned) files in your project.</summary>

- [GitHub](https://github.com/wilhelmer/mkdocs-unused-files) (👨‍💻 2 · 🔀 5 · 📦 39 · 📋 12 - 33% open · ⏱️ 17.07.2023)
- [PyPi](https://pypi.org/project/mkdocs-unused-files) (📥 6.8K / month):
	```
	pip install mkdocs-unused-files
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - unused_files
   ```
</details>
<details><summary><b><a href="https://github.com/sander76/mkdocs-abs-rel-plugin">abs-to-rel</a></b>  - 🥉9 ·  ⭐ 5 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>MkDocs plugin for converting absolute links to relative ones.</summary>

- [GitHub](https://github.com/sander76/mkdocs-abs-rel-plugin) (👨‍💻 2 · 🔀 3 · 📦 38 · ⏱️ 03.03.2020)
- [PyPi](https://pypi.org/project/mkdocs-abs-rel-plugin) (📥 2.7K / month):
	```
	pip install mkdocs-abs-rel-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - abs-to-rel
   ```
</details>
<details><summary><b><a href="https://github.com/neurobin/mdx_wikilink_plus">Wikilink Plus</a></b>  - 🥉8 ·  ⭐ 16 · 💤 · <code>❗Unlicensed</code> · <code><img src="https://cdn.icon-icons.com/icons2/1459/PNG/32/2799201-jigsaw-processing_99781.png" style="display:inline;" width="13" height="13"></code><br>A wikilink extension for Python Markdown.</summary>

- [GitHub](https://github.com/neurobin/mdx_wikilink_plus) (👨‍💻 5 · 🔀 5 · ⏱️ 26.07.2022)
- [PyPi](https://pypi.org/project/mdx-wikilink-plus) (📥 13K / month):
	```
	pip install mdx-wikilink-plus
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#markdown_extensions):
   ```yaml
   markdown_extensions:
     - mdx_wikilink_plus
   ```
</details>
<details><summary><b><a href="https://github.com/zachhannum/mkdocs-tooltipster-links-plugin">tooltipster-links</a></b>  - 🥉7 ·  ⭐ 9 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>An MkDocs plugin that adds tooltips to preview the content of page links using tooltipster.</summary>

- [GitHub](https://github.com/zachhannum/mkdocs-tooltipster-links-plugin) (🔀 1 · 📦 31 · ⏱️ 29.07.2020)
- [PyPi](https://pypi.org/project/mkdocs-tooltipster-links-plugin) (📥 82 / month):
	```
	pip install mkdocs-tooltipster-links-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - tooltipster-links
   ```
</details>
<details><summary><b><a href="https://github.com/six-two/mkdocs-backlinks-section-plugin">MkDocs Backlinks Section Plugin</a></b>  - 🥉7 ·  ⭐ 8 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Create a backlink section that lists every page linking to the current page.</summary>

- [GitHub](https://github.com/six-two/mkdocs-backlinks-section-plugin) (👨‍💻 2 · 🔀 1 · ⏱️ 23.05.2026)
- [PyPi](https://pypi.org/project/mkdocs-backlinks-section-plugin) (📥 3.4K / month):
	```
	pip install mkdocs-backlinks-section-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - backlinks_section
   ```
</details>
<details><summary><b><a href="https://github.com/mihaigalos/mkdocs-issues-plugin">mkdocs-issues-plugin</a></b>  - 🥉7 ·  ⭐ 6 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>A plugin for showing the state and labels of issues, PRs and discussions (GitHub or GitLab) in mkdocs generated docs.</summary>

- [GitHub](https://github.com/mihaigalos/mkdocs-issues-plugin) (👨‍💻 3 · 📦 1 · ⏱️ 24.07.2024)
- [PyPi](https://pypi.org/project/mkdocs-issues-plugin) (📥 200 / month):
	```
	pip install mkdocs-issues-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - mkdocs-issues-plugin
   ```
</details>
<details><summary><b><a href="https://github.com/Darrelk/mkdocs-webcontext-plugin">webcontext</a></b>  - 🥉7 ·  ⭐ 1 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Mkdocs plugin for converting absolute paths to webcontext aware paths using the configured webcontext context.</summary>

- [GitHub](https://github.com/Darrelk/mkdocs-webcontext-plugin) (👨‍💻 2 · 🔀 1 · 📥 13 · 📦 6 · ⏱️ 23.05.2025)
- [PyPi](https://pypi.org/project/mkdocs-webcontext-plugin) (📥 310 / month):
	```
	pip install mkdocs-webcontext-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - webcontext
   ```
</details>
<details><summary><b><a href="https://github.com/theskumar/autolink-references-mkdocs-plugin">Autolink References</a></b>  - 🥉6 ·  ⭐ 19 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>mkdocs plugin to provides GitHub like autolink references in Mkdocs.</summary>

- [GitHub](https://github.com/theskumar/autolink-references-mkdocs-plugin) (👨‍💻 3 · 🔀 8 · 📋 4 - 25% open · ⏱️ 28.12.2023)
- [PyPi](https://pypi.org/project/autolink-references-mkdocs-plugin):
	```
	pip install autolink-references-mkdocs-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - autolink_references
   ```
</details>
<details><summary><b><a href="https://github.com/rhshadrach/mkdocs-argref-plugin">ArgRef</a></b>  - 🥉5 ·  ⭐ 3 · 💤 · <code>❗Unlicensed</code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>mkdocs plugin to provides GitHub like autolink references in Mkdocs.</summary>

- [GitHub](https://github.com/rhshadrach/mkdocs-argref-plugin) (👨‍💻 5 · 🔀 1 · ⏱️ 25.08.2024)
- [PyPi](https://pypi.org/project/mkdocs-argref-plugin):
	```
	pip install mkdocs-argref-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - argref
   ```
</details>
<details><summary><b><a href="https://github.com/rkoe/mkdocs-emailprotect">emailprotect</a></b>  - 🥉3 ·  ⭐ 6 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>A MkDocs plugin that tries to obscure email-addresses from address-harvesting spam-bots.</summary>

- [GitHub](https://github.com/rkoe/mkdocs-emailprotect) (⏱️ 21.01.2020)
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - emailprotect
   ```
</details>
<details><summary><b><a href="https://github.com/cmitu/mkdocs-altlink-plugin">alternate-link</a></b>  - 🥉3 ·  ⭐ 4 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>An MkDocs plugin that simplifies internal links creation.</summary>

- [GitHub](https://github.com/cmitu/mkdocs-altlink-plugin) (👨‍💻 3 · 🔀 2 · ⏱️ 14.02.2021)
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - alternate-link
   ```
</details>
<details><summary><b><a href="https://gitlab.com/frederic-zinelli/mkdocs-addresses">Mkdocs-Addresses</a></b>  - 🥉2 · 💤 · <code>❗Unlicensed</code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Mkdocs plugin, building automatically the appropriate relative paths (to images, links, anchors, ...) using..</summary>

- [PyPi](https://pypi.org/project/mkdocs-addresses):
	```
	pip install mkdocs-addresses
	```
- [GitLab](https://gitlab.com/frederic-zinelli/mkdocs-addresses) (🔀 0 · ⏱️ 13.07.2023)
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - mkdocs-addresses
   ```
</details>
<br>

## 🧩 Markdown extensions

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://github.com/facelessuser/pymdown-extensions">PyMdown Extensions</a></b>  - 🥇35 ·  ⭐ 1.1K · <code>❗Unlicensed</code> · <code><img src="https://cdn.icon-icons.com/icons2/1459/PNG/32/2799201-jigsaw-processing_99781.png" style="display:inline;" width="13" height="13"></code><br>Extensions for Python Markdown.</summary>

- [GitHub](https://github.com/facelessuser/pymdown-extensions) (👨‍💻 56 · 🔀 270 · 📦 60K · 📋 430 - 3% open · ⏱️ 26.05.2026)
- [PyPi](https://pypi.org/project/pymdown-extensions) (📥 25M / month):
	```
	pip install pymdown-extensions
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#markdown_extensions):
   ```yaml
   markdown_extensions:
     - pymdownx.arithmatex
     - pymdownx.b64
     - pymdownx.betterem
     - pymdownx.blocks.admonition
     - pymdownx.blocks.definition
     - pymdownx.blocks.details
     - pymdownx.blocks.html
     - pymdownx.blocks.tab
     - pymdownx.caret
     - pymdownx.critic
     - pymdownx.details
     - pymdownx.emoji
     - pymdownx.escapeall
     - pymdownx.extra
     - pymdownx.highlight
     - pymdownx.inlinehilite
     - pymdownx.keys
     - pymdownx.magiclink
     - pymdownx.mark
     - pymdownx.pathconverter
     - pymdownx.progressbar
     - pymdownx.saneheaders
     - pymdownx.smartsymbols
     - pymdownx.snippets
     - pymdownx.striphtml
     - pymdownx.superfences
     - pymdownx.tabbed
     - pymdownx.tasklist
     - pymdownx.tilde
   ```
</details>
<details><summary><b><a href="https://github.com/sondregronas/mkdocs-callouts">mkdocs-callouts</a></b>  - 🥇21 ·  ⭐ 50 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>A simple MkDocs plugin that converts Obsidian callout blocks to mkdocs supported Admonitions.</summary>

- [GitHub](https://github.com/sondregronas/mkdocs-callouts) (👨‍💻 3 · 🔀 4 · 📦 1.4K · ⏱️ 13.05.2026)
- [PyPi](https://pypi.org/project/mkdocs-callouts) (📥 67K / month):
	```
	pip install mkdocs-callouts
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - callouts
   ```
</details>
<details><summary><b><a href="https://github.com/oprypin/markdown-callouts">markdown-callouts</a></b>  - 🥇18 ·  ⭐ 45 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1459/PNG/32/2799201-jigsaw-processing_99781.png" style="display:inline;" width="13" height="13"></code><br>Markdown extension: a classier syntax for admonitions.</summary>

- [GitHub](https://github.com/oprypin/markdown-callouts) (👨‍💻 2 · 🔀 14 · 📦 700 · 📋 13 - 38% open · ⏱️ 17.04.2026)
- [PyPi](https://pypi.org/project/markdown-callouts) (📥 130K / month):
	```
	pip install markdown-callouts
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#markdown_extensions):
   ```yaml
   markdown_extensions:
     - callouts
     - github-callouts
   ```
</details>
<details><summary><b><a href="https://github.com/mitya57/python-markdown-math">Math extension</a></b>  - 🥈16 ·  ⭐ 130 · 💤 · <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1459/PNG/32/2799201-jigsaw-processing_99781.png" style="display:inline;" width="13" height="13"></code><br>Math extension for Python-Markdown.</summary>

- [GitHub](https://github.com/mitya57/python-markdown-math) (👨‍💻 8 · 🔀 25 · 📦 4K · 📋 24 - 8% open · ⏱️ 10.04.2025)
- [PyPi](https://pypi.org/project/python-markdown-math):
	```
	pip install python-markdown-math
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#markdown_extensions):
   ```yaml
   markdown_extensions:
     - mdx_math
   ```
</details>
<details><summary><b><a href="https://github.com/radude/mdx_truly_sane_lists">Mdx Truly Sane Lists</a></b>  - 🥈15 ·  ⭐ 100 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1459/PNG/32/2799201-jigsaw-processing_99781.png" style="display:inline;" width="13" height="13"></code><br>Extension for Python-Markdown that makes lists truly sane. Custom indents for nested lists and fix for messy..</summary>

- [GitHub](https://github.com/radude/mdx_truly_sane_lists) (👨‍💻 4 · 🔀 10 · 📋 16 - 50% open · ⏱️ 19.07.2022)
- [PyPi](https://pypi.org/project/mdx-truly-sane-lists) (📥 2M / month):
	```
	pip install mdx-truly-sane-lists
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#markdown_extensions):
   ```yaml
   markdown_extensions:
     - mdx_truly_sane_lists
   ```
</details>
<details><summary><b><a href="https://github.com/sivakov512/python-markdown-full-yaml-metadata">YAML metadata</a></b>  - 🥈13 ·  ⭐ 29 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1459/PNG/32/2799201-jigsaw-processing_99781.png" style="display:inline;" width="13" height="13"></code><br>YAML metadata extension for Python-Markdown.</summary>

- [GitHub](https://github.com/sivakov512/python-markdown-full-yaml-metadata) (👨‍💻 7 · 🔀 3 · 📦 95 · 📋 10 - 30% open · ⏱️ 25.03.2026)
- [PyPi](https://pypi.org/project/markdown-full-yaml-metadata):
	```
	pip install markdown-full-yaml-metadata
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#markdown_extensions):
   ```yaml
   markdown_extensions:
     - full_yaml_metadata
   ```
</details>
<details><summary><b><a href="https://github.com/cesaremorel/markdown-inline-graphviz">Markdown Inline Graphviz</a></b>  - 🥈13 ·  ⭐ 5 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1459/PNG/32/2799201-jigsaw-processing_99781.png" style="display:inline;" width="13" height="13"></code><br>Render inline graphs with Markdown and Graphviz.</summary>

- [GitHub](https://github.com/cesaremorel/markdown-inline-graphviz) (👨‍💻 9 · 🔀 10 · ⏱️ 16.01.2024)
- [PyPi](https://pypi.org/project/markdown-inline-graphviz-extension) (📥 84K / month):
	```
	pip install markdown-inline-graphviz-extension
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#markdown_extensions):
   ```yaml
   markdown_extensions:
     - markdown_inline_graphviz
   ```
</details>
<details><summary><b><a href="https://github.com/FND/markdown-checklist">Markdown Checklist</a></b>  - 🥈11 ·  ⭐ 83 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1459/PNG/32/2799201-jigsaw-processing_99781.png" style="display:inline;" width="13" height="13"></code><br>Python Markdown extension for lists of tasks with checkboxes.</summary>

- [GitHub](https://github.com/FND/markdown-checklist) (👨‍💻 2 · 🔀 33 · 📋 8 - 12% open · ⏱️ 29.07.2022)
- [PyPi](https://pypi.org/project/markdown-checklist) (📥 4K / month):
	```
	pip install markdown-checklist
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#markdown_extensions):
   ```yaml
   markdown_extensions:
     - markdown_checklist.extension
   ```
</details>
<details><summary><b><a href="https://github.com/jambonrose/markdown_superscript_extension">MarkdownSuperscript</a></b>  - 🥈11 ·  ⭐ 2 · 💤 · <code><a href="http://bit.ly/3rqEWVr">BSD-2</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1459/PNG/32/2799201-jigsaw-processing_99781.png" style="display:inline;" width="13" height="13"></code><br>An extension to the Python Markdown package enabling superscript text.</summary>

- [GitHub](https://github.com/jambonrose/markdown_superscript_extension) (👨‍💻 2 · 🔀 3 · 📦 47 · 📋 4 - 25% open · ⏱️ 02.12.2018)
- [PyPi](https://pypi.org/project/MarkdownSuperscript) (📥 1K / month):
	```
	pip install MarkdownSuperscript
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#markdown_extensions):
   ```yaml
   markdown_extensions:
     - superscript
   ```
</details>
<details><summary><b><a href="https://github.com/adamb70/mdx-breakless-lists">Breakless Lists</a></b>  - 🥈10 ·  ⭐ 7 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1459/PNG/32/2799201-jigsaw-processing_99781.png" style="display:inline;" width="13" height="13"></code><br>Python markdown breakless lists extension.</summary>

- [GitHub](https://github.com/adamb70/mdx-breakless-lists) (🔀 3 · 📋 2 - 50% open · ⏱️ 08.10.2020)
- [PyPi](https://pypi.org/project/mdx-breakless-lists) (📥 41K / month):
	```
	pip install mdx-breakless-lists
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#markdown_extensions):
   ```yaml
   markdown_extensions:
     - mdx_breakless_lists
   ```
</details>
<details><summary><b><a href="https://github.com/ShadowKyogre/python-asciimathml">python-asciimathml</a></b>  - 🥈9 ·  ⭐ 4 · 💤 · <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1459/PNG/32/2799201-jigsaw-processing_99781.png" style="display:inline;" width="13" height="13"></code><br>python ASCIIMathML to Presentation MathML translator.</summary>

- [GitHub](https://github.com/ShadowKyogre/python-asciimathml) (👨‍💻 8 · 🔀 4 · ⏱️ 04.04.2017)
- [PyPi](https://pypi.org/project/asciimathml) (📥 2.4K / month):
	```
	pip install asciimathml
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#markdown_extensions):
   ```yaml
   markdown_extensions:
     - mdx_asciimathml
   ```
</details>
<details><summary><b><a href="https://github.com/jambonrose/markdown_subscript_extension">MarkdownSubscript</a></b>  - 🥈9 ·  ⭐ 3 · 💤 · <code><a href="http://bit.ly/3rqEWVr">BSD-2</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1459/PNG/32/2799201-jigsaw-processing_99781.png" style="display:inline;" width="13" height="13"></code><br>An extension to the Python Markdown package enabling subscript text.</summary>

- [GitHub](https://github.com/jambonrose/markdown_subscript_extension) (👨‍💻 2 · 🔀 1 · 📦 59 · 📋 5 - 40% open · ⏱️ 02.12.2018)
- [PyPi](https://pypi.org/project/MarkdownSubscript):
	```
	pip install MarkdownSubscript
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#markdown_extensions):
   ```yaml
   markdown_extensions:
     - subscript
   ```
</details>
<details><summary><b><a href="https://github.com/flywire/caption">caption</a></b>  - 🥉8 ·  ⭐ 12 · 💤 · <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1459/PNG/32/2799201-jigsaw-processing_99781.png" style="display:inline;" width="13" height="13"></code></summary>

- [GitHub](https://github.com/flywire/caption) (👨‍💻 4 · 🔀 3 · 📦 71 · 📋 8 - 87% open · ⏱️ 03.05.2025)
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#markdown_extensions):
   ```yaml
   markdown_extensions:
     - caption
     - image_captions
     - table_captions
   ```
</details>
<details><summary><b><a href="https://github.com/max-arnold/markdown-tweetable">Tweetable quotes</a></b>  - 🥉7 ·  ⭐ 16 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1459/PNG/32/2799201-jigsaw-processing_99781.png" style="display:inline;" width="13" height="13"></code><br>Python-Markdown extension to embed tweetable quotes into your blog posts.</summary>

- [GitHub](https://github.com/max-arnold/markdown-tweetable) (🔀 1 · 📦 5 · ⏱️ 25.03.2019)
- [PyPi](https://pypi.org/project/markdown-tweetable) (📥 270 / month):
	```
	pip install markdown-tweetable
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#markdown_extensions):
   ```yaml
   markdown_extensions:
     - tweetable.extension
   ```
</details>
<details><summary><b><a href="https://github.com/MadLittleMods/markdown-icons">markdown-icons</a></b>  - 🥉7 ·  ⭐ 15 · 💤 · <code>❗Unlicensed</code> · <code><img src="https://cdn.icon-icons.com/icons2/1459/PNG/32/2799201-jigsaw-processing_99781.png" style="display:inline;" width="13" height="13"></code><br>Easily display icon fonts in markdown.</summary>

- [GitHub](https://github.com/MadLittleMods/markdown-icons) (👨‍💻 4 · 🔀 11 · 📋 7 - 42% open · ⏱️ 09.12.2018)
- [PyPi](https://pypi.org/project/markdown-iconfonts) (📥 140 / month):
	```
	pip install markdown-iconfonts
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#markdown_extensions):
   ```yaml
   markdown_extensions:
     - iconfonts
   ```
</details>
<details><summary><b><a href="https://github.com/czue/markdown-emdash">markdown-emdash</a></b>  - 🥉6 ·  ⭐ 3 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1459/PNG/32/2799201-jigsaw-processing_99781.png" style="display:inline;" width="13" height="13"></code><br>Emdash extension for python-markdown.</summary>

- [GitHub](https://github.com/czue/markdown-emdash) (🔀 1 · 📦 39 · ⏱️ 18.05.2023)
- [PyPi](https://pypi.org/project/markdown-emdash):
	```
	pip install markdown-emdash
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#markdown_extensions):
   ```yaml
   markdown_extensions:
     - mdx_emdash
   ```
</details>
<details><summary><b><a href="https://github.com/pawamoy/markdown-pycon">Markdown PyCon</a></b>  - 🥉6 ·  ⭐ 2 · 💤 · <code><a href="http://bit.ly/3hkKRql">ISC</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1459/PNG/32/2799201-jigsaw-processing_99781.png" style="display:inline;" width="13" height="13"></code><br>Markdown extension to parse `pycon` code blocks without indentation or fences.</summary>

- [GitHub](https://github.com/pawamoy/markdown-pycon) (📦 11 · ⏱️ 10.01.2025)
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#markdown_extensions):
   ```yaml
   markdown_extensions:
     - pycon
   ```
</details>
<details><summary><b><a href="https://github.com/honzajavorek/markdown-del-ins">markdown-del-ins</a></b>  - 🥉5 ·  ⭐ 13 · 💤 · <code>❗Unlicensed</code> · <code><img src="https://cdn.icon-icons.com/icons2/1459/PNG/32/2799201-jigsaw-processing_99781.png" style="display:inline;" width="13" height="13"></code><br>Markdown extension to support the del and ins tags.</summary>

- [GitHub](https://github.com/honzajavorek/markdown-del-ins) (👨‍💻 2 · 🔀 1 · ⏱️ 09.01.2020)
- [PyPi](https://pypi.org/project/markdown-del-ins) (📥 3.1K / month):
	```
	pip install markdown-del-ins
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#markdown_extensions):
   ```yaml
   markdown_extensions:
     - markdown_del_ins
   ```
</details>
<details><summary><b><a href="https://github.com/ofek/mkpatcher">mkpatcher</a></b>  - 🥉5 ·  ⭐ 2 · 💤 · <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1459/PNG/32/2799201-jigsaw-processing_99781.png" style="display:inline;" width="13" height="13"></code><br>Python-Markdown extension allowing arbitrary scripts to modify MkDocs input files.</summary>

- [GitHub](https://github.com/ofek/mkpatcher) (📦 11 · ⏱️ 26.04.2020)
- [PyPi](https://pypi.org/project/mkpatcher):
	```
	pip install mkpatcher
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#markdown_extensions):
   ```yaml
   markdown_extensions:
     - mkpatcher
   ```
</details>
<details><summary><b><a href="https://github.com/alberic89/markdown_sub_sup">markdown_sub_sup</a></b>  - 🥉5 ·  ⭐ 2 · 💤 · <code><a href="http://bit.ly/37RvQcA">❗️LGPL-3.0</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1459/PNG/32/2799201-jigsaw-processing_99781.png" style="display:inline;" width="13" height="13"></code><br>A python markdown extension for add sub and sup support.</summary>

- [GitHub](https://github.com/alberic89/markdown_sub_sup) (⏱️ 24.03.2023)
- [PyPi](https://pypi.org/project/markdown-sub-sup) (📥 380 / month):
	```
	pip install markdown-sub-sup
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#markdown_extensions):
   ```yaml
   markdown_extensions:
     - markdown_sub_sup
   ```
</details>
<details><summary><b><a href="https://github.com/RickTalken/kbdextension">KBD Extension</a></b>  - 🥉5 ·  ⭐ 2 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1459/PNG/32/2799201-jigsaw-processing_99781.png" style="display:inline;" width="13" height="13"></code><br>KBD Extension for Python-Markdown.</summary>

- [GitHub](https://github.com/RickTalken/kbdextension) (🔀 1 · 📦 12 · ⏱️ 08.06.2020)
- [PyPi](https://pypi.org/project/kbdextension) (📥 130 / month):
	```
	pip install kbdextension
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#markdown_extensions):
   ```yaml
   markdown_extensions:
     - kbdextension
   ```
</details>
<details><summary><b><a href="https://github.com/heartbeatsjp/markdown-extension-hbfm">HEARTBEATS Flavored Markdown</a></b>  - 🥉4 ·  ⭐ 15 · 💤 · <code>❗Unlicensed</code> · <code><img src="https://cdn.icon-icons.com/icons2/1459/PNG/32/2799201-jigsaw-processing_99781.png" style="display:inline;" width="13" height="13"></code><br>HEARTBEATS Flavored Markdown extension.</summary>

- [GitHub](https://github.com/heartbeatsjp/markdown-extension-hbfm) (👨‍💻 2 · 🔀 1 · 📦 10 · ⏱️ 01.03.2018)
- [PyPi](https://pypi.org/project/hbfm):
	```
	pip install hbfm
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#markdown_extensions):
   ```yaml
   markdown_extensions:
     - hbfm.inline_coloring
     - hbfm.inline_list
     - hbfm.number_headers
     - hbfm.quote_uri_hash
   ```
</details>
<details><summary><b><a href="https://github.com/aleray/mdx_semanticwikilinks">Semantic WikiLinks Extension</a></b>  - 🥉4 ·  ⭐ 9 · 💤 · <code>❗Unlicensed</code> · <code><img src="https://cdn.icon-icons.com/icons2/1459/PNG/32/2799201-jigsaw-processing_99781.png" style="display:inline;" width="13" height="13"></code><br>Python-Markdown extension to add support for semantic (wiki)links (RDFa).</summary>

- [GitHub](https://github.com/aleray/mdx_semanticwikilinks) (🔀 1 · ⏱️ 15.08.2012)
- [PyPi](https://pypi.org/project/mdx-semanticwikilinks) (📥 540 / month):
	```
	pip install mdx-semanticwikilinks
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#markdown_extensions):
   ```yaml
   markdown_extensions:
     - mdx_semanticwikilinks
   ```
</details>
<details><summary><b><a href="https://github.com/aleray/mdx_semanticdata">Semantic Data Extension</a></b>  - 🥉4 ·  ⭐ 8 · 💤 · <code>❗Unlicensed</code> · <code><img src="https://cdn.icon-icons.com/icons2/1459/PNG/32/2799201-jigsaw-processing_99781.png" style="display:inline;" width="13" height="13"></code><br>Python-Markdown extension to add support for semantic data (RDFa).</summary>

- [GitHub](https://github.com/aleray/mdx_semanticdata) (🔀 1 · ⏱️ 05.11.2012)
- [PyPi](https://pypi.org/project/mdx-semanticdata) (📥 320 / month):
	```
	pip install mdx-semanticdata
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#markdown_extensions):
   ```yaml
   markdown_extensions:
     - mdx_semanticdata
   ```
</details>
<details><summary><b><a href="https://gitlab.com/mbarkhau/markdown-katex">markdown-katex</a></b>  - 🥉3 ·  ⭐ 11 · 💤 · <code>❗Unlicensed</code> · <code><img src="https://cdn.icon-icons.com/icons2/1459/PNG/32/2799201-jigsaw-processing_99781.png" style="display:inline;" width="13" height="13"></code><br>KaTeX extension for Python Markdown.</summary>

- [PyPi](https://pypi.org/project/markdown-katex):
	```
	pip install markdown-katex
	```
- [GitLab](https://gitlab.com/mbarkhau/markdown-katex) (🔀 4 · 📋 17 - 23% open · ⏱️ 14.05.2019)
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#markdown_extensions):
   ```yaml
   markdown_extensions:
     - markdown_katex
   ```
</details>
<details><summary><b><a href="https://github.com/aleray/mdx_cite">Cite Extension</a></b>  - 🥉3 ·  ⭐ 7 · 💤 · <code>❗Unlicensed</code> · <code><img src="https://cdn.icon-icons.com/icons2/1459/PNG/32/2799201-jigsaw-processing_99781.png" style="display:inline;" width="13" height="13"></code><br>Python-Markdown extension to support the cite tag.</summary>

- [GitHub](https://github.com/aleray/mdx_cite) (🔀 3 · ⏱️ 21.04.2012)
- [PyPi](https://pypi.org/project/mdx-cite):
	```
	pip install mdx-cite
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#markdown_extensions):
   ```yaml
   markdown_extensions:
     - mdx_cite
   ```
</details>
<details><summary><b><a href="https://gitlab.com/WillDaSilva/markdown_grid_tables">Markdown Grid Tables</a></b>  - 🥉1 ·  ⭐ 1 · 💤 · <code>❗Unlicensed</code> · <code><img src="https://cdn.icon-icons.com/icons2/1459/PNG/32/2799201-jigsaw-processing_99781.png" style="display:inline;" width="13" height="13"></code><br>[Python-Markdown](https://python-markdown.github.io/) [extension](https://python-markdown.github.io/extensions/api/)..</summary>

- [PyPi](https://pypi.org/project/markdown-grid-tables):
	```
	pip install markdown-grid-tables
	```
- [GitLab](https://gitlab.com/WillDaSilva/markdown_grid_tables) (🔀 7 · 📋 4 - 75% open · ⏱️ 09.02.2022)
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#markdown_extensions):
   ```yaml
   markdown_extensions:
     - markdown_grid_tables
   ```
</details>
<details><summary><b><a href="https://pypi.org/project/markdown-djangostaticimage/">Django Static Image</a></b>  - 🥉1 · <code>❗Unlicensed</code> · <code><img src="https://cdn.icon-icons.com/icons2/1459/PNG/32/2799201-jigsaw-processing_99781.png" style="display:inline;" width="13" height="13"></code></summary>

- [PyPi](https://pypi.org/project/markdown-djangostaticimage) (📥 67 / month):
	```
	pip install markdown-djangostaticimage
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#markdown_extensions):
   ```yaml
   markdown_extensions:
     - django_static_image
   ```
</details>
<br>

## 🧭 Navigation & page building

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://github.com/oprypin/mkdocs-literate-nav">literate-nav</a></b>  - 🥇23 ·  ⭐ 100 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>MkDocs plugin to specify the navigation in Markdown instead of YAML.</summary>

- [GitHub](https://github.com/oprypin/mkdocs-literate-nav) (🔀 10 · 📦 3.6K · 📋 34 - 47% open · ⏱️ 17.04.2026)
- [PyPi](https://pypi.org/project/mkdocs-literate-nav) (📥 1.7M / month):
	```
	pip install mkdocs-literate-nav
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - literate-nav
   ```
</details>
<details><summary><b><a href="https://github.com/lukasgeiter/mkdocs-awesome-nav">awesome-nav</a></b>  - 🥇22 ·  ⭐ 620 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>A plugin for customizing the navigation structure of your MkDocs site.</summary>

- [GitHub](https://github.com/lukasgeiter/mkdocs-awesome-nav) (👨‍💻 12 · 🔀 43 · 📦 600 · 📋 120 - 18% open · ⏱️ 10.04.2026)
- [PyPi](https://pypi.org/project/mkdocs-awesome-nav) (📥 260K / month):
	```
	pip install mkdocs-awesome-nav
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - awesome-nav
   ```
</details>
<details><summary><b><a href="https://github.com/unverbuggt/mkdocs-encryptcontent-plugin">encryptcontent</a></b>  - 🥇22 ·  ⭐ 170 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>A MkDocs plugin that encrypt/decrypt markdown content with AES.</summary>

- [GitHub](https://github.com/unverbuggt/mkdocs-encryptcontent-plugin) (👨‍💻 7 · 🔀 17 · 📥 100 · 📦 1.3K · 📋 74 - 8% open · ⏱️ 17.05.2026)
- [PyPi](https://pypi.org/project/mkdocs-encryptcontent-plugin) (📥 14K / month):
	```
	pip install mkdocs-encryptcontent-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - encryptcontent
   ```
</details>
<details><summary><b><a href="https://github.com/aklajnert/mkdocs-simple-hooks">mkdocs-simple-hooks</a></b>  - 🥈19 ·  ⭐ 67 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Define your own hooks for mkdocs, without having to create a new package.</summary>

- [GitHub](https://github.com/aklajnert/mkdocs-simple-hooks) (👨‍💻 6 · 🔀 4 · 📥 67 · 📦 2.3K · ⏱️ 14.11.2023)
- [PyPi](https://pypi.org/project/mkdocs-simple-hooks) (📥 130K / month):
	```
	pip install mkdocs-simple-hooks
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - mkdocs-simple-hooks
   ```
</details>
<details><summary><b><a href="https://github.com/oprypin/mkdocs-section-index">section-index</a></b>  - 🥈18 ·  ⭐ 95 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>MkDocs plugin to allow clickable sections that lead to an index page.</summary>

- [GitHub](https://github.com/oprypin/mkdocs-section-index) (👨‍💻 3 · 🔀 7 · 📋 24 - 33% open · ⏱️ 17.04.2026)
- [PyPi](https://pypi.org/project/mkdocs-section-index) (📥 1.3M / month):
	```
	pip install mkdocs-section-index
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - section-index
   ```
</details>
<details><summary><b><a href="https://github.com/apenwarr/mkdocs-exclude">exclude</a></b>  - 🥈17 ·  ⭐ 96 · 💤 · <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>A mkdocs plugin that lets you exclude files or trees from your output.</summary>

- [GitHub](https://github.com/apenwarr/mkdocs-exclude) (🔀 9 · 📦 3.1K · 📋 12 - 75% open · ⏱️ 20.02.2019)
- [PyPi](https://pypi.org/project/mkdocs-exclude) (📥 220K / month):
	```
	pip install mkdocs-exclude
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - exclude
   ```
</details>
<details><summary><b><a href="https://github.com/mkdocs-publisher/mkdocs-publisher">Publisher for MkDocs - meta</a></b>  - 🥈16 ·  ⭐ 130 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Automatic navigation based on files metadata with URL name and publication status control.</summary>

- [GitHub](https://github.com/mkdocs-publisher/mkdocs-publisher) (👨‍💻 4 · 🔀 11 · 📥 140 · 📦 99 · 📋 31 - 25% open · ⏱️ 26.11.2025)
- [PyPi](https://pypi.org/project/mkdocs-publisher) (📥 3.5K / month):
	```
	pip install mkdocs-publisher
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - pub-meta
   ```
</details>
<details><summary><b><a href="https://github.com/EddyLuten/mkdocs-live-edit-plugin">mkdocs-live-edit-plugin</a></b>  - 🥈14 ·  ⭐ 37 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>An MkDocs plugin that allows editing pages directly from the browser.</summary>

- [GitHub](https://github.com/EddyLuten/mkdocs-live-edit-plugin) (👨‍💻 6 · 🔀 9 · 📦 18 · ⏱️ 09.04.2026)
- [PyPi](https://pypi.org/project/mkdocs-live-edit-plugin) (📥 480 / month):
	```
	pip install mkdocs-live-edit-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - live-edit
   ```
</details>
<details><summary><b><a href="https://github.com/EddyLuten/mkdocs-categories-plugin">mkdocs-categories-plugin</a></b>  - 🥈14 ·  ⭐ 16 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>An MkDocs plugin allowing for categorization of wiki pages.</summary>

- [GitHub](https://github.com/EddyLuten/mkdocs-categories-plugin) (🔀 1 · 📦 24 · ⏱️ 09.04.2026)
- [PyPi](https://pypi.org/project/mkdocs-categories-plugin) (📥 4K / month):
	```
	pip install mkdocs-categories-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - categories
   ```
</details>
<details><summary><b><a href="https://github.com/shu307/mkdocs-nav-weight">mkdocs-nav-weight</a></b>  - 🥈14 ·  ⭐ 14 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>A simple mkdocs plugin, enables to organize Navigation in a more markdownic way.</summary>

- [GitHub](https://github.com/shu307/mkdocs-nav-weight) (👨‍💻 4 · 🔀 3 · 📦 130 · ⏱️ 09.09.2025)
- [PyPi](https://pypi.org/project/mkdocs-nav-weight) (📥 42K / month):
	```
	pip install mkdocs-nav-weight
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - mkdocs-nav-weight
   ```
</details>
<details><summary><b><a href="https://github.com/tombreit/mkdocs-pagetree-plugin">mkdocs-pagetree-plugin</a></b>  - 🥈14 ·  ⭐ 12 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>MkDocs plugin that allows you to display the page tree. Like `sitemap.xml`, but for humans.</summary>

- [GitHub](https://github.com/tombreit/mkdocs-pagetree-plugin) (👨‍💻 3 · 🔀 3 · 📦 32 · 📋 15 - 13% open · ⏱️ 02.11.2025)
- [PyPi](https://pypi.org/project/mkdocs-pagetree-plugin) (📥 22K / month):
	```
	pip install mkdocs-pagetree-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - pagetree
   ```
</details>
<details><summary><b><a href="https://github.com/DariuszPorowski/mkdocs-file-filter-plugin">file-filter</a></b>  - 🥈13 ·  ⭐ 10 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>A MkDocs plugin that lets you exclude/include docs files using globs, regexes, gitignore-style file and..</summary>

- [GitHub](https://github.com/DariuszPorowski/mkdocs-file-filter-plugin) (👨‍💻 4 · 🔀 5 · 📥 120 · 📦 18 · 📋 15 - 46% open · ⏱️ 19.07.2024)
- [PyPi](https://pypi.org/project/mkdocs-file-filter-plugin) (📥 3.7K / month):
	```
	pip install mkdocs-file-filter-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - file-filter
   ```
</details>
<details><summary><b><a href="https://github.com/smarie/mkdocs-gallery">mkdocs-gallery</a></b>  - 🥉12 ·  ⭐ 49 · 💤 · <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Same features as sphinx-gallery (https://sphinx-gallery.github.io/) but on mkdocs (https://www.mkdocs.org/) (no sphinx..</summary>

- [GitHub](https://github.com/smarie/mkdocs-gallery) (👨‍💻 10 · 🔀 17 · 📋 75 - 41% open · ⏱️ 30.09.2024)
- [PyPi](https://pypi.org/project/mkdocs-gallery):
	```
	pip install mkdocs-gallery
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - gallery
   ```
</details>
<details><summary><b><a href="https://github.com/DerwenAI/mkrefs">MkRefs</a></b>  - 🥉10 ·  ⭐ 41 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>MkDocs plugin to generate semantic reference Markdown pages from a knowledge graph.</summary>

- [GitHub](https://github.com/DerwenAI/mkrefs) (👨‍💻 2 · 📦 5 · ⏱️ 31.08.2023)
- [PyPi](https://pypi.org/project/mkrefs) (📥 110 / month):
	```
	pip install mkrefs
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - mkrefs
   ```
</details>
<details><summary><b><a href="https://github.com/mysiki/mkdocs_include_dir_to_nav">include directory to navigation</a></b>  - 🥉10 ·  ⭐ 31 · 💤 · <code>❗Unlicensed</code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Simple MKDocs plugin than permit to fetch and replace directory in navigation.</summary>

- [GitHub](https://github.com/mysiki/mkdocs_include_dir_to_nav) (🔀 4 · 📥 17 · 📋 4 - 50% open · ⏱️ 01.03.2022)
- [PyPi](https://pypi.org/project/mkdocs-include-dir-to-nav) (📥 60K / month):
	```
	pip install mkdocs-include-dir-to-nav
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - include_dir_to_nav
   ```
</details>
<details><summary><b><a href="https://github.com/mihaigalos/mkdocs-breadcrumbs-plugin">mkdocs-breadcrumbs-plugin</a></b>  - 🥉10 ·  ⭐ 7 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Location-based breadcrumbs navigation.</summary>

- [GitHub](https://github.com/mihaigalos/mkdocs-breadcrumbs-plugin) (👨‍💻 5 · 🔀 2 · 📦 13 · 📋 5 - 40% open · ⏱️ 18.04.2025)
- [PyPi](https://pypi.org/project/mkdocs-breadcrumbs-plugin) (📥 1.4K / month):
	```
	pip install mkdocs-breadcrumbs-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - mkdocs-breadcrumbs-plugin
   ```
</details>
<details><summary><b><a href="https://github.com/zachhannum/mkdocs-toc-sidebar-plugin">toc-sidebar</a></b>  - 🥉9 ·  ⭐ 4 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>An MkDocs plugin that allows users to add additional content to the ToC sidebar using the Material theme.</summary>

- [GitHub](https://github.com/zachhannum/mkdocs-toc-sidebar-plugin) (👨‍💻 2 · 🔀 3 · 📦 54 · ⏱️ 11.01.2020)
- [PyPi](https://pypi.org/project/mkdocs-toc-sidebar-plugin) (📥 460 / month):
	```
	pip install mkdocs-toc-sidebar-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - toc-sidebar
   ```
</details>
<details><summary><b><a href="https://github.com/zachhannum/mkdocs-vim-md-tags-plugin">vim-md-tags</a></b>  - 🥉8 ·  ⭐ 6 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>An MkDocs plugin that creates a vim tag file of all markdown files.</summary>

- [GitHub](https://github.com/zachhannum/mkdocs-vim-md-tags-plugin) (👨‍💻 4 · 🔀 1 · 📦 12 · ⏱️ 08.05.2020)
- [PyPi](https://pypi.org/project/mkdocs-vim-md-tags-plugin) (📥 76 / month):
	```
	pip install mkdocs-vim-md-tags-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - vim-md-tags
   ```
</details>
<details><summary><b><a href="https://github.com/Rylon/mkdocs-nav-enhancements">mkdocs-nav-enhancements</a></b>  - 🥉8 ·  ⭐ 3 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>WIP plugin for working with titles of pages in MkDocs.</summary>

- [GitHub](https://github.com/Rylon/mkdocs-nav-enhancements) (⏱️ 24.07.2019)
- [PyPi](https://pypi.org/project/mkdocs-nav-enhancements) (📥 6.4K / month):
	```
	pip install mkdocs-nav-enhancements
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - mkdocs-nav-enhancements
   ```
</details>
<details><summary><b><a href="https://github.com/thomaszwagerman/mkdocs-authors-plugin">authors</a></b>  - 🥉7 ·  ⭐ 2 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>MkDocs plugin to display authors dynamically on a template using an .authors.yml file.</summary>

- [GitHub](https://github.com/thomaszwagerman/mkdocs-authors-plugin) (📋 4 - 25% open · ⏱️ 05.08.2025)
- [PyPi](https://pypi.org/project/mkdocs-authors-plugin) (📥 53 / month):
	```
	pip install mkdocs-authors-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - authors
   ```
</details>
<details><summary><b><a href="https://github.com/magicaljellybeans/mkdocs_schema_reader">schema-reader</a></b>  - 🥉6 ·  ⭐ 7 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>A mkdocs plugin that scans specified directories and files for JSON Schema files, converts them to markdown and builds..</summary>

- [GitHub](https://github.com/magicaljellybeans/mkdocs_schema_reader) (👨‍💻 3 · 🔀 2 · 📋 4 - 50% open · ⏱️ 23.06.2021)
- [PyPi](https://pypi.org/project/mkdocs-schema-reader) (📥 3.5K / month):
	```
	pip install mkdocs-schema-reader
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - schema_reader
   ```
</details>
<details><summary><b><a href="https://github.com/swan-cern/mkdocs-swangallery">SWAN Gallery</a></b>  - 🥉6 ·  ⭐ 1 · <code><a href="http://bit.ly/3pwmjO5">❗️AGPL-3.0</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>MkDocs plugin to generate a SWAN Gallery.</summary>

- [GitHub](https://github.com/swan-cern/mkdocs-swangallery) (👨‍💻 3 · 🔀 1 · 📦 3 · ⏱️ 23.01.2026)
- [PyPi](https://pypi.org/project/mkdocs-swangallery) (📥 95 / month):
	```
	pip install mkdocs-swangallery
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - swangallery
   ```
</details>
<details><summary><b><a href="https://github.com/supcik/mkdocs-select-files">select-files</a></b>  - 🥉6 · 💤 · <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Filter pages for assignments.</summary>

- [GitHub](https://github.com/supcik/mkdocs-select-files) (📦 9 · ⏱️ 05.09.2019)
- [PyPi](https://pypi.org/project/mkdocs-select-files) (📥 73 / month):
	```
	pip install mkdocs-select-files
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - select-files
   ```
</details>
<details><summary><b><a href="https://github.com/carlosperate/mkdocs-awesome-list-plugin">awesome-list</a></b>  - 🥉5 ·  ⭐ 5 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>MkDocs Plugin to inject social media cards for each entry in an awesome-list.</summary>

- [GitHub](https://github.com/carlosperate/mkdocs-awesome-list-plugin) (⏱️ 11.03.2026)
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - awesome-list
   ```
</details>
<details><summary><b><a href="https://github.com/six-two/mkdocs-remove-sections-plugin">MkDocs Remove Sections Plugin</a></b>  - 🥉5 ·  ⭐ 1 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Remove sections with specific titles from your MkDocs pages.</summary>

- [GitHub](https://github.com/six-two/mkdocs-remove-sections-plugin) (⏱️ 31.05.2026)
- [PyPi](https://pypi.org/project/mkdocs-remove-sections-plugin) (📥 250 / month):
	```
	pip install mkdocs-remove-sections-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - remove_sections
   ```
</details>
<details><summary><b><a href="https://github.com/idlesign/mkdocs-navsorted-plugin">mkdocs-navsorted-plugin</a></b>  - 🥉5 · 💤 · <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>mkdocs plugin to get nav sorted without yml directives.</summary>

- [GitHub](https://github.com/idlesign/mkdocs-navsorted-plugin) (⏱️ 24.05.2025)
- [PyPi](https://pypi.org/project/mkdocs-navsorted-plugin) (📥 69 / month):
	```
	pip install mkdocs-navsorted-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - navsorted
   ```
</details>
<details><summary><b><a href="https://github.com/mattchristopher314/mkdocs-title-casing-plugin">mkdocs-title-casing-plugin</a></b>  - 🥉4 ·  ⭐ 2 · 💤 · <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>A lightweight mkdocs plugin to add title casing to all mkdocs pages and sections.</summary>

- [GitHub](https://github.com/mattchristopher314/mkdocs-title-casing-plugin) (🔀 1 · 📦 11 · ⏱️ 02.09.2023)
- [PyPi](https://pypi.org/project/mkdocs-title-casing-plugin):
	```
	pip install mkdocs-title-casing-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - title-casing
   ```
</details>
<details><summary><b><a href="https://github.com/Andre601/mkdocs-pagenav-generator">pagenav-generator</a></b>  - 🥉2 ·  ⭐ 4 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Little something to automatically generate a Navigation within a page itself. Depends on Awesome-pages.</summary>

- [GitHub](https://github.com/Andre601/mkdocs-pagenav-generator) (👨‍💻 2 · 🔀 1 · ⏱️ 17.04.2022)
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - pagenav-generator
   ```
</details>
<br>

## ✅ Quality checks (code blocks, spelling, etc.)

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://github.com/pawamoy/mkdocs-spellcheck">mkdocs-spellcheck</a></b>  - 🥇19 ·  ⭐ 22 · <code><a href="http://bit.ly/3hkKRql">ISC</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>A spell checker plugin for MkDocs.</summary>

- [GitHub](https://github.com/pawamoy/mkdocs-spellcheck) (👨‍💻 7 · 🔀 5 · 📦 88 · ⏱️ 11.02.2026)
- [PyPi](https://pypi.org/project/mkdocs-spellcheck) (📥 83K / month):
	```
	pip install mkdocs-spellcheck
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - spellcheck
   ```
</details>
<details><summary><b><a href="https://github.com/koaning/mktestdocs">mktestdocs</a></b>  - 🥈14 ·  ⭐ 160 · <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code><br>Run pytest against markdown files/docstrings.</summary>

- [GitHub](https://github.com/koaning/mktestdocs) (👨‍💻 6 · 🔀 11 · 📋 8 - 37% open · ⏱️ 10.11.2025)
- [PyPi](https://pypi.org/project/mktestdocs) (📥 47K / month):
	```
	pip install mktestdocs
	```
</details>
<details><summary><b><a href="https://github.com/byrnereese/linkchecker-mkdocs">Link Checker</a></b>  - 🥈10 ·  ⭐ 17 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code><br>Python asyncio + aiohttp Markdown *.md URL link checker: 10,000 files/second.</summary>

- [GitHub](https://github.com/byrnereese/linkchecker-mkdocs) (👨‍💻 5 · 🔀 6 · 📋 10 - 90% open · ⏱️ 24.08.2021)
- [PyPi](https://pypi.org/project/mkdocs-linkcheck) (📥 33K / month):
	```
	pip install mkdocs-linkcheck
	```
</details>
<details><summary><b><a href="https://github.com/oprypin/mkdocs-code-validator">mkdocs-code-validator</a></b>  - 🥈10 ·  ⭐ 4 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Checks Markdown code blocks in a MkDocs site against user-defined actions.</summary>

- [GitHub](https://github.com/oprypin/mkdocs-code-validator) (📦 21 · ⏱️ 17.04.2026)
- [PyPi](https://pypi.org/project/mkdocs-code-validator):
	```
	pip install mkdocs-code-validator
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - code-validator
   ```
</details>
<details><summary><b><a href="https://github.com/fralau/mkdocs-test">MkDocs-Test</a></b>  - 🥉6 ·  ⭐ 10 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>A framework for testing MkDocs projects.</summary>

- [GitHub](https://github.com/fralau/mkdocs-test) (👨‍💻 3 · 📋 5 - 20% open · ⏱️ 13.11.2025)
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - test
   ```
</details>
<details><summary><b><a href="https://github.com/byrnereese/codechecker-mkdocs">mkdocs-codecheck</a></b>  - 🥉5 ·  ⭐ 3 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code><br>Traverses a directory tree looking for code samples, then attempts to validate each code sample found.</summary>

- [GitHub](https://github.com/byrnereese/codechecker-mkdocs) (👨‍💻 6 · ⏱️ 16.12.2021)
- [PyPi](https://pypi.org/project/mkdocs-codecheck):
	```
	pip install mkdocs-codecheck
	```
</details>
<br>

## 🔍 Search & tables of content

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://github.com/wilhelmer/mkdocs-localsearch">localsearch</a></b>  - 🥇16 ·  ⭐ 32 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>A MkDocs plugin to make the native search plugin work locally (file:// protocol).</summary>

- [GitHub](https://github.com/wilhelmer/mkdocs-localsearch) (👨‍💻 6 · 🔀 6 · 📦 110 · ⏱️ 02.01.2023)
- [PyPi](https://pypi.org/project/mkdocs-localsearch) (📥 5.4K / month):
	```
	pip install mkdocs-localsearch
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - localsearch
   ```
</details>
<details><summary><b><a href="https://github.com/chrieke/mkdocs-exclude-search">exclude-search</a></b>  - 🥈13 ·  ⭐ 29 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>A mkdocs plugin that excludes selected chapters from the docs search index.</summary>

- [GitHub](https://github.com/chrieke/mkdocs-exclude-search) (👨‍💻 6 · 🔀 3 · 📥 18 · ⏱️ 04.12.2023)
- [PyPi](https://pypi.org/project/mkdocs-exclude-search) (📥 55K / month):
	```
	pip install mkdocs-exclude-search
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - exclude-search
   ```
</details>
<details><summary><b><a href="https://github.com/costantinoai/mkdocs-task-collector">mkdocs-task-collector</a></b>  - 🥉10 ·  ⭐ 6 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>mkdocs plugin to generate a comprehensive and organized task list, making it easier to manage and track tasks, notes,..</summary>

- [GitHub](https://github.com/costantinoai/mkdocs-task-collector) (👨‍💻 2 · 🔀 1 · 📦 5 · ⏱️ 04.04.2025)
- [PyPi](https://pypi.org/project/mkdocs-task-collector) (📥 130K / month):
	```
	pip install mkdocs-task-collector
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - task-collector
   ```
</details>
<details><summary><b><a href="https://github.com/jldiaz/mkdocs-plugin-tags">tags</a></b>  - 🥉8 ·  ⭐ 43 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Processes tags in yaml metadata.</summary>

- [GitHub](https://github.com/jldiaz/mkdocs-plugin-tags) (👨‍💻 3 · 🔀 17 · 📋 14 - 42% open · ⏱️ 02.09.2021)
- [PyPi](https://pypi.org/project/mkdocs-plugin-tags) (📥 490 / month):
	```
	pip install mkdocs-plugin-tags
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - tags
   ```
</details>
<details><summary><b><a href="https://github.com/six-two/mkdocs-extract-listings-plugin">extract listings</a></b>  - 🥉5 ·  ⭐ 2 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Generate a page with all listings and/or a search page for listings.</summary>

- [GitHub](https://github.com/six-two/mkdocs-extract-listings-plugin) (⏱️ 02.06.2026)
- [PyPi](https://pypi.org/project/mkdocs-extract-listings-plugin):
	```
	pip install mkdocs-extract-listings-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - extract_listings
   ```
</details>
<br>

## 🍱 Site conversion (PDF/ePUB/etc.)

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://github.com/orzih/mkdocs-with-pdf">mkdocs-with-pdf</a></b>  - 🥇24 ·  ⭐ 390 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Generate a single PDF file from MkDocs repository.</summary>

- [GitHub](https://github.com/orzih/mkdocs-with-pdf) (👨‍💻 6 · 🔀 72 · 📦 910 · 📋 120 - 57% open · ⏱️ 14.10.2021)
- [PyPi](https://pypi.org/project/mkdocs-with-pdf) (📥 280K / month):
	```
	pip install mkdocs-with-pdf
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - with-pdf
   ```
</details>
<details><summary><b><a href="https://github.com/zhaoterryy/mkdocs-pdf-export-plugin">pdf-export</a></b>  - 🥇22 ·  ⭐ 340 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>An MkDocs plugin to export content pages as PDF files.</summary>

- [GitHub](https://github.com/zhaoterryy/mkdocs-pdf-export-plugin) (👨‍💻 12 · 🔀 39 · 📦 1.5K · 📋 90 - 48% open · ⏱️ 08.10.2025)
- [PyPi](https://pypi.org/project/mkdocs-pdf-export-plugin) (📥 39K / month):
	```
	pip install mkdocs-pdf-export-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - pdf-export
   ```
</details>
<details><summary><b><a href="https://github.com/timvink/mkdocs-print-site-plugin">print-site</a></b>  - 🥈18 ·  ⭐ 180 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>MkDocs Plugin that adds an additional page that combines all pages, allowing easy exports to PDF and standalone HTML.</summary>

- [GitHub](https://github.com/timvink/mkdocs-print-site-plugin) (👨‍💻 17 · 🔀 28 · 📋 110 - 11% open · ⏱️ 10.04.2026)
- [PyPi](https://pypi.org/project/mkdocs-print-site-plugin) (📥 180K / month):
	```
	pip install mkdocs-print-site-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - print-site
   ```
</details>
<details><summary><b><a href="https://github.com/adrienbrignon/mkdocs-exporter">mkdocs-exporter</a></b>  - 🥈18 ·  ⭐ 130 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>The fastest and most configurable plugin for MkDocs, allowing seamless export of individual pages and/or entire..</summary>

- [GitHub](https://github.com/adrienbrignon/mkdocs-exporter) (👨‍💻 4 · 🔀 16 · 📦 49 · 📋 71 - 56% open · ⏱️ 29.10.2024)
- [PyPi](https://pypi.org/project/mkdocs-exporter) (📥 23K / month):
	```
	pip install mkdocs-exporter
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - exporter
   ```
</details>
<details><summary><b><a href="https://github.com/comwes/mkpdfs-mkdocs-plugin">mkpdfs</a></b>  - 🥈16 ·  ⭐ 100 · 💤 · <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Converts your mkdocs documentation in PDF, to be shared with users.</summary>

- [GitHub](https://github.com/comwes/mkpdfs-mkdocs-plugin) (👨‍💻 9 · 🔀 29 · 📥 44 · 📦 66 · 📋 39 - 30% open · ⏱️ 11.08.2021)
- [PyPi](https://pypi.org/project/mkpdfs-mkdocs) (📥 810 / month):
	```
	pip install mkpdfs-mkdocs
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - mkpdfs
   ```
</details>
<details><summary><b><a href="https://github.com/jgrassler/mkdocs-pandoc">mkdocs-pandoc</a></b>  - 🥉14 ·  ⭐ 110 · 💤 · <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code><br>[unmaintained] mkdocs - pandoc converter: use this fork https://github.com/twardoch/mkdocs-combine.</summary>

- [GitHub](https://github.com/jgrassler/mkdocs-pandoc) (👨‍💻 4 · 🔀 22 · 📦 78 · 📋 23 - 56% open · ⏱️ 14.03.2016)
- [PyPi](https://pypi.org/project/mkdocs-pandoc) (📥 600 / month):
	```
	pip install mkdocs-pandoc
	```
</details>
<details><summary><b><a href="https://github.com/smaxtec/mkdocs-pdf-with-js-plugin">pdf-with-js</a></b>  - 🥉12 ·  ⭐ 8 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>A MkDocs plugin that exports your documentation as PDF with rendered JavaScript content.</summary>

- [GitHub](https://github.com/smaxtec/mkdocs-pdf-with-js-plugin) (👨‍💻 4 · 🔀 3 · 📦 13 · ⏱️ 23.07.2021)
- [PyPi](https://pypi.org/project/mkdocs-pdf-with-js-plugin) (📥 880 / month):
	```
	pip install mkdocs-pdf-with-js-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - pdf-with-js
   ```
</details>
<details><summary><b><a href="https://github.com/HaoLiuHust/mkdocs-mk2pdf-plugin">mk2pdf-export</a></b>  - 🥉6 ·  ⭐ 11 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>The plugin is based on https://github.com/zhaoterryy/mkdocs-pdf-export-plugin/ ,the main change is use pandoc to..</summary>

- [GitHub](https://github.com/HaoLiuHust/mkdocs-mk2pdf-plugin) (👨‍💻 4 · 🔀 4 · 📦 3 · ⏱️ 11.09.2020)
- [PyPi](https://pypi.org/project/mkdocs-mk2pdf-plugin):
	```
	pip install mkdocs-mk2pdf-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - mk2pdf-export
   ```
</details>
<details><summary><b><a href="https://github.com/JakubAndrysek/mkdocs-zip-folders">mkdocs-zip-folders</a></b>  - 🥉6 ·  ⭐ 4 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>MkDocs plugin to zip configured folders and add them to the site.</summary>

- [GitHub](https://github.com/JakubAndrysek/mkdocs-zip-folders) (👨‍💻 2 · 🔀 2 · ⏱️ 03.07.2025)
- [PyPi](https://pypi.org/project/mkdocs-zip-folders) (📥 170 / month):
	```
	pip install mkdocs-zip-folders
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - zip_folders
   ```
</details>
<details><summary><b><a href="https://github.com/M00nF1sh/mkdocs-helm">helm</a></b>  - 🥉4 ·  ⭐ 1 · 💤 · <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>An mkdocs plugin that turns docs website into helm repository.</summary>

- [GitHub](https://github.com/M00nF1sh/mkdocs-helm) (🔀 1 · ⏱️ 21.11.2018)
- [PyPi](https://pypi.org/project/mkdocs-helm) (📥 59 / month):
	```
	pip install mkdocs-helm
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - helm-repo
   ```
</details>
<details><summary><b><a href="https://github.com/martinohanlon/mkdocs_autozip">mkdocs-autozip</a></b>  - 🥉1 ·  ⭐ 2 · 💤 · <code>❗Unlicensed</code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>A mkdocs plugin for auto zipping the document source.</summary>

- [GitHub](https://github.com/martinohanlon/mkdocs_autozip) (⏱️ 05.10.2022)
- [PyPi](https://pypi.org/project/mkdocs-autozip) (📥 98 / month):
	```
	pip install mkdocs-autozip
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - autozip
   ```
</details>
<br>

## 🔧 Site building, site management

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://github.com/jimporter/mike">mike</a></b>  - 🥇29 ·  ⭐ 730 · <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Manage multiple versions of your MkDocs-powered documentation via Git.</summary>

- [GitHub](https://github.com/jimporter/mike) (👨‍💻 9 · 🔀 52 · 📥 500 · 📦 6.5K · 📋 200 - 6% open · ⏱️ 14.04.2026)
- [PyPi](https://pypi.org/project/mike) (📥 1.6M / month):
	```
	pip install mike
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - mike
   ```
</details>
<details><summary><b><a href="https://github.com/backstage/mkdocs-techdocs-core">techdocs-core</a></b>  - 🥇27 ·  ⭐ 110 · <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>The core MkDocs plugin used by Backstages TechDocs as a wrapper around multiple MkDocs plugins and Python Markdown..</summary>

- [GitHub](https://github.com/backstage/mkdocs-techdocs-core) (👨‍💻 51 · 🔀 79 · 📦 210 · ⏱️ 10.06.2026)
- [PyPi](https://pypi.org/project/mkdocs-techdocs-core) (📥 680K / month):
	```
	pip install mkdocs-techdocs-core
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - techdocs-core
   ```
</details>
<details><summary><b><a href="https://github.com/backstage/mkdocs-monorepo-plugin">monorepo</a></b>  - 🥇24 ·  ⭐ 390 · <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Build multiple documentation folders in a single Mkdocs. Designed for large codebases.</summary>

- [GitHub](https://github.com/backstage/mkdocs-monorepo-plugin) (👨‍💻 32 · 🔀 78 · 📦 670 · 📋 76 - 53% open · ⏱️ 15.06.2025)
- [PyPi](https://pypi.org/project/mkdocs-monorepo-plugin) (📥 1.6M / month):
	```
	pip install mkdocs-monorepo-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - monorepo
   ```
</details>
<details><summary><b><a href="https://github.com/jdoiro3/mkdocs-multirepo-plugin">mkdocs-multirepo-plugin</a></b>  - 🥈21 ·  ⭐ 190 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Build documentation in multiple repos into one site.</summary>

- [GitHub](https://github.com/jdoiro3/mkdocs-multirepo-plugin) (👨‍💻 17 · 🔀 60 · 📦 250 · 📋 120 - 52% open · ⏱️ 19.03.2026)
- [PyPi](https://pypi.org/project/mkdocs-multirepo-plugin) (📥 57K / month):
	```
	pip install mkdocs-multirepo-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - multirepo
   ```
</details>
<details><summary><b><a href="https://github.com/oprypin/mkdocs-same-dir">same-dir</a></b>  - 🥈21 ·  ⭐ 47 · 📈 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>ProperDocs plugin to allow placing mkdocs.yml in the same directory as documentation.</summary>

- [GitHub](https://github.com/oprypin/mkdocs-same-dir) (👨‍💻 3 · 🔀 3 · 📦 560 · 📋 9 - 22% open · ⏱️ 17.04.2026)
- [PyPi](https://pypi.org/project/mkdocs-same-dir) (📥 120K / month):
	```
	pip install mkdocs-same-dir
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - same-dir
   ```
</details>
<details><summary><b><a href="https://github.com/athackst/mkdocs-simple-plugin">simple</a></b>  - 🥈20 ·  ⭐ 51 · <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Build documentation files inside your code into a MkDocs site.</summary>

- [GitHub](https://github.com/athackst/mkdocs-simple-plugin) (👨‍💻 8 · 🔀 9 · 📦 63 · ⏱️ 22.05.2026)
- [PyPi](https://pypi.org/project/mkdocs-simple-plugin) (📥 37K / month):
	```
	pip install mkdocs-simple-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - simple
   ```
</details>
<details><summary><b><a href="https://github.com/ldeluigi/markdown-docs">markdown-docs</a></b>  - 🥈17 ·  ⭐ 27 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1448/PNG/32/42498factory_99134.png" style="display:inline;" width="13" height="13"></code><br>Action/docker image that transforms your markdown into a static website. No need for particular configuration: it just..</summary>

- [GitHub](https://github.com/ldeluigi/markdown-docs) (👨‍💻 6 · 🔀 6 · 📦 110 · ⏱️ 02.06.2026)
- [Docker Hub](https://hub.docker.com/r/deloo/markdown-docs) (📥 49K · ⏱️ 01.06.2026):
	```
	docker pull deloo/markdown-docs
	```
</details>
<details><summary><b><a href="https://github.com/mkdocs-publisher/mkdocs-publisher">Publisher for MkDocs - debugger</a></b>  - 🥈16 ·  ⭐ 130 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Advanced console and file logger from build and serve process.</summary>

- [GitHub](https://github.com/mkdocs-publisher/mkdocs-publisher) (👨‍💻 4 · 🔀 11 · 📥 140 · 📦 99 · 📋 31 - 25% open · ⏱️ 26.11.2025)
- [PyPi](https://pypi.org/project/mkdocs-publisher) (📥 3.5K / month):
	```
	pip install mkdocs-publisher
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - pub-debugger
   ```
</details>
<details><summary><b><a href="https://github.com/wilhelmer/mkdocs-multirepo">multirepo</a></b>  - 🥈13 ·  ⭐ 46 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code><br>A bit like monorepo, but keeps MkDocs projects separate.</summary>

- [GitHub](https://github.com/wilhelmer/mkdocs-multirepo) (👨‍💻 3 · 🔀 3 · 📦 3 · ⏱️ 04.01.2024)
- [PyPi](https://pypi.org/project/mkdocs-multirepo) (📥 380 / month):
	```
	pip install mkdocs-multirepo
	```
</details>
<details><summary><b><a href="https://github.com/zayd62/mkdocs-versioning">mkdocs-versioning</a></b>  - 🥈13 ·  ⭐ 40 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>A tool that allows for versioning sites built with mkdocs.</summary>

- [GitHub](https://github.com/zayd62/mkdocs-versioning) (👨‍💻 5 · 🔀 5 · 📦 180 · 📋 25 - 12% open · ⏱️ 01.08.2021)
- [PyPi](https://pypi.org/project/mkdocs-versioning):
	```
	pip install mkdocs-versioning
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - mkdocs-versioning
   ```
</details>
<details><summary><b><a href="https://github.com/ovasquez/mkdocs-merge">MkDocs Merge</a></b>  - 🥈13 ·  ⭐ 23 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code><br>Merge the source of multiple MkDocs sites into a single one.</summary>

- [GitHub](https://github.com/ovasquez/mkdocs-merge) (👨‍💻 3 · 🔀 5 · 📦 9 · 📋 10 - 50% open · ⏱️ 05.07.2025)
- [PyPi](https://pypi.org/project/mkdocs-merge) (📥 3K / month):
	```
	pip install mkdocs-merge
	```
</details>
<details><summary><b><a href="https://github.com/JonasDoesThings/mkdocs-exclude-unused-files">mkdocs-exclude-unused-files</a></b>  - 🥈13 ·  ⭐ 5 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Exclude orphaned (unused) static files from your mkdocs build.</summary>

- [GitHub](https://github.com/JonasDoesThings/mkdocs-exclude-unused-files) (👨‍💻 4 · 🔀 2 · 📥 12 · 📦 27 · 📋 4 - 25% open · ⏱️ 11.06.2025)
- [PyPi](https://pypi.org/project/mkdocs-exclude-unused-files) (📥 11K / month):
	```
	pip install mkdocs-exclude-unused-files
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - exclude-unused-files
   ```
</details>
<details><summary><b><a href="https://github.com/virtualguard101/mkdocs-note">mkdocs-note</a></b>  - 🥉8 ·  ⭐ 7 · <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>A MkDocs plugin to add note boxes to your documentation.</summary>

- [GitHub](https://github.com/virtualguard101/mkdocs-note) (👨‍💻 2 · 🔀 1 · 📋 19 - 15% open · ⏱️ 08.04.2026)
- [PyPi](https://pypi.org/project/mkdocs-note) (📥 520 / month):
	```
	pip install mkdocs-note
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - mkdocs-note
   ```
</details>
<details><summary><b><a href="https://github.com/JakubAndrysek/mkdocs-auto-refresh-build-pages">mkdocs-auto-refresh-build-pages</a></b>  - 🥉8 ·  ⭐ 3 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>MkDocs plugin that automatically refreshes the build pages when the documentation is updated.</summary>

- [GitHub](https://github.com/JakubAndrysek/mkdocs-auto-refresh-build-pages) (📦 6 · ⏱️ 06.07.2025)
- [PyPi](https://pypi.org/project/mkdocs-auto-refresh-build-pages) (📥 290 / month):
	```
	pip install mkdocs-auto-refresh-build-pages
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - auto-refresh-build-pages
   ```
</details>
<details><summary><b><a href="https://github.com/boozallen/mkdocs-yamp-plugin">mkdocs-yamp</a></b>  - 🥉8 ·  ⭐ 2 · 💤 · <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Yet Another Multirepo Plugin for MkDocs.</summary>

- [GitHub](https://github.com/boozallen/mkdocs-yamp-plugin) (👨‍💻 2 · 🔀 5 · 📦 7 · ⏱️ 10.10.2022)
- [PyPi](https://pypi.org/project/mkdocs-yamp) (📥 110 / month):
	```
	pip install mkdocs-yamp
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - yamp
   ```
</details>
<details><summary><b><a href="https://github.com/JonasDoesThings/mkdocs-exclude-tagged-files">mkdocs-exclude-tagged-files</a></b>  - 🥉7 ·  ⭐ 4 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>A mkdocs plugin for excluding files based on frontmatter tags.</summary>

- [GitHub](https://github.com/JonasDoesThings/mkdocs-exclude-tagged-files) (👨‍💻 2 · 🔀 2 · 📦 4 · ⏱️ 10.09.2023)
- [PyPi](https://pypi.org/project/mkdocs-exclude-tagged-files) (📥 290 / month):
	```
	pip install mkdocs-exclude-tagged-files
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - mkdocs_exclude_tagged_files
   ```
</details>
<details><summary><b><a href="https://github.com/unmc-vcr/mkdocs-required-frontmatter-plugin">mkdocs-required-frontmatter-plugin</a></b>  - 🥉7 ·  ⭐ 4 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>This MkDocs plugin enforces required frontmatter for documentation pages.</summary>

- [GitHub](https://github.com/unmc-vcr/mkdocs-required-frontmatter-plugin) (📦 2 · ⏱️ 22.03.2024)
- [PyPi](https://pypi.org/project/mkdocs-required-frontmatter-plugin) (📥 530 / month):
	```
	pip install mkdocs-required-frontmatter-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - required-frontmatter
   ```
</details>
<details><summary><b><a href="https://github.com/RDIL/mkdocs-plugin-progress">progress</a></b>  - 🥉6 ·  ⭐ 5 · <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>A plugin for MkDocs that lets you know exactly what is happening during the build.</summary>

- [GitHub](https://github.com/RDIL/mkdocs-plugin-progress) (👨‍💻 4 · 📦 41 · ⏱️ 22.04.2026)
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - progress
   ```
</details>
<details><summary><b><a href="https://github.com/kevin-411/mkdocs-new-features-notifier">mkdocs-new-features-notifier</a></b>  - 🥉6 ·  ⭐ 4 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>This plugin enables you to notify users of new features in your product. It does this by identifying new documentation..</summary>

- [GitHub](https://github.com/kevin-411/mkdocs-new-features-notifier) (👨‍💻 2 · 🔀 1 · ⏱️ 15.01.2020)
- [PyPi](https://pypi.org/project/mkdocs-new-features-notifier) (📥 1.3K / month):
	```
	pip install mkdocs-new-features-notifier
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - mkdocs-new-features-notifier
   ```
</details>
<details><summary><b><a href="https://github.com/leonardehrenfried/mkdocs-no-sitemap-plugin">no-sitemap</a></b>  - 🥉5 ·  ⭐ 3 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Disable Mkdocs sitemap generation.</summary>

- [GitHub](https://github.com/leonardehrenfried/mkdocs-no-sitemap-plugin) (👨‍💻 2 · 🔀 1 · 📦 54 · ⏱️ 23.08.2025)
- [PyPi](https://pypi.org/project/mkdocs-no-sitemap-plugin):
	```
	pip install mkdocs-no-sitemap-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - no-sitemap
   ```
</details>
<details><summary><b><a href="https://github.com/experimaestro/mkdocs-multiple">multiple</a></b>  - 🥉3 ·  ⭐ 2 · 💤 · <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Allows to merge mkdocs documentations dynamically.</summary>

- [GitHub](https://github.com/experimaestro/mkdocs-multiple) (👨‍💻 2 · ⏱️ 22.11.2019)
- [PyPi](https://pypi.org/project/mkdocs-multiple) (📥 800 / month):
	```
	pip install mkdocs-multiple
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - multiple
   ```
</details>
<details><summary><b><a href="https://github.com/octadocs/octadocs-adr">octadocs-adr</a></b>  - 🥉3 ·  ⭐ 1 · 💤 · <code>❗Unlicensed</code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>A blueprint for Architecture Decision Record in Octadocs - the smart documentation environment.</summary>

- [GitHub](https://github.com/octadocs/octadocs-adr) (⏱️ 22.08.2021)
- [PyPi](https://pypi.org/project/octadocs-adr) (📥 45 / month):
	```
	pip install octadocs-adr
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - octadocs_adr
   ```
</details>
<br>

## 📁 Snippets & includes (reusing contents)

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

<details><summary><b><a href="https://github.com/mondeja/mkdocs-include-markdown-plugin">include-markdown</a></b>  - 🥇27 ·  ⭐ 150 · <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Mkdocs Markdown includer plugin.</summary>

- [GitHub](https://github.com/mondeja/mkdocs-include-markdown-plugin) (👨‍💻 18 · 🔀 26 · 📥 710 · 📦 4K · 📋 100 - 0% open · ⏱️ 15.05.2026)
- [PyPi](https://pypi.org/project/mkdocs-include-markdown-plugin) (📥 590K / month):
	```
	pip install mkdocs-include-markdown-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - include-markdown
   ```
</details>
<details><summary><b><a href="https://github.com/cmacmackin/markdown-include">Markdown-Include</a></b>  - 🥈21 ·  ⭐ 120 · 💤 · <code><a href="http://bit.ly/2M0xdwT">❗️GPL-3.0</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1459/PNG/32/2799201-jigsaw-processing_99781.png" style="display:inline;" width="13" height="13"></code><br>Provides syntax for Python-Markdown which allows for the inclusion of the contents of other Markdown documents.</summary>

- [GitHub](https://github.com/cmacmackin/markdown-include) (👨‍💻 12 · 🔀 36 · 📦 8K · 📋 27 - 29% open · ⏱️ 07.02.2023)
- [PyPi](https://pypi.org/project/markdown-include) (📥 260K / month):
	```
	pip install markdown-include
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#markdown_extensions):
   ```yaml
   markdown_extensions:
     - markdown_include.include
   ```
</details>
<details><summary><b><a href="https://github.com/prcr/mkdocs-meta-descriptions-plugin">meta-descriptions</a></b>  - 🥈18 ·  ⭐ 20 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Generate meta descriptions from the first paragraphs in your MkDocs pages.</summary>

- [GitHub](https://github.com/prcr/mkdocs-meta-descriptions-plugin) (👨‍💻 3 · 🔀 2 · 📦 1.3K · 📋 12 - 8% open · ⏱️ 29.04.2026)
- [PyPi](https://pypi.org/project/mkdocs-meta-descriptions-plugin) (📥 18K / month):
	```
	pip install mkdocs-meta-descriptions-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - meta-descriptions
   ```
</details>
<details><summary><b><a href="https://github.com/rnorth/mkdocs-codeinclude-plugin">codeinclude</a></b>  - 🥈16 ·  ⭐ 18 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>A plugin to include code snippets into mkdocs pages.</summary>

- [GitHub](https://github.com/rnorth/mkdocs-codeinclude-plugin) (👨‍💻 5 · 🔀 6 · 📦 190 · 📋 12 - 41% open · ⏱️ 20.02.2026)
- [PyPi](https://pypi.org/project/mkdocs-codeinclude-plugin) (📥 48K / month):
	```
	pip install mkdocs-codeinclude-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - codeinclude
   ```
</details>
<details><summary><b><a href="https://github.com/fire1ce/mkdocs-embed-external-markdown">mkdocs-embed-external-markdown</a></b>  - 🥉15 ·  ⭐ 11 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>MkDocs Embed External Markdown plugin that allow to inject section or all full markdown content from a given url. The..</summary>

- [GitHub](https://github.com/fire1ce/mkdocs-embed-external-markdown) (👨‍💻 7 · 🔀 6 · 📦 180 · 📋 12 - 8% open · ⏱️ 24.02.2025)
- [PyPi](https://pypi.org/project/mkdocs-embed-external-markdown) (📥 10K / month):
	```
	pip install mkdocs-embed-external-markdown
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - external-markdown
   ```
</details>
<details><summary><b><a href="https://github.com/glennmatthews/markdown-version-annotations">markdown-version-annotations</a></b>  - 🥉12 ·  ⭐ 9 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1459/PNG/32/2799201-jigsaw-processing_99781.png" style="display:inline;" width="13" height="13"></code><br>MkDocs plugin to add custom admonitions for documenting version differences.</summary>

- [GitHub](https://github.com/glennmatthews/markdown-version-annotations) (📥 30 · 📦 98 · ⏱️ 06.05.2024)
- [PyPi](https://pypi.org/project/markdown-version-annotations) (📥 18K / month):
	```
	pip install markdown-version-annotations
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#markdown_extensions):
   ```yaml
   markdown_extensions:
     - markdown_version_annotations
   ```
</details>
<details><summary><b><a href="https://github.com/neurobin/mdx_include">Mdx Include</a></b>  - 🥉10 ·  ⭐ 63 · 💤 · <code>❗Unlicensed</code> · <code><img src="https://cdn.icon-icons.com/icons2/1459/PNG/32/2799201-jigsaw-processing_99781.png" style="display:inline;" width="13" height="13"></code><br>Python Markdown extension to include local or remote files.</summary>

- [GitHub](https://github.com/neurobin/mdx_include) (👨‍💻 3 · 🔀 3 · 📋 9 - 44% open · ⏱️ 26.07.2022)
- [PyPi](https://pypi.org/project/mdx-include) (📥 120K / month):
	```
	pip install mdx-include
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#markdown_extensions):
   ```yaml
   markdown_extensions:
     - mdx_include
   ```
</details>
<details><summary><b><a href="https://github.com/samcomi/mkdocs-gitsnippet-plugin">git snippet</a></b>  - 🥉10 ·  ⭐ 8 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>Mkdocs plugin that allow to inject snippet or all markdown content from a given remote git repository.</summary>

- [GitHub](https://github.com/samcomi/mkdocs-gitsnippet-plugin) (👨‍💻 4 · 🔀 4 · 📦 13 · ⏱️ 15.11.2020)
- [PyPi](https://pypi.org/project/mkdocs-gitsnippet-plugin) (📥 1.1K / month):
	```
	pip install mkdocs-gitsnippet-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - gitsnippet
   ```
</details>
<details><summary><b><a href="https://github.com/mprivat/mkdocs-snippet-plugin">snippet</a></b>  - 🥉8 ·  ⭐ 12 · 💤 · <code><a href="http://bit.ly/34MBwT8">MIT</a></code> · <code><img src="https://cdn.icon-icons.com/icons2/1465/PNG/32/701electricplug_100845.png" style="display:inline;" width="13" height="13"></code><br>An mkdocs plugin that injects snippets from a file in a git repository.</summary>

- [GitHub](https://github.com/mprivat/mkdocs-snippet-plugin) (👨‍💻 4 · 🔀 2 · 📦 23 · 📋 7 - 42% open · ⏱️ 21.10.2021)
- [PyPi](https://pypi.org/project/mkdocs-snippet-plugin) (📥 910 / month):
	```
	pip install mkdocs-snippet-plugin
	```
- Add to [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/#plugins):
   ```yaml
   plugins:
     - snippet
   ```
</details>

---

## Related Resources

- [**Best-of lists**](https://best-of.org): Discover other best-of lists with awesome open-source projects on all kinds of topics.

## Contribution

Contributions are encouraged and always welcome! If you like to add or update projects, choose one of the following ways:

- Open an issue by selecting one of the provided categories from the [issue page](https://github.com/mkdocs/catalog/issues/new/choose) and fill in the requested information.
- Modify the [projects.yaml](https://github.com/mkdocs/catalog/blob/main/projects.yaml) with your additions or changes, and submit a pull request. This can also be done directly via the [Github UI](https://github.com/mkdocs/catalog/edit/main/projects.yaml).

If you like to contribute to or share suggestions regarding the project metadata collection or markdown generation, please refer to the [best-of-generator](https://github.com/best-of-lists/best-of-generator) repository. If you like to create your own best-of list, we recommend to follow [this guide](https://github.com/best-of-lists/best-of/blob/main/create-best-of-list.md).

For more information on how to add or update projects, please read the [contribution guidelines](https://github.com/mkdocs/catalog/blob/main/CONTRIBUTING.md). By participating in this project, you agree to abide by its [Code of Conduct](https://github.com/mkdocs/catalog/blob/main/.github/CODE_OF_CONDUCT.md).

## License

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by-sa.svg)](https://creativecommons.org/licenses/by-sa/4.0/)
