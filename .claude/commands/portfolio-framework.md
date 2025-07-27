# /portfolio-framework - Portfolio Project Framework Setup

## Purpose
Initialize and configure the physics-programmer portfolio project framework with proper directory structure, environment validation, and dependency checking.

## Usage
```
/portfolio-framework [--project-root PATH] [--validate] [--reset] [--verbose]
```

## Arguments
- `--project-root PATH` - Set custom project root (default: /Users/salim/Documents/github-profile/)
- `--validate` - Validate existing setup without making changes
- `--reset` - Reset project structure to clean state
- `--verbose` - Show detailed setup information

## Implementation

### 1. Environment Validation
- Validate project root directory permissions and accessibility
- Check required system dependencies (Git, Python, etc.)
- Verify file system permissions for read/write operations

### 2. Directory Structure Setup
- Create standardized project directory structure
- Initialize data, content, and output directories
- Set up logging and configuration directories

### 3. Configuration Management
- Establish default configuration values
- Set up environment variables and paths
- Initialize project state tracking

### 4. Dependency Verification
- Check Claude Code tool availability
- Validate required Python packages for Pelican
- Verify Git configuration and access

### 5. Project State Initialization
- Create project metadata and configuration files
- Initialize tracking for pipeline execution state
- Set up logging and error handling frameworks

## Project Structure

### Directory Layout
```
/Users/salim/Documents/github-profile/
├── .claude/           # Slash commands and configurations
├── data/             # Generated data and scan results
├── content/          # Pelican content files
├── output/           # Generated website
├── themes/           # Pelican themes
├── agents/           # Legacy agent configurations (if present)
└── logs/             # Execution logs and reports
```

## Execution Flow

### Setup Phase
1. **Validate Arguments**: Parse and validate command-line arguments
2. **Check Environment**: Verify system dependencies and permissions
3. **Create Directories**: Initialize required directory structure
4. **Set Configuration**: Establish project configuration and defaults

### Validation Phase  
1. **System Dependencies**: Check Git, Python, and required tools
2. **Project Structure**: Verify all required directories exist
3. **Permissions**: Validate read/write access to project directories
4. **State Consistency**: Check for existing project state and conflicts

### Reporting Phase
1. **Setup Summary**: Report initialization results and configuration
2. **Validation Results**: Display dependency and structure validation
3. **Next Steps**: Provide guidance for next commands to run
4. **Error Handling**: Report any issues with resolution guidance

## Error Handling

### Error Categories
- **Configuration Error**: Invalid arguments or missing prerequisites
- **Permission Error**: File system access or directory creation failures  
- **Dependency Error**: Missing system tools or Python packages
- **State Error**: Conflicting existing project state

### Recovery Strategies
- **Automatic Retry**: Retry transient file system operations
- **User Guidance**: Provide clear instructions for manual resolution
- **Graceful Degradation**: Continue with reduced functionality when possible
- **Clean Rollback**: Restore previous state on critical failures

## Prerequisites
- Git installed and configured
- Python 3.8+ with pip
- Write permissions to project directory
- Claude Code with standard tools available

## Success Criteria
- All required directories created
- Project configuration initialized
- Dependencies validated
- System ready for portfolio commands

## Examples
```bash
# Basic setup with defaults
/portfolio-framework

# Setup with custom project root
/portfolio-framework --project-root /path/to/portfolio

# Validate existing setup
/portfolio-framework --validate

# Reset and reinitialize
/portfolio-framework --reset --verbose
```

This framework provides the foundation for all portfolio generation commands with consistent error handling and validation.