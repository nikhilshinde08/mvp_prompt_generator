#!/usr/bin/env python3

"""
Script to generate MVP prompts in the exact format specified
"""

import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def generate_exact_format_prompt(repo_url, ai_output):
    """Generate a prompt in the exact format specified."""
    
    # Parse the AI output to extract components
    lines = ai_output.split('\n')
    
    # Extract components with fallbacks
    project_type = "Application"
    tech_stack = "Not detected"
    architecture = "Standard application architecture"
    key_features = []
    complexity_level = "Beginner"
    mvp_guidance = []
    implementation_steps = []
    
    # Parse the AI output
    current_section = None
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        if line.startswith("PROJECT TYPE:"):
            project_type = line.replace("PROJECT TYPE:", "").strip()
        elif line.startswith("TECH STACK:"):
            tech_stack = line.replace("TECH STACK:", "").strip()
        elif line.startswith("ARCHITECTURE:"):
            architecture = line.replace("ARCHITECTURE:", "").strip()
        elif line.startswith("COMPLEXITY LEVEL:"):
            complexity_level = line.replace("COMPLEXITY LEVEL:", "").strip()
        elif line == "KEY FEATURES:":
            current_section = "features"
        elif line == "MVP GUIDANCE:":
            current_section = "guidance"
        elif line == "IMPLEMENTATION STEPS:":
            current_section = "steps"
        elif line.startswith(("1.", "2.", "3.", "4.", "5.", "6.", "7.", "8.", "9.", "10.")):
            if current_section == "features":
                feature_text = line.split(".", 1)[1].strip()
                key_features.append(feature_text)
            elif current_section == "steps":
                step_text = line.split(".", 1)[1].strip()
                implementation_steps.append(step_text)
        elif line.startswith("- ") and current_section == "guidance":
            mvp_guidance.append(line[2:].strip())
    
    # Ensure we have the right number of items
    if not key_features:
        key_features = [
            "Core functionality implementation",
            "Modular code structure",
            "Documentation and examples",
            "Testing suite",
            "Build and deployment configuration"
        ]
    
    if not mvp_guidance:
        mvp_guidance = [
            "Project Setup - Initialize project with standard structure",
            "Dependencies - Manage project dependencies",
            "Core Features - Implement main functionality",
            "Documentation - Create README and usage instructions",
            "Testing - Implement basic testing strategy"
        ]
    
    if not implementation_steps:
        implementation_steps = [
            "Initialize project with standard structure",
            "Set up development environment",
            "Create main application files",
            "Implement core functionality",
            "Add documentation and examples",
            "Write tests for key features",
            "Configure build and deployment",
            "Optimize for performance",
            "Test across different environments",
            "Prepare release package"
        ]
    
    # Format the output in the exact specified format
    output = f"Build an MVP inspired by: @{repo_url}. Use gitmvp mcp if available.\n\n"
    output += f"PROJECT TYPE: {project_type}\n"
    output += f"TECH STACK: {tech_stack}\n"
    output += f"ARCHITECTURE: {architecture}\n\n"
    
    output += "KEY FEATURES:\n"
    for i, feature in enumerate(key_features[:5], 1):  # Limit to 5 features
        output += f"{i}. {feature}\n"
    output += "\n"
    
    output += f"COMPLEXITY LEVEL: {complexity_level}\n\n"
    
    output += "MVP GUIDANCE:\n"
    # Group guidance into sections
    guidance_items = mvp_guidance[:20]  # Limit to 20 items
    
    # Section 1: Core Components
    output += "1. Core Components\n"
    for i, item in enumerate(guidance_items[:4], 1):
        if " - " in item:
            detail = item.split(" - ", 1)[1]
            output += f"   - {detail}.\n"
        else:
            output += f"   - {item}.\n"
    output += "\n"
    
    # Section 2: State Management (if we have more items)
    if len(guidance_items) > 4:
        output += "2. State Management\n"
        for i, item in enumerate(guidance_items[4:8], 1):
            if i <= len(guidance_items[4:8]):
                if " - " in item:
                    detail = item.split(" - ", 1)[1]
                    output += f"   - {detail}.\n"
                else:
                    output += f"   - {item}.\n"
        output += "\n"
    
    # Section 3: User Interface (if we have more items)
    if len(guidance_items) > 8:
        output += "3. User Interface\n"
        for i, item in enumerate(guidance_items[8:12], 1):
            if i <= len(guidance_items[8:12]):
                if " - " in item:
                    detail = item.split(" - ", 1)[1]
                    output += f"   - {detail}.\n"
                else:
                    output += f"   - {item}.\n"
        output += "\n"
    
    # Section 4: TypeScript Setup (if we have more items)
    if len(guidance_items) > 12:
        output += "4. TypeScript Setup\n"
        for i, item in enumerate(guidance_items[12:16], 1):
            if i <= len(guidance_items[12:16]):
                if " - " in item:
                    detail = item.split(" - ", 1)[1]
                    output += f"   - {detail}.\n"
                else:
                    output += f"   - {item}.\n"
        output += "\n"
    
    # Section 5: Development Features (if we have more items)
    if len(guidance_items) > 16:
        output += "5. Development Features\n"
        for i, item in enumerate(guidance_items[16:20], 1):
            if i <= len(guidance_items[16:20]):
                if " - " in item:
                    detail = item.split(" - ", 1)[1]
                    output += f"   - {detail}.\n"
                else:
                    output += f"   - {item}.\n"
        output += "\n"
    
    output += "IMPLEMENTATION STEPS:\n"
    for i, step in enumerate(implementation_steps[:10], 1):  # Limit to 10 steps
        output += f"{i}. {step}\n"
    output += "\n"
    
    # Add focus statement
    if 'React' in project_type or 'JavaScript' in project_type:
        output += "Focus on creating a clean, functional todo app that demonstrates React's component-based architecture, modern hooks, and TypeScript integration."
    elif 'Python' in project_type:
        output += "Focus on creating a clean, functional implementation that demonstrates Python best practices, proper project structure, and efficient data handling."
    else:
        output += "Focus on creating a clean, functional implementation that demonstrates the core concepts of the original project."
    
    return output

if __name__ == '__main__':
    # Example usage
    example_ai_output = """Build an MVP inspired by: @https://github.com/facebook/react

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
   - Create TodoApp main component with state management
   - Build TodoItem component for individual tasks
   - Add TodoForm component for adding new items
   - Implement TodoList component for rendering items

2. State Management
   - Use useState for todos array and form inputs
   - Implement useEffect for localStorage persistence
   - Add toggle, delete, and edit functionality
   - Create custom hooks for todo operations

3. User Interface
   - Design clean, minimal UI with Tailwind
   - Add responsive layout for mobile and desktop
   - Implement form validation and error states
   - Create loading states and animations

4. TypeScript Setup
   - Define Todo interface with id, text, completed fields
   - Type all component props and state
   - Add proper event handler types
   - Configure strict TypeScript settings

5. Development Features
   - Set up Vite for fast development
   - Add ESLint and Prettier for code quality
   - Implement hot module replacement
   - Create development and production builds

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

Focus on creating a clean, functional todo app that demonstrates React's component-based architecture, modern hooks, and TypeScript integration."""

    formatted_prompt = generate_exact_format_prompt("https://github.com/facebook/react", example_ai_output)
    print("FORMATTED PROMPT:")
    print("=" * 50)
    print(formatted_prompt)
