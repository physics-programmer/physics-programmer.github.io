# Full Site Build Workflow

## Objective
Execute a complete physics-programmer portfolio site build from repository discovery through deployment-ready static site generation. This workflow orchestrates all specialized agents to create a professional, comprehensive portfolio showcasing current projects and research achievements.

## Prerequisites
- Access to `/Users/salim/Documents/` for repository scanning
- Pelican and dependencies installed
- Agent system prompts available in `/agents/` directory
- Empty or existing site structure in project directory

## Agent Execution Sequence

### Phase 1: Repository Discovery and Analysis
**Duration**: 10-15 minutes
**Agent**: Repository Scanner Agent

#### Objective
Discover all Git repositories in the Documents folder and extract comprehensive metadata for each project.

#### Execution
```bash
# Create data directory for agent outputs
mkdir -p data

# Execute Repository Scanner Agent
# This agent will scan /Users/salim/Documents recursively for Git repositories
# and generate structured data about each discovered project
```

**Agent Instructions**: Use the system prompt from `/agents/repository-scanner.md`

**Expected Outputs**:
- `data/repository-scan-results.json` - Complete repository inventory
- `data/scan-log.txt` - Scanning process log and statistics
- `data/discovered-repos.txt` - Simple list of found repositories

**Success Criteria**:
- All Git repositories in Documents folder discovered
- Complete metadata extracted for each repository
- Technology stacks identified accurately
- Activity levels assessed correctly

**Quality Checks**:
- Verify reasonable number of repositories found (expected: 15-30)
- Check that major known projects are included
- Validate metadata completeness for significant projects
- Confirm no permissions or access errors

---

### Phase 2: Project Classification and Contextualization
**Duration**: 15-20 minutes
**Agent**: Project Classifier Agent

#### Objective
Analyze repository data to classify projects by type (EU, internal, research, collaboration, personal) and assess professional significance.

#### Execution Prerequisites
- Repository scan results from Phase 1
- Agent has access to repository contents for detailed analysis

**Agent Instructions**: Use the system prompt from `/agents/project-classifier.md`

**Expected Outputs**:
- `data/classified-projects.json` - Enhanced repository data with classifications
- `data/classification-report.json` - Summary statistics and recommendations
- `data/evidence-log.txt` - Classification evidence and reasoning

**Success Criteria**:
- All projects assigned appropriate primary classifications
- High confidence scores for clear project types
- Evidence documented for classification decisions
- Portfolio organization recommendations generated

**Quality Checks**:
- Verify EU projects properly identified with funding evidence
- Check that research projects have academic indicators
- Validate collaboration projects show multi-party evidence
- Confirm classification confidence scores are reasonable

---

### Phase 3: Content Generation and Site Structure
**Duration**: 20-25 minutes
**Agent**: Content Generator Agent

#### Objective
Transform classified project data into compelling, professional Pelican-compatible content that showcases physics-programmer's achievements effectively.

#### Execution Prerequisites
- Classified project data from Phase 2
- Understanding of target audience and portfolio goals
- physics-programmer brand identity and professional context

**Agent Instructions**: Use the system prompt from `/agents/content-generator.md`

**Expected Outputs**:
- `content/index.md` - Homepage with featured projects and introduction
- `content/about.md` - Professional background and expertise overview
- `content/projects/` - Individual project pages organized by category
- `content/categories/` - Category overview pages (EU research, data science, etc.)
- `content/timeline.md` - Chronological project development timeline

**Success Criteria**:
- Compelling homepage that establishes professional credibility
- Individual project pages with appropriate technical depth
- Clear navigation structure and content organization
- Consistent professional tone throughout all content
- Proper Pelican metadata and formatting

**Quality Checks**:
- Verify all significant projects have dedicated pages
- Check that EU research projects are prominently featured
- Validate technical descriptions are accurate and comprehensive
- Confirm professional achievements are highlighted effectively
- Ensure consistent branding and voice across all content

---

### Phase 4: Site Building and Optimization
**Duration**: 10-15 minutes
**Agent**: Site Builder Agent

#### Objective
Generate optimized static site from content, prepare for deployment, and ensure performance and quality standards are met.

#### Execution Prerequisites
- Complete Pelican content structure from Phase 3
- Pelican configuration and theme files
- Build and optimization tools available

**Agent Instructions**: Use the system prompt from `/agents/site-builder.md`

**Expected Outputs**:
- `output/` - Complete static website ready for deployment
- `data/build-report.json` - Build statistics and performance metrics
- `data/deployment-packages/` - Platform-specific deployment configurations
- `docs/deployment-guide.md` - Instructions for hosting and maintenance

**Success Criteria**:
- Successful Pelican build with no errors
- Performance targets met (Lighthouse score >90)
- All content properly rendered and linked
- Deployment packages generated for multiple platforms
- Build documentation complete

**Quality Checks**:
- Verify all pages load correctly and navigation works
- Test responsive design across different screen sizes
- Validate performance metrics meet professional standards
- Check accessibility compliance (WCAG 2.1 AA)
- Confirm SEO optimization is complete

---

## Workflow Coordination

### Inter-Agent Data Flow
```
Repository Scanner → Project Classifier → Content Generator → Site Builder
        ↓                    ↓                   ↓               ↓
  scan-results.json → classified-projects.json → pelican-content → static-site
```

### Data Validation Points
1. **After Repository Scanning**: Verify expected repositories found
2. **After Classification**: Confirm reasonable distribution of project types
3. **After Content Generation**: Check content completeness and quality
4. **After Site Building**: Validate deployment-ready output

### Error Handling Strategy

#### Repository Scanner Failures
- **Insufficient Repositories**: Check scan path and permissions
- **Metadata Extraction Errors**: Verify Git repository integrity
- **Technology Detection Issues**: Review file pattern matching

#### Classifier Failures
- **Low Confidence Classifications**: Manual review of unclear projects
- **Missing Evidence**: Additional repository content analysis
- **Category Imbalances**: Verify classification criteria appropriate

#### Content Generator Failures
- **Missing Content**: Check data availability and template issues
- **Formatting Errors**: Validate Pelican metadata and markdown syntax
- **Incomplete Narratives**: Review project significance assessment

#### Site Builder Failures
- **Build Errors**: Check Pelican configuration and dependencies
- **Performance Issues**: Review optimization settings and asset sizes
- **Deployment Problems**: Verify platform configuration requirements

### Success Validation

#### Technical Validation
- [ ] All agents execute successfully without critical errors
- [ ] Data flows correctly between agent phases
- [ ] Final output meets technical specifications
- [ ] Performance benchmarks achieved

#### Content Validation
- [ ] Portfolio accurately represents physics-programmer's work
- [ ] Professional achievements prominently featured
- [ ] Technical expertise clearly demonstrated
- [ ] Research leadership and collaboration highlighted

#### Quality Validation
- [ ] Professional appearance suitable for career purposes
- [ ] Accessibility and usability standards met
- [ ] SEO optimization complete for discoverability
- [ ] Deployment readiness confirmed

## Execution Commands

### Manual Execution
Execute each agent individually using the Task tool:

```bash
# Phase 1: Repository Discovery
claude --task "Execute the Repository Scanner Agent using the system prompt from agents/repository-scanner.md. Scan /Users/salim/Documents for Git repositories and generate comprehensive metadata."

# Phase 2: Project Classification
claude --task "Execute the Project Classifier Agent using the system prompt from agents/project-classifier.md. Analyze the repository scan results and classify all projects."

# Phase 3: Content Generation
claude --task "Execute the Content Generator Agent using the system prompt from agents/content-generator.md. Create compelling Pelican content for the physics-programmer portfolio."

# Phase 4: Site Building
claude --task "Execute the Site Builder Agent using the system prompt from agents/site-builder.md. Generate the optimized static site and prepare deployment packages."
```

### Validation Commands
```bash
# Check build output
ls -la output/
find output -name "*.html" | wc -l

# Verify content structure
find content -name "*.md" | head -10

# Check data outputs
ls -la data/
cat data/build-report.json | jq '.build_summary'
```

## Timeline and Resources

### Expected Duration
- **Total Workflow Time**: 60-80 minutes
- **Agent Execution**: 55-75 minutes
- **Validation and Review**: 5-10 minutes

### Resource Requirements
- **Compute**: Moderate (repository analysis and site generation)
- **Storage**: ~50MB for intermediate data, ~100MB for final site
- **Network**: Minimal (local processing only)

### Scalability Considerations
- **Repository Count**: Optimized for 10-50 repositories
- **Content Volume**: Suitable for comprehensive portfolios
- **Build Complexity**: Supports advanced Pelican features and optimization

## Post-Workflow Actions

### Quality Review
1. **Manual Content Review**: Verify portfolio accuracy and completeness
2. **Technical Testing**: Test site functionality across browsers and devices
3. **Performance Validation**: Confirm speed and accessibility targets met
4. **Professional Assessment**: Ensure content supports career objectives

### Deployment Preparation
1. **Platform Selection**: Choose appropriate hosting service
2. **Domain Configuration**: Set up custom domain if required
3. **Analytics Setup**: Implement tracking and monitoring
4. **Backup Strategy**: Establish content and configuration backups

### Maintenance Planning
1. **Update Schedule**: Plan regular content refreshes
2. **Monitoring Setup**: Track site performance and user engagement
3. **Content Evolution**: Plan for adding new projects and achievements
4. **Technical Maintenance**: Keep dependencies and tools updated

## Success Metrics

### Quantitative Metrics
- Build completion rate: 100%
- Page load speed: <3 seconds
- Lighthouse performance score: >90
- Content coverage: 100% of significant projects
- Zero broken links or missing assets

### Qualitative Metrics
- Professional appearance and credibility
- Clear demonstration of expertise and achievements
- Effective storytelling and project presentation
- Strong foundation for career advancement and collaboration opportunities

This workflow represents a complete, professional portfolio generation process that leverages AI agents for intelligent content creation while maintaining high standards for technical quality and professional presentation.