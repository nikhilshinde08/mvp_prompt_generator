# GitHub MVP Generator

This tool transforms any GitHub repository into an MVP (Minimum Viable Product) prompt for bootstrapping new projects based on proven open-source implementations.

## How It Works

1. **Repository Analysis**: The tool analyzes the GitHub repository by:
   - Examining the repository structure and files
   - Identifying the primary programming language
   - Detecting frameworks and technologies used
   - Analyzing the README and other documentation

2. **MVP Prompt Generation**: Based on the analysis, it generates a structured prompt that includes:
   - Project type and architecture
   - Technology stack
   - Key features
   - Implementation guidance
   - Step-by-step instructions

## Use Cases

- **Learning**: Understand how popular open-source projects are structured
- **Bootstrapping**: Quickly start new projects based on proven architectures
- **Education**: Create coding exercises and assignments based on real projects
- **Planning**: Generate implementation plans for new features

## Supported Technologies

The tool can analyze repositories built with:
- JavaScript/TypeScript frameworks (React, Vue, Angular, etc.)
- Python frameworks (Django, Flask, FastAPI, etc.)
- Java frameworks (Spring, etc.)
- Ruby frameworks (Rails, etc.)
- And many more...

## Output Format

The generated MVP prompt follows a structured format:
```
Build an MVP inspired by: @{repo_url}

PROJECT TYPE: {type}
TECH STACK: {technologies}
ARCHITECTURE: {architecture}

KEY FEATURES:
1. {feature_1}
2. {feature_2}
...

COMPLEXITY LEVEL: {level}

MVP GUIDANCE:
1. {guidance_1}
2. {guidance_2}
...

IMPLEMENTATION STEPS:
1. {step_1}
2. {step_2}
...

Focus on creating a clean, functional implementation...
```