# Physics-Programmer Portfolio

Professional portfolio website showcasing computational research and European collaboration projects.

## 🌟 Features

- **AI-Driven Content**: Automated project discovery and content generation using specialized agents
- **Professional Design**: Modern, responsive portfolio optimized for research professionals
- **Automated Deployment**: GitHub Actions pipeline for seamless updates
- **Research Focus**: Highlighting EU research projects, academic collaborations, and computational expertise

## 🏗️ Architecture

### Agent-Driven Content Pipeline
- **Repository Scanner Agent**: Discovers Git repositories and extracts metadata
- **Project Classifier Agent**: Categorizes projects by type (EU Research, Academic, etc.)
- **Content Generator Agent**: Creates compelling project narratives
- **Site Builder Agent**: Generates optimized static site

### Technology Stack
- **Static Site Generator**: Pelican (Python)
- **Hosting**: GitHub Pages
- **Deployment**: GitHub Actions with uv for fast Python builds
- **Theme**: Custom responsive design optimized for research portfolios

## 🚀 Development

### Setup
```bash
# Clone repository
git clone https://github.com/physics-programmer/physics-programmer.github.io
cd physics-programmer.github.io

# Create virtual environment with uv
uv venv .venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

### Local Development
```bash
# Build site
pelican content

# Development server
pelican --listen

# Production build
pelican content -s publishconf.py
```

### Content Updates
```bash
# Run agent workflow to update content
# (Execute agents in workflows/full-site-build.md)

# Commit and push (triggers auto-deployment)
git add .
git commit -m "Update portfolio content"
git push origin main
```

## 📁 Project Structure

```
├── agents/                     # AI agent system prompts
│   ├── repository-scanner.md
│   ├── project-classifier.md
│   ├── content-generator.md
│   └── site-builder.md
├── content/                    # Pelican content
├── themes/physics-programmer/  # Custom theme
├── workflows/                  # Agent orchestration
├── data/                      # Agent outputs
└── output/                    # Generated site
```

## 🔧 Configuration

- **Development**: `pelicanconf.py`
- **Production**: `publishconf.py` 
- **Deployment**: `.github/workflows/deploy.yml`

## 📊 Deployment

The site automatically deploys to GitHub Pages when changes are pushed to the main branch:

1. **GitHub Actions** builds the site using uv and Pelican
2. **Optimized output** is deployed to GitHub Pages
3. **Live site** available at `https://physics-programmer.github.io`

## 🎯 Professional Use

This portfolio is designed for:
- Academic researchers and computational scientists
- EU research project principal investigators
- Software engineering professionals in research
- Open source contributors and collaborators

## 📄 License

MIT License - See [LICENSE](LICENSE) for details.

---

**Built with AI agents and modern web technologies** | **Optimized for research professionals**