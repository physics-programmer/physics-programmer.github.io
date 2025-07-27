# /update-portfolio - Incremental Portfolio Updates

## Purpose
Provide smart incremental updates to maintain current portfolio content without full pipeline regeneration.

## Usage
```
/update-portfolio [--mode MODE] [--force] [--check-changes] [--content-age-days N] [--verbose]
```

## Arguments
- `--mode MODE` - Update mode: quick, standard, full (default: standard)
- `--force` - Force update ignoring change detection
- `--check-changes` - Only check for changes without updating
- `--content-age-days N` - Content refresh threshold in days (default: 30)
- `--verbose` - Show detailed update analysis and progress

## Update Strategy

Smart incremental updates with change detection:

1. **Change Detection**: Identify new or modified repositories since last update
2. **Selective Processing**: Update only changed components
3. **Content Refresh**: Regenerate content for updated projects
4. **Optimized Building**: Fast rebuild with change detection

## Update Modes

### Quick Update (5-10 minutes)
- Scan for new repositories only
- Update existing project metadata if significantly changed
- Regenerate homepage and navigation
- Fast site rebuild without full optimization

### Standard Update (15-20 minutes)  
- Full repository scan with intelligent change detection
- Reclassify projects with low confidence scores or significant changes
- Update content for modified projects and new discoveries
- Complete site rebuild with production optimization

### Full Refresh (60-80 minutes)
- Complete pipeline execution (equivalent to `/full-pipeline`)
- Use when major changes, troubleshooting, or comprehensive refresh needed

## Implementation

### 1. State Analysis
- Load previous execution results and timestamps
- Compare current repository state with last scan
- Identify changes requiring updates (new repos, commits, README changes)
- Calculate update scope and estimated execution time

### 2. Change Detection
Intelligent analysis of what needs updating:
- **New Repositories**: Repositories created since last scan
- **Modified Repositories**: Significant changes (>10 commits, README updates)
- **Stale Content**: Content older than threshold (default: 30 days)
- **Low Confidence Classifications**: Scores below 0.8 requiring review

### 3. Selective Command Execution
Execute only necessary commands based on detected changes:
- **Repository Scanner**: Process new/changed repositories only
- **Project Classifier**: Reclassify flagged or new projects
- **Content Generator**: Update content for affected projects
- **Site Builder**: Optimized rebuild with change detection

### 4. Progress Tracking and Optimization
- Initialize TodoWrite for update progress tracking
- Execute updates in parallel when possible
- Reuse unchanged data and content from cache
- Validate updates and provide comprehensive reporting

## Execution Flow

### Initialization Phase
1. **Validate Arguments**: Parse update mode and options
2. **Load Previous State**: Read last execution results and timestamps
3. **Change Analysis**: Compare current state with previous scan
4. **Update Planning**: Determine scope and create execution plan

### Change Detection Phase
1. **Repository Changes**: Identify new, modified, or removed repositories
2. **Content Staleness**: Check content age against refresh thresholds
3. **Classification Review**: Find low-confidence classifications needing review
4. **Impact Assessment**: Determine which components need updating

### Selective Update Phase
1. **Conditional Scanning**: Run repository scan only if new/changed repos found
2. **Targeted Classification**: Reclassify only flagged or new projects
3. **Content Updates**: Regenerate content for affected projects only
4. **Optimized Building**: Fast rebuild focusing on changed components

### Validation Phase
1. **Update Verification**: Verify all changes applied correctly
2. **Quality Checks**: Validate updated content and website functionality
3. **Performance Testing**: Ensure updates don't degrade performance
4. **Report Generation**: Create comprehensive update summary

## Output Files
- `data/update-analysis.json` - Change detection and impact analysis
- `data/update-results.json` - Summary of updates applied
- `logs/update-log.txt` - Detailed update process log
- `update-summary.json` - Complete update summary with performance metrics

## Error Handling
- **Change Detection Failures**: Continue with manual fallback options
- **Partial Updates**: Complete available updates and report failures
- **State Corruption**: Detect inconsistencies and provide recovery options
- **Rollback Capability**: Restore previous state if major issues occur

## Success Criteria
- Accurate change detection with minimal false positives
- Significant time savings compared to full pipeline execution
- No loss of existing quality content during updates
- All new projects properly integrated with consistent formatting
- Website performance maintained or improved after updates

## Performance Optimization
- **Intelligent Caching**: Reuse unchanged data and content across updates
- **Parallel Processing**: Update multiple components concurrently when possible
- **Selective Rebuilding**: Only regenerate affected pages and components
- **Incremental Validation**: Validate only changed components for efficiency

## Examples
```bash
# Quick daily update check
/update-portfolio --mode quick

# Standard weekly update with change detection
/update-portfolio --mode standard --verbose

# Force full update ignoring change detection
/update-portfolio --mode standard --force

# Check for changes without applying updates
/update-portfolio --check-changes --verbose

# Full refresh equivalent to pipeline
/update-portfolio --mode full
```

This command provides efficient portfolio maintenance and regular updates without requiring complete pipeline regeneration.