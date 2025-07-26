# Requirements Specification - physics-programmer Portfolio

## Project Overview

**Project Name**: physics-programmer Portfolio Site
**Purpose**: Create a professional developer portfolio that showcases current projects like a CV
**Target Audience**: Potential collaborators, employers, research partners, EU project evaluators

## Core Requirements

### Identity & Branding
- **Handle**: "physics-programmer" (primary identity)
- **Style**: Professional developer portfolio with scientific/physics theme
- **Tone**: Technical competence, research-oriented, collaborative

### Content Source
- **Primary Data**: Projects in `/Users/salim/Documents/`
- **Repository Discovery**: Automatic scanning of Git repositories
- **Project Classification**: EU projects, internal projects, personal research, collaborations
- **Metadata Extraction**: Git history, commit patterns, technology stacks, activity levels

### Project Information Display
- **Project Overview**: Name, description, current status
- **Technical Details**: Programming languages, frameworks, tools used
- **Activity Metrics**: Recent commits, development timeline, contribution patterns
- **Project Context**: Project type (EU/Internal/Personal), funding source, collaboration details
- **Code Quality**: Repository structure, documentation quality, testing practices

### User Experience Requirements
- **Navigation**: Easy browsing of projects by category, technology, or timeline
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Performance**: Fast loading static site
- **Accessibility**: Screen reader compatible, keyboard navigation
- **Search**: Find projects by technology, keywords, or project type

### Technical Requirements
- **Framework**: Python-based static site generator (Pelican)
- **Architecture**: Agent-driven content generation and management
- **Deployment**: Static hosting (GitHub Pages, Netlify, or Vercel)
- **Updates**: Automated scanning and content regeneration
- **Version Control**: Git-tracked agent definitions and content

## Project Classification Criteria

### EU Projects
- **Indicators**: Horizon Europe, ERC, Marie Curie references
- **Keywords**: "European", "EU funding", "Horizon", "ERC", "MSCA"
- **Documentation**: Grant references, partner institutions, deliverables

### Internal Projects
- **Indicators**: Company/institution specific code, internal tools
- **Keywords**: "internal", "proprietary", "company", "institution"
- **Characteristics**: Limited external documentation, specific use cases

### Research Projects
- **Indicators**: Academic publications, research methodologies
- **Keywords**: "research", "publication", "paper", "experiment"
- **Outputs**: Papers, datasets, analysis tools

### Collaboration Projects
- **Indicators**: Multiple contributors, external repositories
- **Keywords**: "collaboration", "joint", "partnership"
- **Structure**: Shared repositories, cross-institutional work

## Success Criteria

### Functional
- [ ] All Git repositories in Documents folder discovered and analyzed
- [ ] Projects correctly classified by type and context
- [ ] Complete technical profiles generated for each project
- [ ] Responsive portfolio site with professional appearance
- [ ] Fast load times (<3 seconds on standard connections)

### Content Quality
- [ ] Accurate project descriptions and technical details
- [ ] Clear indication of project status and activity levels
- [ ] Proper attribution of collaborations and funding sources
- [ ] Up-to-date information reflecting current project states

### User Experience
- [ ] Intuitive navigation and project discovery
- [ ] Mobile-friendly responsive design
- [ ] Accessible to users with disabilities
- [ ] Professional appearance suitable for career purposes

### Maintenance
- [ ] Agent-driven system for easy content updates
- [ ] Automated scanning and regeneration capabilities
- [ ] Version-controlled agent prompts for system evolution
- [ ] Clear documentation for system operation and modification

## Future Enhancements (Optional)

- **Analytics Integration**: Track visitor engagement with projects
- **Interactive Elements**: Project demos, code previews, documentation integration
- **Publication Integration**: Automatic inclusion of research papers and citations
- **Collaboration Network**: Visual representation of project connections and partnerships
- **Timeline Visualization**: Interactive project development timelines

## Questions for Refinement

1. What specific visual style preferences do you have for the physics-programmer brand?
2. Are there particular projects you want to highlight or keep private?
3. What level of technical detail should be shown for each project?
4. Do you have preferred color schemes or design elements?
5. Should the site include contact information or collaboration requests?
6. Are there specific technologies or achievements you want to emphasize?