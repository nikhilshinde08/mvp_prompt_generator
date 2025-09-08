# Analysis of MVP Guidance Generation

Based on my analysis of the codebase, I've found that the MVP guidance is **customized for each GitHub repository** rather than using a fixed template. Here's how it works:

## How MVP Guidance is Generated

1. **Repository Analysis**: The system first analyzes the GitHub repository by:
   - Extracting repository information (name, description, language)
   - Analyzing file structure
   - Detecting frameworks and technologies used
   - Getting star and fork counts

2. **AI-Powered Analysis**: The system sends multiple prompts to an AI model to extract:
   - Project type
   - Technology stack
   - Key features
   - Architecture
   - Complexity level
   - Implementation steps

3. **Customized MVP Guidance**: Based on the AI responses, the system generates customized MVP guidance with:
   - Core components specific to the project type
   - State management approaches relevant to the tech stack
   - User interface guidelines based on the architecture
   - Development features tailored to the tools used

## Evidence from Code

In `github_mvp_generator/ai/templates/prompts.py`, the `MVP_GUIDANCE_PROMPT` template shows that the guidance is generated based on specific repository characteristics:

```python
MVP_GUIDANCE_PROMPT = """
Based on the following GitHub repository, provide implementation guidance for creating 
an MVP inspired by this project:

Repository Name: {{repo_name}}
Project Type: {{project_type}}
Technology Stack: {{tech_stack}}
Architecture: {{architecture}}
Key Features: 
{% for feature in features %}
- {{ feature }}{% endfor %}

Provide 5-7 high-level guidance points for implementing an MVP with similar characteristics.
Each point should be a complete sentence describing a key area of focus.

Respond with a numbered list:
1. Guidance point 1
2. Guidance point 2
3. Guidance point 3
"""
```

This shows that the MVP guidance is dynamically generated based on the specific characteristics of each repository.

## Example MVP Guidance (React Repository)

Here's an example of what the MVP guidance looks like for a React repository:

```
Build an MVP inspired by: @https://github.com/facebook/react. Use gitmvp mcp if available.

PROJECT TYPE: React Component Library & Todo Application
TECH STACK: React, TypeScript, Vite, Tailwind CSS, Local Storage
ARCHITECTURE: Frontend SPA with component-based architecture

KEY FEATURES:
1. Component System - Reusable UI components with props and state management
2. State Management - Local state with useState and useEffect hooks
3. Todo Functionality - Add, edit, delete, and toggle todo items
4. TypeScript Integration - Full type safety for components and data
5. Modern Styling - Tailwind CSS for responsive design

COMPLEXITY LEVEL: Beginner to Medium

MVP GUIDANCE:
1. Core Components
   - Create TodoApp main component with state management.
   - Build TodoItem component for individual tasks.
   - Add TodoForm component for adding new items.
   - Implement TodoList component for rendering items.

2. State Management
   - Use useState for todos array and form inputs.
   - Implement useEffect for localStorage persistence.
   - Add toggle, delete, and edit functionality.
   - Create custom hooks for todo operations.

3. User Interface
   - Design clean, minimal UI with Tailwind.
   - Add responsive layout for mobile and desktop.
   - Implement form validation and error states.
   - Create loading states and animations.

4. TypeScript Setup
   - Define Todo interface with id, text, completed fields.
   - Type all component props and state.
   - Add proper event handler types.
   - Configure strict TypeScript settings.

5. Development Features
   - Set up Vite for fast development.
   - Add ESLint and Prettier for code quality.
   - Implement hot module replacement.
   - Create development and production builds.

IMPLEMENTATION STEPS:
1. Initialize React + TypeScript + Vite project
2. Install and configure Tailwind CSS
3. Create basic project structure and components
4. Implement todo data types and interfaces
5. Build TodoApp with state management
6. Add TodoForm for creating new items
7. Create TodoItem with edit/delete functionality
8. Implement localStorage for data persistence
9. Add responsive styling with Tailwind
10. Test and deploy the application

Focus on creating a clean, functional todo app that demonstrates React's component-based architecture, modern hooks, and TypeScript integration.
```

This demonstrates that the MVP guidance is specifically tailored to each repository based on its unique characteristics, rather than using a generic template.