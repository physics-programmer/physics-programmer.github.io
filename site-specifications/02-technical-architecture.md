# Technical Architecture - physics-programmer Portfolio

## System Architecture Overview

### Agent-Driven Design Philosophy
The portfolio system uses an innovative **agent-driven architecture** where specialized AI agents handle different aspects of site generation and maintenance. Each agent is defined by a markdown file containing system prompts rather than traditional code.

### Core Architecture Principles
- **Declarative Agent Definitions**: Behavior defined through prompts, not imperative code
- **Modular Agent System**: Each agent has a specific, well-defined responsibility
- **Workflow Orchestration**: Agents work together through defined workflows
- **Static Site Generation**: Fast, secure, deployable static output
- **Python-Based Toolchain**: Pelican for site generation, Python ecosystem for processing

## System Components

### 1. Agent Layer
**Purpose**: Intelligent processing and content generation
**Location**: `/agents/` directory
**Format**: Markdown files with system prompts

#### Core Agents
- **Repository Scanner Agent**: Discovers and analyzes Git repositories
- **Project Classifier Agent**: Categorizes projects by type and context
- **Content Generator Agent**: Creates Pelican-compatible markdown content
- **Site Builder Agent**: Manages Pelican build and optimization processes

#### Specification Agents
- **Requirements Analyst Agent**: Gathers and refines user requirements
- **Technical Architect Agent**: Makes technical decisions and recommendations

### 2. Workflow Orchestration Layer
**Purpose**: Coordinates agent execution and data flow
**Location**: `/workflows/` directory
**Format**: Markdown files with agent execution sequences

#### Core Workflows
- **Full Site Build**: Complete portfolio generation from scratch
- **Content Update**: Incremental updates to existing content
- **Requirements Gathering**: Interactive specification refinement

### 3. Content Generation Layer
**Purpose**: Static site content management
**Technology**: Pelican static site generator
**Input**: Markdown content from agents
**Output**: HTML/CSS/JS static site

### 4. Data Processing Pipeline

```
Documents Folder → Repository Scanner → Project Classifier → Content Generator → Site Builder → Static Site
```

#### Data Flow
1. **Discovery**: Scanner agent finds Git repositories in Documents folder
2. **Analysis**: Classifier agent analyzes repositories for type, technology, activity
3. **Classification**: Projects categorized as EU/Internal/Research/Collaboration
4. **Content Creation**: Generator agent creates structured Pelican content
5. **Site Building**: Builder agent processes content into deployable static site

### 5. Theme and Design System
**Framework**: Custom Pelican theme for physics-programmer brand
**Styling**: CSS with physics/scientific design elements
**Responsiveness**: Mobile-first responsive design
**Accessibility**: WCAG 2.1 AA compliance

## Technology Stack

### Core Technologies
- **Python 3.9+**: Primary development language
- **Pelican**: Static site generator
- **Markdown**: Content format for both agents and site content
- **Git**: Version control for both content and agent definitions
- **Claude Code Task Tool**: Agent execution runtime

### Dependencies
```python
# requirements.txt
pelican[markdown]>=4.8.0
typogrify>=2.0.7
python-dateutil>=2.8.0
pygments>=2.12.0
```

### Development Tools
- **Agent Runtime**: Claude Code with Task tool for sub-agent execution
- **Local Preview**: Pelican built-in development server
- **Build Automation**: Agent-driven build process
- **Version Control**: Git for all components

## Agent System Design

### Agent Definition Structure
Each agent is defined in a markdown file with:
- **Role Definition**: Clear purpose and responsibilities
- **Input Specifications**: Expected data format and sources
- **Processing Instructions**: Detailed operational guidelines
- **Output Requirements**: Format and structure of generated results
- **Tool Permissions**: Specific tools the agent may use

### Agent Communication
- **Input/Output**: Structured data exchange between agents
- **State Management**: Temporary files for inter-agent data sharing
- **Error Handling**: Graceful failure and recovery procedures
- **Logging**: Agent execution tracking and debugging

### Agent Execution Model
- **Invocation**: Through Claude Code Task tool
- **Isolation**: Each agent runs in isolated context
- **Coordination**: Workflow files define execution sequences
- **Monitoring**: Success/failure tracking and error reporting

## Data Schema

### Repository Metadata
```json
{
  "name": "project-name",
  "path": "/full/path/to/repository",
  "git_url": "remote-origin-url",
  "description": "project description",
  "languages": ["Python", "JavaScript"],
  "frameworks": ["FastAPI", "React"],
  "last_commit": "2024-01-15T10:30:00Z",
  "commit_count": 150,
  "contributors": ["physics-programmer"],
  "project_type": "EU_PROJECT",
  "classification_confidence": 0.95,
  "activity_level": "HIGH",
  "documentation_quality": "GOOD"
}
```

### Project Classification Schema
```json
{
  "project_types": {
    "EU_PROJECT": "European Union funded research",
    "INTERNAL_PROJECT": "Institution or company internal work",
    "RESEARCH_PROJECT": "Academic research and publications",
    "COLLABORATION": "Multi-party collaborative work",
    "PERSONAL_PROJECT": "Individual development work"
  },
  "activity_levels": ["HIGH", "MEDIUM", "LOW", "ARCHIVED"],
  "technology_categories": ["AI/ML", "Web Development", "Data Analysis", "Scientific Computing"]
}
```

## Deployment Architecture

### Build Process
1. **Agent Execution**: Workflow orchestrates all agents
2. **Content Generation**: Pelican processes agent output
3. **Static Site Output**: HTML/CSS/JS in `/output/` directory
4. **Deployment**: Upload to hosting service

### Hosting Options
- **GitHub Pages**: Free, automatic deployment from repository
- **Netlify**: Continuous deployment with build hooks
- **Vercel**: Python support with automatic deployments
- **Self-Hosted**: Any web server serving static files

### Update Mechanism
- **Manual Trigger**: Run full site build workflow
- **Automated**: Git hooks or scheduled builds
- **Incremental**: Content update workflow for faster rebuilds

## Security Considerations

### Data Privacy
- **Local Processing**: All analysis happens locally
- **No External APIs**: Avoid sending code to external services
- **Selective Publishing**: Control which projects are included in public site

### Agent Security
- **Sandboxed Execution**: Agents run in isolated contexts
- **Tool Restrictions**: Agents only access permitted tools
- **Input Validation**: Sanitize all agent inputs and outputs

## Performance Requirements

### Build Time
- **Full Build**: <5 minutes for typical project portfolio
- **Incremental Update**: <1 minute for content changes
- **Agent Execution**: <30 seconds per agent

### Site Performance
- **Load Time**: <3 seconds on 3G networks
- **Bundle Size**: <500KB initial load
- **Responsiveness**: <100ms interaction response times

### Scalability
- **Project Count**: Support for 100+ repositories
- **Content Volume**: Handle large repositories efficiently
- **Agent Complexity**: Support for additional specialized agents

## Monitoring and Maintenance

### Agent Performance Tracking
- **Execution Time**: Monitor agent processing duration
- **Success Rates**: Track agent completion rates
- **Error Patterns**: Identify common failure modes

### Content Quality Assurance
- **Link Validation**: Ensure all generated links work
- **Content Accuracy**: Verify project information correctness
- **Update Freshness**: Monitor content staleness

### System Evolution
- **Agent Prompt Versioning**: Track agent definition changes
- **A/B Testing**: Compare agent prompt variations
- **Performance Optimization**: Continuous improvement of agent efficiency