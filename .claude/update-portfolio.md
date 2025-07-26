# Update Portfolio Command

Incremental portfolio update workflow for maintaining current content.

## Update Strategy

This command provides smart incremental updates rather than full pipeline regeneration:

1. **Smart Scanning**: Only process new or modified repositories
2. **Incremental Classification**: Update classifications for changed projects
3. **Selective Content Generation**: Generate content only for updated projects
4. **Optimized Building**: Fast rebuild with change detection

## Update Modes

### Quick Update (5-10 minutes)
- Scan for new repositories only
- Update existing project metadata if significantly changed
- Regenerate homepage and navigation
- Fast site rebuild

### Standard Update (15-20 minutes)  
- Full repository scan with change detection
- Reclassify projects with low confidence scores
- Update content for modified projects
- Complete site rebuild with optimization

### Full Refresh (45-60 minutes)
- Complete pipeline execution (equivalent to `/full-pipeline`)
- Use when major changes or troubleshooting needed

## Update Execution

### Prerequisites Check
Verify existing portfolio state:
- Check for previous pipeline execution results
- Validate existing data files integrity
- Confirm website builds successfully

### Change Detection
Identify what needs updating:
- New Git repositories since last scan
- Modified repositories (new commits, changed README)
- Classification confidence scores below threshold
- Missing or outdated content files

### Selective Processing
Execute only necessary agent operations:
- **Repository Scanner**: Process new/changed repositories only
- **Project Classifier**: Reclassify flagged projects
- **Content Generator**: Update affected content files
- **Site Builder**: Incremental build with change detection

## Update Configuration

### Default Settings
- **UPDATE_MODE**: standard
- **CHANGE_DETECTION**: true
- **FORCE_RECLASSIFICATION**: false
- **CONTENT_REFRESH_THRESHOLD**: 30 days
- **BUILD_OPTIMIZATION**: true

### Smart Thresholds
- **New Repository Detection**: Repositories created since last scan
- **Significant Changes**: >10 new commits or major README updates
- **Classification Review**: Confidence scores <0.8
- **Content Staleness**: Content older than 30 days

## Update Process

### Phase 1: State Analysis
```
1. Load previous execution results
2. Compare current repository state
3. Identify changes and update requirements
4. Calculate update scope and estimated time
```

### Phase 2: Incremental Updates
```
1. Update repository metadata for changed projects
2. Reclassify projects with low confidence or significant changes
3. Regenerate content for updated projects
4. Update homepage and navigation with new information
```

### Phase 3: Site Refresh
```
1. Perform optimized site build
2. Validate changes and test functionality
3. Generate update report
4. Prepare for deployment
```

## Update Outputs

### Change Report
Document all updates made:
- New repositories discovered
- Projects reclassified
- Content files updated
- Performance improvements

### Update Log
Detailed log of update process:
- Change detection results
- Processing decisions
- Time savings vs full pipeline
- Any issues encountered

### Deployment Summary
Prepare deployment information:
- Files changed since last deployment
- Validation results
- Performance impact
- Deployment readiness

## Smart Update Logic

### Repository Changes
```
IF new_repositories_found > 0:
    run_repository_scanner(new_repos_only=True)
    
IF significant_changes_detected > 5:
    run_project_classifier(changed_projects_only=True)
    
IF content_age > threshold OR projects_updated:
    run_content_generator(selective_update=True)
    
ALWAYS:
    run_site_builder(optimization_level="fast")
```

### Performance Optimization
- **Parallel Processing**: Update multiple projects concurrently
- **Caching**: Reuse unchanged data and content
- **Selective Building**: Only rebuild affected pages
- **Incremental Validation**: Validate only changed components

## Usage Examples

### Quick Daily Update
```
/update-portfolio mode=quick
```
Check for new repositories and update homepage (5 minutes)

### Weekly Standard Update  
```
/update-portfolio mode=standard
```
Comprehensive update with change detection (15-20 minutes)

### Monthly Full Refresh
```
/update-portfolio mode=full
```
Complete pipeline regeneration (45-60 minutes)

### Force Update
```
/update-portfolio force=true
```
Ignore change detection and update everything

## Success Criteria

### Update Efficiency
- Significant time savings vs full pipeline
- Accurate change detection
- No loss of existing quality content
- Smooth deployment process

### Content Quality
- New projects properly integrated
- Existing content remains accurate
- Navigation and links updated correctly
- Professional consistency maintained

## Error Handling

### Update Failures
- **Partial Updates**: Complete what's possible, report failures
- **Rollback Capability**: Restore previous state if major issues
- **Manual Override**: Allow forced updates when automation fails
- **Graceful Degradation**: Maintain existing portfolio if updates fail

### Change Detection Issues
- **False Positives**: Validate detected changes before processing
- **Missed Changes**: Provide manual override for forced updates
- **State Corruption**: Detect and recover from data inconsistencies

Use this command for efficient portfolio maintenance and regular updates without full pipeline regeneration.