# GitHub MVP Generator Usage Examples

Here are some examples of how to use the GitHub MVP Generator with different types of repositories.

## Basic Usage

Analyze any public GitHub repository:

```bash
python main.py https://github.com/facebook/react
```

With a GitHub personal access token for higher rate limits:

```bash
python main.py https://github.com/facebook/react --token YOUR_GITHUB_TOKEN
```

## Example Outputs

### React Application
```
Build an MVP inspired by: @https://github.com/facebook/react

PROJECT TYPE: React Web Application
TECH STACK: JavaScript, React
ARCHITECTURE: Frontend SPA with component-based architecture

KEY FEATURES:
1. React Hooks - Functional components with hooks
2. Component System - Reusable UI components
3. State Management - Centralized state handling

COMPLEXITY LEVEL: Advanced

MVP GUIDANCE:
1. Core Components - Create main App component with state management
2. Component Hierarchy - Build reusable UI components with props
3. State Management - Use hooks for local state management
4. Event Handling - Implement user interactions and form handling
5. Styling - Add CSS modules or styled components for styling

IMPLEMENTATION STEPS:
1. Initialize React project with Create React App or Vite
2. Install required dependencies and libraries
3. Set up project structure with components directory
4. Create main App component with basic layout
5. Implement routing with React Router
6. Build reusable UI components
7. Add state management with hooks
8. Implement form handling and validation
9. Add styling with CSS or styling library
10. Test and optimize the application
```

### Python Application
```
Build an MVP inspired by: @https://github.com/tensorflow/tensorflow

PROJECT TYPE: Python Application
TECH STACK: Python
ARCHITECTURE: Python application architecture

KEY FEATURES:
1. Scalable Architecture - Designed for high usage
2. Well-structured Code - Organized project layout

COMPLEXITY LEVEL: Advanced

MVP GUIDANCE:
1. Project Structure - Organize code into modules and packages
2. Dependencies - Manage requirements with pip
3. Documentation - Write docstrings and README files
4. Testing - Implement unit tests with unittest or pytest
5. Packaging - Prepare for distribution with setup.py

IMPLEMENTATION STEPS:
1. Set up Python virtual environment
2. Initialize project directory structure
3. Create main application file
4. Implement core functionality
5. Add required dependencies to requirements.txt
6. Write unit tests for core features
7. Create documentation and usage instructions
8. Set up CI/CD configuration
9. Package application for distribution
10. Test installation and usage
```

### JavaScript Library
```
Build an MVP inspired by: @https://github.com/lodash/lodash

PROJECT TYPE: JavaScript Application
TECH STACK: JavaScript
ARCHITECTURE: Standard application architecture

KEY FEATURES:
1. Well-structured Code - Organized project layout
2. Modular Design - Well-organized code structure

COMPLEXITY LEVEL: Intermediate to Advanced

MVP GUIDANCE:
1. Project Setup - Initialize project with standard structure
2. Dependencies - Manage project dependencies
3. Modular Design - Organize code into logical modules
4. Documentation - Create README and usage instructions
5. Testing - Implement basic testing strategy

IMPLEMENTATION STEPS:
1. Initialize project with standard structure
2. Set up development environment
3. Create main application files
4. Implement core functionality
5. Add documentation and examples
6. Write tests for key features
7. Configure build and deployment
8. Optimize for performance
9. Test across different environments
10. Prepare release package
```

## Tips for Best Results

1. **Use a GitHub Personal Access Token**: For better rate limits, create a token at https://github.com/settings/tokens

2. **Choose Well-Known Repositories**: The tool works best with popular, well-structured repositories that have clear indicators of their technology stack.

3. **Check the Output**: The generated prompts are starting points. You may need to adjust them based on your specific needs.

4. **Combine Multiple Sources**: For complex projects, consider analyzing multiple related repositories to get a fuller picture.

## Common Use Cases

1. **Learning New Technologies**: Understand how popular projects are structured
2. **Bootstrapping Projects**: Create a foundation based on proven architectures
3. **Educational Purposes**: Generate assignments and exercises for students
4. **Project Planning**: Create implementation plans for new features

## Troubleshooting

### API Rate Limit Errors
If you see rate limit errors, create a GitHub personal access token:
1. Go to https://github.com/settings/tokens
2. Generate a new token with public_repo access
3. Add it to your `.env` file or use the `--token` flag

### Repository Not Found
Make sure the repository URL is correct and the repository is public.

### Incorrect Technology Detection
The tool uses heuristics to detect technologies. For more accurate results:
1. Use repositories with clear technology indicators (package.json, requirements.txt, etc.)
2. Check the repository's README for explicit technology mentions