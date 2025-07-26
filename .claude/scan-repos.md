# Scan Repositories Command

Execute the Repository Scanner Agent to discover and analyze Git repositories.

## Command Configuration

**Agent**: Repository Scanner  
**Prompt Source**: `/Users/salim/Documents/github-profile/agents/repository-scanner.md`  
**Output Directory**: `/Users/salim/Documents/github-profile/data/`

## Execution Parameters

### Default Configuration
- **SCAN_PATH**: `/Users/salim/Documents/`
- **OUTPUT_DIR**: `/Users/salim/Documents/github-profile/data/`
- **SCAN_DEPTH**: Unlimited (recursive)
- **MIN_COMMITS**: 1
- **ACTIVITY_THRESHOLD_DAYS**: 90
- **AUTHOR_FILTER**: `["salim mimouni", "physics-programmer"]`
- **MIN_AUTHOR_CONTRIBUTION**: 10 (minimum 10% of commits)
- **REQUIRE_AUTHOR_PRESENCE**: true

### Environment Setup
- **PROJECT_ROOT**: `/Users/salim/Documents/github-profile/`
- **AGENTS_DIR**: `/Users/salim/Documents/github-profile/agents/`
- **DATA_DIR**: `/Users/salim/Documents/github-profile/data/`

## Agent Execution

You are the Repository Scanner Agent for the physics-programmer portfolio project. Load your complete system prompt from `/Users/salim/Documents/github-profile/agents/repository-scanner.md` and execute it with the following configuration:

### Configuration
```json
{
  "SCAN_PATH": "/Users/salim/Documents/",
  "OUTPUT_DIR": "/Users/salim/Documents/github-profile/data/",
  "SCAN_DEPTH": "unlimited",
  "EXCLUDE_PATTERNS": ["node_modules", ".venv", "__pycache__", ".DS_Store", "dist", "build"],
  "MIN_COMMITS": 1,
  "MAX_REPOS": "unlimited",
  "ACTIVITY_THRESHOLD_DAYS": 90,
  "AUTHOR_FILTER": ["salim mimouni", "physics-programmer"],
  "MIN_AUTHOR_CONTRIBUTION": 10,
  "REQUIRE_AUTHOR_PRESENCE": true,
  "PROJECT_ROOT": "/Users/salim/Documents/github-profile/",
  "AGENTS_DIR": "/Users/salim/Documents/github-profile/agents/",
  "DATA_DIR": "/Users/salim/Documents/github-profile/data/"
}
```

### Mission Objectives
1. **Repository Discovery**: Scan `/Users/salim/Documents/` recursively for all Git repositories
2. **Author Filtering**: Apply contribution-based filtering to only include repos with meaningful user involvement
3. **Metadata Extraction**: Extract Git history, technology stack, activity levels for each repo
4. **Quality Assessment**: Analyze README quality, documentation, project structure
5. **Structured Output**: Generate JSON data ready for Project Classifier Agent with author contribution metrics

### Required Outputs
- `repository-scan-results.json` - Complete repository inventory with metadata
- `scan-log.txt` - Detailed scanning process log
- `discovered-repos.txt` - Simple list of discovered repositories

### Success Criteria
- Discover all Git repositories in the Documents folder
- Extract complete metadata for repositories with commits
- Generate accurate technology stack profiles
- Provide reliable activity and quality assessments
- Create structured output ready for classification

### Tools Available
- **LS**: Directory exploration and file discovery
- **Bash**: Git commands and file system operations  
- **Read**: Examining configuration files and README content
- **Write**: Saving scan results and logs

### Focus Areas
Prioritize discovery of projects valuable for a computational researcher's portfolio:
- Research projects and academic work
- EU/international collaborations  
- Scientific computing and data science projects
- Open source contributions and tools
- Professional software development work

Execute this systematically and provide detailed findings with structured status reporting as defined in your agent prompt.