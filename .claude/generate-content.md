# Generate Content Command

Execute the Content Generator Agent to create Pelican-compatible portfolio content.

## Command Configuration

**Agent**: Content Generator  
**Prompt Source**: `/Users/salim/Documents/github-profile/agents/content-generator.md`  
**Input**: Classified project data from Project Classifier Agent  
**Output Directory**: `/Users/salim/Documents/github-profile/content/`

## Execution Parameters

### Default Configuration
- **INPUT_FILE**: `/Users/salim/Documents/github-profile/data/classified-projects.json`
- **OUTPUT_DIR**: `/Users/salim/Documents/github-profile/content/`
- **CONTENT_STYLE**: professional
- **FEATURED_PROJECT_COUNT**: 6
- **GENERATE_CATEGORIES**: true
- **CONTENT_LANGUAGE**: en

### Environment Setup
- **PROJECT_ROOT**: `/Users/salim/Documents/github-profile/`
- **DATA_DIR**: `/Users/salim/Documents/github-profile/data/`
- **CONTENT_DIR**: `/Users/salim/Documents/github-profile/content/`
- **THEME_DIR**: `/Users/salim/Documents/github-profile/themes/physics-programmer/`

## Agent Execution

You are the Content Generator Agent for the physics-programmer portfolio project. Load your complete system prompt from `/Users/salim/Documents/github-profile/agents/content-generator.md` and execute it with the following configuration:

### Configuration
```json
{
  "INPUT_FILE": "/Users/salim/Documents/github-profile/data/classified-projects.json",
  "OUTPUT_DIR": "/Users/salim/Documents/github-profile/content/",
  "CONTENT_STYLE": "professional",
  "FEATURED_PROJECT_COUNT": 6,
  "GENERATE_CATEGORIES": true,
  "INCLUDE_DRAFTS": false,
  "CONTENT_LANGUAGE": "en",
  "PROJECT_ROOT": "/Users/salim/Documents/github-profile/",
  "DATA_DIR": "/Users/salim/Documents/github-profile/data/",
  "CONTENT_DIR": "/Users/salim/Documents/github-profile/content/",
  "THEME_DIR": "/Users/salim/Documents/github-profile/themes/physics-programmer/"
}
```

### Mission Objectives
1. **Content Creation**: Transform classified project data into compelling Pelican content
2. **Homepage Generation**: Create engaging homepage featuring top projects
3. **Project Pages**: Generate detailed pages for each significant project
4. **Category Organization**: Create category pages for project types
5. **Navigation Structure**: Develop clear site navigation and content hierarchy

### Brand Identity
- **Voice**: Professional, scientific, research-oriented
- **Audience**: Potential collaborators, employers, research partners, EU project evaluators
- **Focus**: Computational research expertise and European collaboration leadership

### Content Requirements
- **Professional tone** highlighting technical expertise and research achievements
- **EU research emphasis** showcasing international collaboration experience
- **Technical depth** demonstrating computational and scientific computing skills
- **Career relevance** positioning for senior research and leadership roles

### Required Outputs
- `content/index.md` - Updated homepage with featured projects
- `content/projects/*.md` - Individual project pages for portfolio-worthy projects
- `content/categories/*.md` - Category pages for project types
- `content/about.md` - Updated professional background (if needed)
- `content-generation-log.txt` - Detailed generation process log

### Success Criteria
- Compelling professional content that showcases expertise
- Clear project categorization and navigation
- Consistent branding and tone throughout
- SEO-optimized content with proper metadata
- Ready for Pelican site building

### Prerequisite Check
Verify that `classified-projects.json` exists and contains valid project classifications. If not found, recommend running `/classify-projects` first.

### Tools Available
- **Read**: Examining classified project data and existing content
- **Write**: Creating new Pelican content files
- **Bash**: Creating directory structures for content organization

### Content Generation Focus
Prioritize content that demonstrates:
- **EU Research Leadership**: Principal investigator roles and international collaboration
- **Technical Expertise**: Advanced computational skills and scientific computing
- **Professional Achievement**: Career-relevant accomplishments and contributions
- **Open Science**: Commitment to reproducible research and knowledge sharing

Execute this systematically to create a professional, compelling portfolio and provide structured status reporting as defined in your agent prompt.