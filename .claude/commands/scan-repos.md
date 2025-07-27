# /scan-repos - Repository Discovery and Analysis

## Purpose
Discover and analyze Git repositories with intelligent content filtering and personal contribution validation for portfolio generation.

## Usage
```
/scan-repos [--scan-path PATH] [--output-dir PATH] [--author NAME] [--min-contribution PERCENT] [--validate] [--verbose]
```

## Arguments
- `--scan-path PATH` - Directory to scan for repositories (default: /Users/salim/Documents/)
- `--output-dir PATH` - Output directory for results (default: data/)
- `--author NAME` - Author name to filter for (default: "salim mimouni")
- `--min-contribution PERCENT` - Minimum author contribution percentage (default: 20)
- `--validate` - Validate authorship before including projects
- `--verbose` - Show detailed scanning progress

## Implementation

### 1. Repository Discovery
Use LS and Bash tools to recursively scan for Git repositories:
- Scan specified directory path for .git folders
- Exclude common build/cache directories (node_modules, .venv, __pycache__, .DS_Store)
- Apply depth limits and size filtering for efficiency
- Create initial repository inventory

### 2. Git Analysis  
For each discovered repository, use Bash to extract:
- Commit history and author statistics
- Branch information and activity levels
- File types and technology stack indicators
- README and documentation quality
- Recent activity and maintenance status

### 3. Author Contribution Validation
Calculate contribution metrics:
- Count commits by author using `git log --author`
- Calculate percentage of total commits by target author
- Identify author roles (primary contributor, collaborator, etc.)
- Flag repositories below minimum contribution threshold

### 4. Metadata Extraction
Extract comprehensive repository metadata:
- Technology stack from file extensions and config files
- Project description from README and package files  
- License and documentation quality
- Activity metrics (last commit, total commits, active period)
- Repository size and complexity indicators

### 5. Portfolio Assessment
Evaluate repositories for portfolio inclusion:
- Apply minimum contribution threshold filtering
- Assess project significance and professional relevance
- Identify EU research projects and professional collaborations
- Score projects based on contribution level and impact

### 6. Structured Output Generation
Generate JSON output with repository data:
- Complete metadata for all discovered repositories
- Author contribution validation results  
- Portfolio worthiness scores and recommendations
- Technology stack analysis and expertise mapping

## Output Files
- `repository-scan-results.json` - Complete repository inventory with metadata
- `scan-log.txt` - Detailed scanning process log  
- `discovered-repos.txt` - Simple list of discovered repositories

## Execution Flow

### Initialization Phase
1. **Validate Arguments**: Parse command arguments and set defaults
2. **Check Prerequisites**: Verify Git availability and directory permissions
3. **Setup Output**: Create output directory and initialize logging
4. **Progress Tracking**: Initialize TodoWrite for scan progress

### Discovery Phase
1. **Directory Scanning**: Use LS to recursively find .git directories
2. **Repository Validation**: Verify each discovered repository is accessible
3. **Initial Filtering**: Apply basic filters (size, accessibility, etc.)
4. **Progress Reporting**: Update progress as repositories are discovered

### Analysis Phase
1. **Git Metadata Extraction**: Use Bash to run git commands for each repository
2. **Author Analysis**: Calculate contribution percentages for target author
3. **Technology Detection**: Analyze file types and project structure
4. **Quality Assessment**: Evaluate README, documentation, and project organization

### Validation Phase
1. **Contribution Verification**: Apply minimum contribution thresholds
2. **Portfolio Assessment**: Score repositories for portfolio worthiness
3. **Data Validation**: Verify extracted metadata for completeness
4. **Error Handling**: Report any repositories that failed analysis

### Output Phase
1. **JSON Generation**: Create structured repository-scan-results.json
2. **Log Creation**: Generate detailed scan-log.txt
3. **Summary Report**: Provide scan summary with key statistics
4. **Next Steps**: Recommend next commands based on results

## Error Handling
- **Permission Errors**: Skip inaccessible repositories with warning
- **Git Errors**: Handle corrupted repositories gracefully
- **Analysis Failures**: Continue scan with partial data
- **Output Errors**: Validate file writing and provide fallbacks

## Success Criteria
- All accessible Git repositories discovered and analyzed
- Author contribution validation completed for target author
- Complete metadata extracted with portfolio assessment
- Structured output files generated successfully
- Ready for project classification phase

## Examples
```bash
# Basic repository scan with defaults
/scan-repos

# Scan custom directory with specific author
/scan-repos --scan-path /path/to/projects --author "physics-programmer"

# Scan with lower contribution threshold
/scan-repos --min-contribution 10 --validate

# Verbose scan with detailed output
/scan-repos --verbose --output-dir ./custom-data
```

This command provides comprehensive repository discovery and analysis for portfolio generation.