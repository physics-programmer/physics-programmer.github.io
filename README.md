# Physics-Programmer Portfolio

Source repository for the `physics-programmer.github.io` personal portfolio and CV.

## What Lives Here

- `content/`: Pelican Markdown content for the personal site.
- `themes/physics-programmer/`: custom Pelican theme.
- `pelicanconf.py`: local/development Pelican settings.
- `publishconf-simple.py`: production settings used by GitHub Actions.
- `.github/workflows/deploy.yml`: GitHub Pages deployment workflow.
- `cv/overleaf/`: canonical LaTeX CV source.
- `cv/works.bib`: publication and patent bibliography source.

Generated site output is not source. `output/`, caches, logs, and CV build outputs are ignored.

## Setup

```bash
uv venv .venv
source .venv/bin/activate
uv pip install -r requirements-minimal.txt
```

## Build The Site

Use the same environment shape as CI:

```bash
PYTHONPATH=$PWD .venv/bin/pelican content -s publishconf-simple.py
```

For a disposable local check:

```bash
PYTHONPATH=$PWD .venv/bin/pelican content -s publishconf-simple.py -o /tmp/github-profile-output-check
```

## Build The CV

```bash
cd cv/overleaf
tectonic resume.tex --outdir build
```

The local PDF is written to `cv/overleaf/build/resume.pdf`.

## Deployment

Pushing to `main` runs `.github/workflows/deploy.yml`, builds the Pelican site into `output/`, and deploys that artifact to GitHub Pages.

Do not commit generated HTML directories such as `output/`, `archives/`, `category/`, `tag/`, `projects/`, or `theme/` once the source-based workflow has been verified on GitHub Actions.
