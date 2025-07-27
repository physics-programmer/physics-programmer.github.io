# /classify-projects - Project Classification and Assessment

## Purpose
Categorize and assess repository significance for portfolio generation using intelligent classification and evidence-based scoring.

## Usage
```
/classify-projects [--input-file PATH] [--output-dir PATH] [--confidence-threshold FLOAT] [--portfolio-threshold FLOAT] [--verbose]
```

## Arguments
- `--input-file PATH` - Repository scan results file (default: data/repository-scan-results.json)
- `--output-dir PATH` - Output directory for classifications (default: data/)
- `--confidence-threshold FLOAT` - Minimum confidence for classification (default: 0.7)
- `--portfolio-threshold FLOAT` - Minimum score for portfolio inclusion (default: 0.5)
- `--verbose` - Show detailed classification reasoning

## Implementation

### 1. Input Validation
- Read and validate repository scan results file
- Check data completeness and format integrity
- Verify required metadata fields are present
- Initialize classification tracking with TodoWrite

### 2. Classification Analysis
For each repository, analyze using Read and Grep tools:
- **README Content Analysis**: Search for project indicators and keywords
- **Technology Stack Assessment**: Evaluate technology choices for professionalism
- **Documentation Quality**: Assess completeness and professional presentation
- **Collaboration Evidence**: Look for multiple contributors and institutional affiliations

### 3. Category Classification
Apply intelligent classification using keyword detection:

**EU_FUNDED_RESEARCH Indicators:**
- Keywords: "EU", "European", "Horizon", "H2020", "FP7", "ERC", "Marie Curie", "MSCA", "Grant"
- Institutional affiliations in README or documentation
- Grant numbers or funding acknowledgments

**ACADEMIC_RESEARCH Indicators:**
- Keywords: "research", "university", "paper", "publication", "DOI", "experiment", "study"
- Academic email addresses in Git history
- Research methodology descriptions

**PROFESSIONAL_COLLABORATION Indicators:**
- Keywords: "consortium", "partner", "joint", "collaboration", "multi-institutional"
- Multiple professional contributors
- Commercial or enterprise technology stacks

**INTERNAL_TOOLS Indicators:**
- Single-author repositories with utility focus
- Limited documentation or private use indicators
- Development/debugging tool patterns

**PERSONAL_PROJECTS Indicators:**
- Learning projects and experiments
- Tutorial following or skill development
- Limited scope and personal use focus

### 4. Significance Scoring
Calculate portfolio worthiness based on:
- Author contribution percentage (higher = better)
- Project complexity and professional relevance
- Documentation quality and completeness
- Technology stack sophistication
- Collaboration level and institutional connections

### 5. Evidence Documentation
For each classification decision:
- Record specific evidence found (keywords, patterns, metadata)
- Calculate confidence score based on evidence strength
- Document reasoning for manual review if needed
- Flag low-confidence classifications for review

## Output Files
- `classified-projects.json` - Complete project classifications with evidence
- `classification-summary.json` - Portfolio-level statistics and recommendations  
- `classification-log.txt` - Detailed analysis process log

## Execution Flow

### Initialization Phase
1. **Validate Arguments**: Parse command arguments and apply defaults
2. **Check Prerequisites**: Verify input file exists and is readable
3. **Setup Output**: Create output directory and initialize logging
4. **Progress Tracking**: Initialize TodoWrite for classification progress

### Analysis Phase
1. **Load Repository Data**: Read and parse repository scan results
2. **Repository Iteration**: Process each repository systematically
3. **Content Analysis**: Use Read/Grep to analyze README and documentation
4. **Pattern Matching**: Apply classification indicators and scoring

### Classification Phase
1. **Category Assignment**: Determine primary project category
2. **Evidence Collection**: Document supporting evidence for classification
3. **Confidence Scoring**: Calculate confidence based on evidence strength
4. **Portfolio Scoring**: Assess project value for portfolio inclusion

### Validation Phase
1. **Threshold Filtering**: Apply confidence and portfolio thresholds
2. **Quality Review**: Flag low-confidence classifications for review
3. **Data Validation**: Verify classification completeness and consistency
4. **Summary Generation**: Create portfolio-level statistics

### Output Phase
1. **JSON Generation**: Create structured classified-projects.json
2. **Summary Creation**: Generate classification-summary.json
3. **Log Documentation**: Write detailed classification-log.txt
4. **Next Steps**: Recommend content generation with classification results

## Error Handling
- **Missing Input**: Graceful handling when scan results unavailable
- **Malformed Data**: Skip corrupted repository entries with warnings
- **Analysis Failures**: Continue classification with partial data
- **Output Errors**: Validate file writing and provide error recovery

## Success Criteria
- All repositories classified with evidence and confidence scores
- Portfolio-worthy projects identified and prioritized
- Clear documentation of classification reasoning
- Structured output ready for content generation phase

## Examples
```bash
# Basic classification with defaults
/classify-projects

# Classification with custom thresholds
/classify-projects --confidence-threshold 0.8 --portfolio-threshold 0.6

# Verbose classification with custom input
/classify-projects --input-file ./custom-scan.json --verbose

# Low-threshold classification for comprehensive review
/classify-projects --confidence-threshold 0.5 --portfolio-threshold 0.3
```

This command provides intelligent project classification and portfolio assessment for content generation.