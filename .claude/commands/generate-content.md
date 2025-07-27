# /generate-content - Portfolio Content Generation

## Purpose
Create compelling Pelican-compatible portfolio content from classified project data with professional presentation and SEO optimization.

## Usage
```
/generate-content [--input-file PATH] [--output-dir PATH] [--style STYLE] [--featured-count N] [--language LANG] [--regenerate]
```

## Arguments
- `--input-file PATH` - Classified projects file (default: data/classified-projects.json)
- `--output-dir PATH` - Content output directory (default: content/)
- `--style STYLE` - Content style: professional, academic, technical (default: professional)
- `--featured-count N` - Number of featured projects for homepage (default: 6)
- `--language LANG` - Content language code (default: en)
- `--regenerate` - Regenerate all content even if existing

## Implementation

### 1. Input Processing
- Read and validate classified projects data
- Filter projects based on portfolio inclusion criteria
- Sort projects by significance and contribution level
- Initialize content generation tracking with TodoWrite

### 2. Content Strategy
Apply professional content filtering:
- **Include Only**: EU_FUNDED_RESEARCH, PROFESSIONAL_COLLABORATION projects
- **Emphasize**: Projects with ≥20% author contribution
- **Exclude**: Personal projects, internal tools, learning exercises
- **Prioritize**: Projects demonstrating professional expertise and leadership

### 3. Homepage Generation
Create compelling homepage (content/index.md):
- Professional introduction highlighting research and technical expertise
- Featured projects showcase (6 highest-scoring projects)
- Clear value proposition for potential collaborators and employers
- SEO-optimized content with proper metadata

### 4. Project Pages Creation
Generate individual project pages (content/projects/*.md):
- Detailed project descriptions emphasizing user contributions
- Technology stack and implementation details
- Collaboration context and institutional affiliations
- Professional outcomes and achievements
- Proper Pelican metadata for categorization

### 5. Category Organization
Create category pages (content/categories/*.md):
- EU Research category showcasing European collaboration leadership
- Professional Collaboration highlighting commercial and institutional work
- Clear navigation and project grouping
- SEO optimization for professional discovery

### 6. Professional Branding
Establish consistent professional voice:
- **Tone**: Scientific, research-oriented, collaborative
- **Audience**: EU project evaluators, research partners, potential employers
- **Focus**: Computational research expertise and international collaboration
- **Positioning**: Senior research and leadership roles in European context

## Output Files
- `content/index.md` - Professional homepage with featured projects
- `content/projects/*.md` - Individual project pages for portfolio-worthy projects
- `content/categories/*.md` - Category pages for project organization
- `content/about.md` - Professional background and expertise summary
- `content-generation-log.txt` - Detailed generation process documentation

## Execution Flow

### Initialization Phase
1. **Validate Arguments**: Parse command arguments and apply defaults
2. **Check Prerequisites**: Verify classified projects file exists and is valid
3. **Setup Output**: Create content directory structure and initialize logging
4. **Progress Tracking**: Initialize TodoWrite for content generation progress

### Content Planning Phase
1. **Load Classifications**: Read and parse classified projects data
2. **Apply Filters**: Filter for portfolio-worthy projects only
3. **Content Strategy**: Plan homepage, project pages, and category organization
4. **Template Selection**: Choose content templates based on project types

### Content Creation Phase
1. **Homepage Generation**: Create professional homepage with featured projects
2. **Project Pages**: Generate individual project pages with emphasis on contributions
3. **Category Pages**: Create category organization pages
4. **About Page**: Generate or update professional background page
5. **Metadata Optimization**: Add Pelican metadata and SEO optimization

### Quality Assurance Phase
1. **Content Validation**: Verify all required content files generated
2. **Metadata Check**: Validate Pelican metadata for each content file
3. **Link Verification**: Check internal links and references
4. **SEO Optimization**: Verify meta descriptions, titles, and keywords

### Output Phase
1. **File Writing**: Write all content files with proper Pelican formatting
2. **Log Generation**: Create detailed content-generation-log.txt
3. **Summary Report**: Provide content generation summary
4. **Next Steps**: Recommend site building with generated content

## Error Handling
- **Missing Input**: Graceful handling when classified projects unavailable
- **Invalid Data**: Skip malformed project entries with warnings
- **Template Errors**: Fallback to basic templates when advanced formatting fails
- **File Writing**: Validate file creation and provide error recovery

## Success Criteria
- Professional content showcasing expertise and achievements
- Clear project categorization and navigation structure
- Consistent branding and professional tone throughout
- SEO-optimized content with proper Pelican metadata
- All content files ready for static site generation

## Examples
```bash
# Basic content generation with defaults
/generate-content

# Generate content with academic style
/generate-content --style academic --featured-count 8

# Regenerate all content with custom input
/generate-content --input-file ./custom-classifications.json --regenerate

# Generate content for specific language
/generate-content --language fr --style professional
```

This command transforms classified project data into compelling, professional portfolio content optimized for static site generation and professional presentation.