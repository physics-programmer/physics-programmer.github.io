# /build-site - Static Site Generation and Optimization

## Purpose
Generate and optimize the final portfolio website using Pelican with performance optimization, SEO enhancement, and deployment preparation.

## Usage
```
/build-site [--content-dir PATH] [--output-dir PATH] [--build-mode MODE] [--optimize] [--validate] [--verbose]
```

## Arguments
- `--content-dir PATH` - Content directory path (default: content/)
- `--output-dir PATH` - Output directory for generated site (default: output/)
- `--build-mode MODE` - Build mode: development, production (default: production)
- `--optimize` - Enable asset optimization and compression
- `--validate` - Validate HTML, links, and SEO after build
- `--verbose` - Show detailed build progress

## Implementation

### 1. Environment Validation
- Verify Python virtual environment and Pelican installation
- Check Pelican configuration files (pelicanconf.py, publishconf.py)
- Validate theme availability and configuration
- Initialize build tracking with TodoWrite

### 2. Content Validation
- Verify all required content files exist in content directory
- Check Pelican metadata completeness for all content files
- Validate internal links and references
- Ensure proper content organization and structure

### 3. Pelican Build Process
Execute Pelican static site generation:
- Use Bash to run Pelican build commands
- Apply production configuration for optimization
- Generate all static pages, categories, and navigation
- Process themes and static assets

### 4. Asset Optimization
Optimize generated assets for performance:
- Compress images and media files
- Minify CSS and JavaScript files
- Optimize fonts and static resources
- Generate responsive image variants if needed

### 5. Quality Assurance
Validate generated website:
- HTML syntax validation using standard tools
- Internal link checking and validation
- SEO element verification (meta tags, structured data)
- Mobile responsiveness testing
- Performance benchmarking

### 6. Deployment Preparation
Prepare website for deployment:
- Validate all generated files and directory structure
- Create deployment-ready package
- Generate sitemap.xml and robots.txt if not present
- Verify GitHub Pages compatibility

## Output Files
- `output/` - Complete static website ready for deployment
- `build-report.json` - Detailed build statistics and performance metrics
- `build-log.txt` - Comprehensive build process log
- `validation-report.json` - Quality assurance and validation results

## Execution Flow

### Initialization Phase
1. **Validate Arguments**: Parse command arguments and apply defaults
2. **Check Prerequisites**: Verify Pelican installation and content availability
3. **Setup Environment**: Activate virtual environment and verify dependencies
4. **Progress Tracking**: Initialize TodoWrite for build progress

### Pre-Build Phase
1. **Content Validation**: Verify all content files exist and have valid metadata
2. **Configuration Check**: Validate Pelican configuration files
3. **Theme Verification**: Check theme availability and compatibility
4. **Clean Output**: Remove previous build artifacts if regenerating

### Build Phase
1. **Pelican Execution**: Run Pelican build with production configuration
2. **Asset Processing**: Optimize images, CSS, JavaScript, and other assets
3. **Theme Application**: Apply theme styling and layout
4. **Static File Processing**: Copy and optimize static resources

### Optimization Phase
1. **Performance Optimization**: Compress assets and optimize loading
2. **SEO Enhancement**: Validate meta tags, structured data, sitemap
3. **Accessibility Check**: Verify WCAG compliance and responsive design
4. **Link Validation**: Check all internal and external links

### Validation Phase
1. **HTML Validation**: Verify markup compliance and syntax
2. **Performance Testing**: Measure load times and performance metrics
3. **Mobile Testing**: Validate responsive design and mobile compatibility
4. **Deployment Validation**: Ensure GitHub Pages compatibility

### Output Phase
1. **Report Generation**: Create build-report.json with statistics
2. **Log Documentation**: Generate comprehensive build-log.txt
3. **Validation Report**: Create validation-report.json with QA results
4. **Summary Display**: Show build summary and next steps

## Error Handling
- **Missing Content**: Graceful handling when content files unavailable
- **Build Failures**: Continue with partial builds when possible
- **Asset Errors**: Skip problematic assets with warnings
- **Validation Failures**: Report issues without stopping deployment preparation

## Success Criteria
- Complete static website generated successfully
- All content properly rendered with correct formatting
- Performance targets met (load time <3s, Lighthouse >90)
- HTML validation passing with minimal warnings
- All internal links functional and verified
- Mobile responsive design working across devices
- Ready for immediate GitHub Pages deployment

## Examples
```bash
# Basic site build with defaults
/build-site

# Development build without optimization
/build-site --build-mode development --verbose

# Production build with full optimization and validation
/build-site --optimize --validate --verbose

# Custom directories with optimization
/build-site --content-dir ./custom-content --output-dir ./custom-output --optimize
```

This command generates a complete, optimized static website ready for professional deployment.