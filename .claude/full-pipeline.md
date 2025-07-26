# Full Pipeline Command

Execute the complete 4-agent pipeline to build the physics-programmer portfolio from scratch.

## Pipeline Overview

This command orchestrates all four specialized agents in sequence to create a complete professional portfolio:

1. **Repository Scanner** → Discover and analyze Git repositories
2. **Project Classifier** → Categorize and assess project significance  
3. **Content Generator** → Create compelling portfolio content
4. **Site Builder** → Generate optimized static website

## Execution Sequence

### Phase 1: Repository Discovery (10-15 minutes)
Execute `/scan-repos` to discover all Git repositories in Documents folder and extract comprehensive metadata.

**Expected Output**: `repository-scan-results.json` with 15-30 repositories analyzed

### Phase 2: Project Classification (15-20 minutes)
Execute `/classify-projects` to categorize projects and assess portfolio significance.

**Expected Output**: `classified-projects.json` with projects organized by type and importance

### Phase 3: Content Generation (20-25 minutes)
Execute `/generate-content` to create compelling Pelican content from classified projects.

**Expected Output**: Professional portfolio content in `/content/` directory

### Phase 4: Site Building (10-15 minutes)
Execute `/build-site` to generate the final optimized static website.

**Expected Output**: Production-ready website in `/output/` directory

## Pipeline Configuration

### Environment Setup
- **PROJECT_ROOT**: `/Users/salim/Documents/github-profile/`
- **SCAN_PATH**: `/Users/salim/Documents/`
- **DATA_DIR**: `/Users/salim/Documents/github-profile/data/`
- **CONTENT_DIR**: `/Users/salim/Documents/github-profile/content/`
- **OUTPUT_DIR**: `/Users/salim/Documents/github-profile/output/`

### Quality Gates
Each phase includes validation to ensure pipeline integrity:
- **Phase 1 Gate**: Minimum 10 repositories discovered with metadata
- **Phase 2 Gate**: At least 70% of projects successfully classified
- **Phase 3 Gate**: All portfolio-worthy projects have generated content
- **Phase 4 Gate**: Website builds successfully with no critical errors

## Pipeline Execution

Execute the following agents in sequence with error handling and validation between phases:

### Agent 1: Repository Scanner
```
Command: /scan-repos
Configuration: Default settings for Documents folder scan
Success Criteria: repository-scan-results.json created with valid repository data
Error Handling: If scan fails, report issues and allow manual troubleshooting
```

### Agent 2: Project Classifier
```
Command: /classify-projects
Prerequisites: Successful completion of repository scanning
Configuration: Standard classification with EU research focus
Success Criteria: classified-projects.json created with project categorizations
Error Handling: If classification fails, allow partial results and continue
```

### Agent 3: Content Generator
```
Command: /generate-content
Prerequisites: Successful project classification
Configuration: Professional style, 6 featured projects, full category generation
Success Criteria: Complete portfolio content generated in content/ directory
Error Handling: If generation fails, preserve existing content and report issues
```

### Agent 4: Site Builder
```
Command: /build-site
Prerequisites: Content generation completed successfully
Configuration: Production build with optimization and validation
Success Criteria: Complete static website ready for deployment
Error Handling: If build fails, provide detailed error analysis and recovery options
```

## Success Criteria

### Pipeline Completion
- All four agents execute successfully
- Each phase produces required outputs
- Quality gates pass validation
- Final website is deployment-ready

### Output Validation
- **Repository Data**: Comprehensive metadata for discovered projects
- **Classifications**: Meaningful project categorization with confidence scores
- **Content Quality**: Professional, compelling portfolio content
- **Website Performance**: Fast, accessible, mobile-responsive site

### Performance Targets
- **Total Pipeline Time**: 55-75 minutes
- **Repository Discovery**: 15-30 valid repositories
- **Content Generation**: 10-20 project pages
- **Website Performance**: Lighthouse score >90

## Error Recovery

### Phase Failures
- **Scan Failure**: Check permissions, Git access, disk space
- **Classification Failure**: Allow partial results, manual review
- **Content Failure**: Preserve existing content, identify missing data
- **Build Failure**: Check configuration, dependencies, file structure

### Partial Success Handling
- Allow pipeline to continue with reduced scope
- Document any missing or failed components
- Provide recovery recommendations
- Generate status report with next steps

## Pipeline Status Reporting

Track overall pipeline execution and provide comprehensive status:

```json
{
  "pipeline_status": "COMPLETED|FAILED|PARTIAL",
  "execution_id": "uuid",
  "start_time": "iso8601",
  "end_time": "iso8601",
  "total_duration_minutes": 67.3,
  "phases": {
    "repository_scan": {
      "status": "COMPLETED",
      "duration_minutes": 12.5,
      "repositories_found": 23
    },
    "project_classification": {
      "status": "COMPLETED", 
      "duration_minutes": 18.2,
      "projects_classified": 21
    },
    "content_generation": {
      "status": "COMPLETED",
      "duration_minutes": 24.1,
      "pages_generated": 15
    },
    "site_building": {
      "status": "COMPLETED",
      "duration_minutes": 12.5,
      "lighthouse_score": 94
    }
  },
  "final_outputs": {
    "website_url": "file:///Users/salim/Documents/github-profile/output/index.html",
    "deployment_ready": true,
    "project_count": 15,
    "featured_projects": 6
  },
  "next_steps": [
    "Review generated content for accuracy",
    "Test website functionality",
    "Deploy to GitHub Pages",
    "Update portfolio regularly"
  ]
}
```

## Post-Pipeline Actions

After successful completion:
1. **Content Review**: Examine generated content for accuracy and completeness
2. **Website Testing**: Test all functionality, links, and responsive behavior
3. **Performance Validation**: Verify load times and accessibility scores
4. **Deployment**: Push to GitHub repository to trigger automatic deployment
5. **Monitoring Setup**: Configure analytics and performance monitoring

Execute this pipeline to generate a complete, professional physics-programmer portfolio from your existing projects.