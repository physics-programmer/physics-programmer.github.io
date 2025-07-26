# Build Site Command

Execute the Site Builder Agent to generate and optimize the final portfolio website.

## Command Configuration

**Agent**: Site Builder  
**Prompt Source**: `/Users/salim/Documents/github-profile/agents/site-builder.md`  
**Input**: Pelican content from Content Generator Agent  
**Output Directory**: `/Users/salim/Documents/github-profile/output/`

## Execution Parameters

### Default Configuration
- **CONTENT_DIR**: `/Users/salim/Documents/github-profile/content/`
- **OUTPUT_DIR**: `/Users/salim/Documents/github-profile/output/`
- **BUILD_MODE**: production
- **OPTIMIZATION_LEVEL**: standard
- **VALIDATE_OUTPUT**: true

### Build Configuration
- **PELICAN_CONFIG**: `/Users/salim/Documents/github-profile/publishconf.py`
- **THEME_PATH**: `/Users/salim/Documents/github-profile/themes/physics-programmer/`
- **STATIC_OPTIMIZATION**: true
- **SEO_VALIDATION**: true

### Environment Setup
- **PROJECT_ROOT**: `/Users/salim/Documents/github-profile/`
- **VENV_PATH**: `/Users/salim/Documents/github-profile/.venv/`

## Agent Execution

You are the Site Builder Agent for the physics-programmer portfolio project. Load your complete system prompt from `/Users/salim/Documents/github-profile/agents/site-builder.md` and execute it with the following configuration:

### Configuration
```json
{
  "CONTENT_DIR": "/Users/salim/Documents/github-profile/content/",
  "OUTPUT_DIR": "/Users/salim/Documents/github-profile/output/",
  "BUILD_MODE": "production",
  "OPTIMIZATION_LEVEL": "standard",
  "VALIDATE_OUTPUT": true,
  "PELICAN_CONFIG": "/Users/salim/Documents/github-profile/publishconf.py",
  "THEME_PATH": "/Users/salim/Documents/github-profile/themes/physics-programmer/",
  "STATIC_OPTIMIZATION": true,
  "SEO_VALIDATION": true,
  "PROJECT_ROOT": "/Users/salim/Documents/github-profile/",
  "VENV_PATH": "/Users/salim/Documents/github-profile/.venv/"
}
```

### Mission Objectives
1. **Site Building**: Generate optimized static website using Pelican
2. **Asset Optimization**: Compress images, minify CSS/JS, optimize performance
3. **SEO Enhancement**: Validate SEO elements, structured data, accessibility
4. **Quality Assurance**: Validate all links, check responsive design
5. **Deployment Preparation**: Ensure site is ready for GitHub Pages deployment

### Build Process
1. **Environment Setup**: Activate virtual environment and verify dependencies
2. **Content Validation**: Check all required content files exist and are valid
3. **Pelican Build**: Execute production build with optimizations
4. **Asset Processing**: Optimize images, fonts, and static resources
5. **Quality Checks**: Validate HTML, check links, test responsive design
6. **Performance Analysis**: Measure load times, accessibility scores
7. **Deployment Package**: Prepare final output for GitHub Pages

### Required Outputs
- `output/` - Complete static website ready for deployment
- `build-report.json` - Detailed build statistics and performance metrics
- `build-log.txt` - Comprehensive build process log
- `validation-report.json` - Quality assurance and validation results

### Success Criteria
- Successfully generated static website with all content
- All links functional and accessible
- Responsive design working across devices
- Performance metrics meeting professional standards
- SEO optimization and accessibility compliance
- Ready for immediate GitHub Pages deployment

### Prerequisite Check
Verify that:
- Content directory contains generated portfolio content
- Virtual environment is properly set up
- Pelican configuration is valid
- Theme files are accessible

If content is missing, recommend running `/generate-content` first.

### Tools Available
- **Bash**: Pelican build commands, file operations, optimization tools
- **Read**: Examining configuration files and validating content
- **Write**: Creating build reports and logs
- **LS**: Verifying output structure and file presence

### Performance Targets
- **Load Time**: <3 seconds on 3G networks
- **Lighthouse Score**: >90 for Performance, Accessibility, SEO
- **Mobile Responsive**: 100% compatibility across devices
- **HTML Validation**: W3C compliant markup
- **Broken Links**: Zero broken internal links

### Quality Assurance
Execute comprehensive validation including:
- HTML/CSS syntax validation
- Link checking (internal and external)
- Image optimization verification
- Mobile responsiveness testing
- SEO element validation
- Accessibility compliance (WCAG 2.1 AA)
- Performance benchmarking

Execute this systematically to produce a professional, optimized portfolio website and provide structured status reporting as defined in your agent prompt.