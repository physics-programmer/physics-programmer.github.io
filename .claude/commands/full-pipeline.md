# /full-pipeline - Complete Portfolio Generation Pipeline

## Purpose
Execute the complete 4-command pipeline to build the physics-programmer portfolio from scratch with comprehensive validation and quality gates.

## Usage
```
/full-pipeline [--project-root PATH] [--scan-path PATH] [--featured-count N] [--validate-all] [--verbose]
```

## Arguments
- `--project-root PATH` - Project root directory (default: current directory)
- `--scan-path PATH` - Directory to scan for repositories (default: /Users/salim/Documents/)
- `--featured-count N` - Number of featured projects (default: 6)
- `--validate-all` - Enable comprehensive validation at each phase
- `--verbose` - Show detailed progress from all pipeline commands

## Pipeline Overview

Orchestrates four specialized commands in sequence:

1. **Portfolio Framework** → Initialize project structure and validate environment
2. **Repository Scanner** → Discover and analyze Git repositories
3. **Project Classifier** → Categorize and assess project significance  
4. **Content Generator** → Create compelling portfolio content
5. **Site Builder** → Generate optimized static website

## Implementation

### 1. Pipeline Initialization
- Validate pipeline arguments and set defaults
- Initialize comprehensive TodoWrite tracking for all phases
- Check system prerequisites and dependencies
- Create execution plan and estimated timeline

### 2. Phase Execution with Quality Gates
Execute each command in sequence with validation:

**Phase 1: Framework Setup (2-3 minutes)**
- Execute `/portfolio-framework` with project root validation
- Verify directory structure and dependencies
- Quality Gate: Environment ready for pipeline execution

**Phase 2: Repository Discovery (10-15 minutes)**
- Execute `/scan-repos` with specified scan path
- Discover and analyze all Git repositories
- Quality Gate: Minimum 10 repositories with valid metadata

**Phase 3: Project Classification (15-20 minutes)**
- Execute `/classify-projects` on scan results
- Categorize and assess project significance
- Quality Gate: 70% of projects successfully classified

**Phase 4: Content Generation (20-25 minutes)**
- Execute `/generate-content` from classifications
- Create professional portfolio content
- Quality Gate: All portfolio-worthy projects have content

**Phase 5: Site Building (10-15 minutes)**
- Execute `/build-site` with production optimization
- Generate final static website
- Quality Gate: Website builds successfully with validation

### 3. Inter-Command Data Flow
Manage data dependencies between commands:
- Pass arguments and configuration between pipeline phases
- Validate output files before proceeding to next phase
- Handle partial failures with graceful degradation
- Maintain execution state for recovery and resumption

### 4. Progress Tracking and Reporting
- Real-time progress updates for entire pipeline
- Phase-specific progress within each command
- Estimated completion times and performance metrics
- Comprehensive error handling and recovery guidance

## Execution Flow

### Initialization Phase
1. **Validate Arguments**: Parse pipeline arguments and validate prerequisites
2. **System Check**: Verify all required tools and dependencies available
3. **Plan Generation**: Create execution plan with time estimates
4. **Progress Setup**: Initialize comprehensive TodoWrite tracking

### Pipeline Execution
Execute commands in sequence with comprehensive error handling:

**Command 1: /portfolio-framework**
- Initialize project structure and validate environment
- Success Criteria: All directories created, dependencies verified
- Error Handling: Fix permission/dependency issues before continuing

**Command 2: /scan-repos**
- Discover repositories in specified scan path
- Success Criteria: repository-scan-results.json with valid data
- Error Handling: Continue with partial results, report inaccessible repos

**Command 3: /classify-projects**
- Categorize discovered repositories
- Success Criteria: classified-projects.json with confidence scores
- Error Handling: Allow partial classifications, flag low-confidence items

**Command 4: /generate-content**
- Create professional portfolio content
- Success Criteria: Complete content directory with all required files
- Error Handling: Preserve existing content, generate with available data

**Command 5: /build-site**
- Generate optimized static website
- Success Criteria: Production-ready website in output directory
- Error Handling: Provide detailed build analysis and recovery options

### Validation Phase
1. **Quality Gates**: Verify each phase meets success criteria before continuing
2. **Data Validation**: Check file completeness and format compliance
3. **Error Recovery**: Handle failures with fallback strategies
4. **Progress Updates**: Maintain real-time status throughout pipeline

### Completion Phase
1. **Final Validation**: Comprehensive check of all outputs
2. **Performance Metrics**: Collect and report pipeline performance
3. **Summary Report**: Generate complete execution summary
4. **Next Steps**: Provide deployment guidance and recommendations

## Output Files
- `data/repository-scan-results.json` - Repository discovery results
- `data/classified-projects.json` - Project classifications
- `content/` - Complete portfolio content directory
- `output/` - Production-ready website
- `logs/pipeline-execution.log` - Complete pipeline execution log
- `pipeline-summary.json` - Execution summary with performance metrics

## Error Handling
- **Command Failures**: Continue pipeline with degraded functionality when possible
- **Data Issues**: Handle missing or corrupted data gracefully
- **Dependency Problems**: Provide clear guidance for resolution
- **Partial Success**: Complete pipeline with available data and report limitations

## Success Criteria
- All five commands execute with acceptable results
- Quality gates pass validation at each phase
- Final website generated and deployment-ready
- Comprehensive documentation and logs created
- Performance targets met (total time 60-80 minutes)

## Performance Targets
- **Total Pipeline Time**: 60-80 minutes
- **Repository Discovery**: 15-30 valid repositories
- **Content Generation**: 10-20 project pages
- **Website Performance**: Lighthouse score >90, load time <3s

## Examples
```bash
# Basic pipeline execution with defaults
/full-pipeline

# Pipeline with custom scan path and validation
/full-pipeline --scan-path /path/to/projects --validate-all

# Verbose pipeline with custom project root
/full-pipeline --project-root /custom/portfolio --verbose

# Pipeline with specific featured project count
/full-pipeline --featured-count 8 --validate-all --verbose
```

## Post-Pipeline Actions

After successful completion:
1. **Content Review**: Examine generated content for accuracy and completeness
2. **Website Testing**: Test all functionality, links, and responsive behavior
3. **Performance Validation**: Verify load times and accessibility scores
4. **Deployment**: Push to GitHub repository to trigger automatic deployment
5. **Monitoring Setup**: Configure analytics and performance monitoring

This pipeline generates a complete, professional physics-programmer portfolio from existing projects with comprehensive validation and optimization.