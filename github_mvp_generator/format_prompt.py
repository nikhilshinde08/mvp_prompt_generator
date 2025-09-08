#!/usr/bin/env python3

"""
Script to generate MVP prompts in the exact format specified
"""

import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from jinja2 import Template

# Template for the exact format you want
MVP_PROMPT_TEMPLATE = """Build an MVP inspired by: @{{repo_url}}. Use gitmvp mcp if available.

PROJECT TYPE: {{project_type}}
TECH STACK: {{tech_stack}}
ARCHITECTURE: {{architecture}}

KEY FEATURES:
{% for feature in key_features %}{{ loop.index }}. {{ feature }}
{% endfor %}
COMPLEXITY LEVEL: {{complexity_level}}

MVP GUIDANCE:
{% for i in range(mvp_guidance|length) %}{% set guidance = mvp_guidance[i] %}{% if i in [0, 5, 10, 15] %}{{ (i // 5) + 1 }}. {{ guidance.split(' - ')[0] if ' - ' in guidance else guidance }}
   - {{ guidance.split(' - ')[1] if ' - ' in guidance else guidance }}.
{% elif i < 20 %}   - {{ guidance }}.
{% endif %}{% endfor %}

IMPLEMENTATION STEPS:
{% for step in implementation_steps %}{{ loop.index }}. {{ step }}
{% endfor %}
Focus on creating a clean, functional {{focus_description}}."""

def generate_example_prompt():
    """Generate an example prompt in the exact format specified."""
    
    # Example data for React repository
    data = {
        'repo_url': 'https://github.com/facebook/react',
        'project_type': 'React Component Library & Todo Application',
        'tech_stack': 'React, TypeScript, Vite, Tailwind CSS, Local Storage',
        'architecture': 'Frontend SPA with component-based architecture',
        'key_features': [
            'Component System - Reusable UI components with props and state management',
            'State Management - Local state with useState and useEffect hooks',
            'Todo Functionality - Add, edit, delete, and toggle todo items',
            'TypeScript Integration - Full type safety for components and data',
            'Modern Styling - Tailwind CSS for responsive design'
        ],
        'complexity_level': 'Beginner to Medium',
        'mvp_guidance': [
            'Core Components - Create TodoApp main component with state management',
            'Build TodoItem component for individual tasks',
            'Add TodoForm component for adding new items',
            'Implement TodoList component for rendering items',
            'State Management - Use useState for todos array and form inputs',
            'Implement useEffect for localStorage persistence',
            'Add toggle, delete, and edit functionality',
            'Create custom hooks for todo operations',
            'User Interface - Design clean, minimal UI with Tailwind',
            'Add responsive layout for mobile and desktop',
            'Implement form validation and error states',
            'Create loading states and animations',
            'TypeScript Setup - Define Todo interface with id, text, completed fields',
            'Type all component props and state',
            'Add proper event handler types',
            'Configure strict TypeScript settings',
            'Development Features - Set up Vite for fast development',
            'Add ESLint and Prettier for code quality',
            'Implement hot module replacement',
            'Create development and production builds'
        ],
        'implementation_steps': [
            'Initialize React + TypeScript + Vite project',
            'Install and configure Tailwind CSS',
            'Create basic project structure and components',
            'Implement todo data types and interfaces',
            'Build TodoApp with state management',
            'Add TodoForm for creating new items',
            'Create TodoItem with edit/delete functionality',
            'Implement localStorage for data persistence',
            'Add responsive styling with Tailwind',
            'Test and deploy the application'
        ],
        'focus_description': 'todo app that demonstrates React\'s component-based architecture, modern hooks, and TypeScript integration'
    }
    
    template = Template(MVP_PROMPT_TEMPLATE)
    return template.render(data)

if __name__ == '__main__':
    # Generate and print the example prompt
    example_prompt = generate_example_prompt()
    print("EXAMPLE PROMPT:")
    print("=" * 50)
    print(example_prompt)
    print("\n" + "=" * 50)