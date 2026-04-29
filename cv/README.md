# CV

This directory keeps one canonical CV source and separates private inputs from generated outputs.

## Canonical source

- `cv/overleaf/resume.tex`: main LaTeX entry point for the template-quality CV.
- `cv/overleaf/_header.tex`: header/contact layout.
- `cv/overleaf/TLCresume.sty`: template styling.
- `cv/overleaf/sections/`: CV content sections.
- `cv/overleaf/salim.jpg`: portrait used by the CV.
- `cv/works.bib`: bibliography/reference source for publications and patents.

## Local-only files

These are ignored by git:

- `cv/sources/`: LinkedIn and ORCID source dumps used to update the CV.
- `cv/outputs/`: generated PDFs.
- `cv/overleaf/build/`: local LaTeX build output.

## Build

From the repo root:

```bash
cd cv/overleaf
tectonic resume.tex --outdir build
```

The generated PDF is:

```text
cv/overleaf/build/resume.pdf
```

For Overleaf, upload the contents of `cv/overleaf/` and set `resume.tex` as the main file.
