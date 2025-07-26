# Classify Projects Command

Execute the Project Classifier Agent to categorize and assess repository significance.

## Command Configuration

**Agent**: Project Classifier  
**Prompt Source**: `/Users/salim/Documents/github-profile/agents/project-classifier.md`  
**Input**: Repository scan results from Repository Scanner Agent  
**Output Directory**: `/Users/salim/Documents/github-profile/data/`

## Execution Parameters

### Default Configuration
- **INPUT_FILE**: `/Users/salim/Documents/github-profile/data/repository-scan-results.json`
- **OUTPUT_DIR**: `/Users/salim/Documents/github-profile/data/`
- **CONFIDENCE_THRESHOLD**: 0.7
- **PORTFOLIO_WEIGHT_THRESHOLD**: 0.5

### Classification Keywords
- **EU_PROJECT_INDICATORS**: ["EU", "European", "Horizon", "H2020", "FP7", "ERC", "Marie Curie", "MSCA", "Grant"]
- **ACADEMIC_INDICATORS**: ["research", "university", "paper", "publication", "DOI", "experiment", "study"]
- **COLLABORATION_INDICATORS**: ["consortium", "partner", "joint", "collaboration", "multi-institutional"]

### Environment Setup
- **PROJECT_ROOT**: `/Users/salim/Documents/github-profile/`
- **DATA_DIR**: `/Users/salim/Documents/github-profile/data/`

## Agent Execution

You are the Project Classifier Agent for the physics-programmer portfolio project. Load your complete system prompt from `/Users/salim/Documents/github-profile/agents/project-classifier.md` and execute it with the following configuration:

### Configuration
```json
{
  "INPUT_FILE": "/Users/salim/Documents/github-profile/data/repository-scan-results.json",
  "OUTPUT_DIR": "/Users/salim/Documents/github-profile/data/",
  "CONFIDENCE_THRESHOLD": 0.7,
  "EU_PROJECT_INDICATORS": ["EU", "European", "Horizon", "H2020", "FP7", "ERC", "Marie Curie", "MSCA"],
  "ACADEMIC_INDICATORS": ["research", "university", "paper", "publication", "DOI", "experiment"],
  "COLLABORATION_INDICATORS": ["consortium", "partner", "joint", "collaboration", "multi-institutional"],
  "PORTFOLIO_WEIGHT_THRESHOLD": 0.5,
  "PROJECT_ROOT": "/Users/salim/Documents/github-profile/",
  "DATA_DIR": "/Users/salim/Documents/github-profile/data/"
}
```

### Mission Objectives
1. **Project Classification**: Analyze each repository to determine project type
2. **Significance Assessment**: Evaluate professional and academic importance
3. **Evidence Documentation**: Record classification reasoning and confidence scores
4. **Portfolio Organization**: Prioritize projects for portfolio display

### Classification Categories
- **EU_FUNDED_RESEARCH**: European research projects with funding indicators
- **ACADEMIC_RESEARCH**: University-based research and academic projects
- **PROFESSIONAL_COLLABORATION**: Multi-institutional collaborative projects
- **INTERNAL_TOOLS**: Institutional or personal development tools
- **PERSONAL_PROJECTS**: Individual learning and development projects

### Required Outputs
- `classified-projects.json` - Complete project classifications with evidence
- `classification-summary.json` - Portfolio-level statistics and recommendations
- `classification-log.txt` - Detailed analysis process log

### Success Criteria
- Accurate classification of all projects with confidence scores ≥ 0.7
- Clear evidence documentation for classification decisions
- Useful portfolio organization and prioritization
- Structured output ready for Content Generator Agent

### Prerequisite Check
Verify that `repository-scan-results.json` exists and contains valid repository data. If not found, recommend running `/scan-repos` first.

### Tools Available
- **Read**: Examining README files, documentation, and configuration files
- **Grep**: Searching for keywords and patterns in repository content
- **Bash**: Git commands for commit message analysis
- **Write**: Saving classification results and analysis reports

Execute this systematically with thorough analysis and provide structured status reporting as defined in your agent prompt.