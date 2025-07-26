# Command Framework for Physics-Programmer Portfolio

## Overview
This document defines the execution framework for our custom agent commands. Each command follows standardized patterns for configuration, execution, and reporting.

## Command Execution Pattern

### 1. Configuration Validation
- Validate required parameters
- Set default values for optional parameters
- Check file system permissions and prerequisites

### 2. Agent Prompt Loading
- Load agent prompt from `/agents/` directory
- Merge command configuration with agent prompt
- Validate agent requirements and tool availability

### 3. Execution Environment Setup
- Create output directories if needed
- Set up logging and progress tracking
- Initialize error handling and recovery mechanisms

### 4. Agent Execution
- Execute agent with provided configuration
- Monitor progress and handle errors gracefully
- Capture outputs and validate against expected schema

### 5. Result Validation and Reporting
- Validate output files and data formats
- Generate execution summary and status report
- Update project state for pipeline coordination

## Standard Configuration Schema

```json
{
  "agent_name": "string",
  "execution_id": "uuid",
  "timestamp": "iso8601",
  "configuration": {
    "input_path": "string",
    "output_directory": "string", 
    "validation_rules": {},
    "custom_parameters": {}
  },
  "environment": {
    "project_root": "string",
    "data_directory": "string",
    "agents_directory": "string"
  }
}
```

## Error Handling Framework

### Error Categories
- **Configuration Error**: Invalid parameters or missing prerequisites
- **Execution Error**: Agent runtime failures or tool errors
- **Validation Error**: Output validation failures or schema mismatches
- **System Error**: File system, permissions, or resource errors

### Recovery Strategies
- **Retry Logic**: Automatic retry for transient failures
- **Partial Success**: Handle partial completions gracefully
- **Rollback**: Restore previous state on critical failures
- **Escalation**: Report complex errors to user with actionable guidance

## Progress Tracking

### Status Levels
- **INITIALIZING**: Command setup and validation
- **EXECUTING**: Agent running and processing
- **VALIDATING**: Output validation and verification
- **COMPLETED**: Successful completion with valid outputs
- **FAILED**: Execution failure with error details

### Progress Reporting
- Real-time status updates during execution
- Estimated completion times for long-running operations
- Detailed logs for debugging and optimization
- Summary reports for pipeline coordination

## Integration Patterns

### Pipeline Coordination
- Commands can check prerequisites from previous agents
- Standardized data exchange formats between agents
- Automatic dependency resolution and execution ordering
- Checkpoint and resume capabilities for long pipelines

### Environment Adaptation
- Development vs. production configuration profiles
- Local vs. CI/CD execution environments
- Resource scaling based on available system capacity
- Graceful degradation when optional tools unavailable

This framework ensures consistent, reliable, and maintainable agent execution across all custom commands.