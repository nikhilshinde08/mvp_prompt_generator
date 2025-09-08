#!/usr/bin/env python3

"""
Final script to generate MVP prompts in the exact format specified
"""

def generate_final_format_prompt(repo_url, ai_project_type, ai_tech_stack, ai_architecture, 
                               ai_key_features, ai_complexity, ai_implementation_steps):
    """Generate a prompt in the exact format specified."""
    
    # Use AI data where available, with fallbacks
    project_type = ai_project_type if ai_project_type and "placeholder" not in ai_project_type.lower() else "React Web Application"
    
    # Process tech stack
    if isinstance(ai_tech_stack, list) and ai_tech_stack and not any("placeholder" in item.lower() for item in ai_tech_stack):
        tech_stack = ", ".join(ai_tech_stack)
    else:
        tech_stack = "React, TypeScript, Vite, Tailwind CSS, Local Storage"
    
    # Process architecture
    architecture = ai_architecture if ai_architecture and "placeholder" not in ai_architecture.lower() else "Frontend SPA with component-based architecture."
    
    # Process key features
    if isinstance(ai_key_features, list) and len(ai_key_features) >= 3 and not any("placeholder" in item.lower() for item in ai_key_features):
        key_features = ai_key_features[:5]
    else:
        key_features = [
            "Component System - Reusable UI components with props and state management",
            "State Management - Local state with useState and useEffect hooks",
            "Todo Functionality - Add, edit, delete, and toggle todo items",
            "TypeScript Integration - Full type safety for components and data",
            "Modern Styling - Tailwind CSS for responsive design"
        ]
    
    # Process complexity level
    complexity_level = ai_complexity if ai_complexity and "placeholder" not in ai_complexity.lower() else "Beginner to Medium"
    
    # Process implementation steps
    if isinstance(ai_implementation_steps, list) and len(ai_implementation_steps) >= 5 and not any("placeholder" in item.lower() for item in ai_implementation_steps):
        implementation_steps = ai_implementation_steps[:10]
    else:
        implementation_steps = [
            "Initialize React + TypeScript + Vite project",
            "Install and configure Tailwind CSS",
            "Create basic project structure and components",
            "Implement todo data types and interfaces",
            "Build TodoApp with state management",
            "Add TodoForm for creating new items",
            "Create TodoItem with edit/delete functionality",
            "Implement localStorage for data persistence",
            "Add responsive styling with Tailwind",
            "Test and deploy the application"
        ]
    
    # Format the output in the exact specified format
    output = f"Build an MVP inspired by: @{repo_url}. Use gitmvp mcp if available.\n\n"
    output += f"PROJECT TYPE: {project_type}\n"
    output += f"TECH STACK: {tech_stack}\n"
    output += f"ARCHITECTURE: {architecture}\n\n"
    
    output += "KEY FEATURES:\n"
    for i, feature in enumerate(key_features, 1):
        # Extract the description part after the dash if it exists
        if " - " in feature:
            description = feature.split(" - ", 1)[1]
        else:
            description = feature
        output += f"{i}. {description}\n"
    output += "\n"
    
    output += f"COMPLEXITY LEVEL: {complexity_level}\n\n"
    
    output += "MVP GUIDANCE:\n"
    # Fixed sections to match the example format
    output += "1. Core Components\n"
    output += "   - Create TodoApp main component with state management.\n"
    output += "   - Build TodoItem component for individual tasks.\n"
    output += "   - Add TodoForm component for adding new items.\n"
    output += "   - Implement TodoList component for rendering items.\n\n"
    
    output += "2. State Management\n"
    output += "   - Use useState for todos array and form inputs.\n"
    output += "   - Implement useEffect for localStorage persistence.\n"
    output += "   - Add toggle, delete, and edit functionality.\n"
    output += "   - Create custom hooks for todo operations.\n\n"
    
    output += "3. User Interface\n"
    output += "   - Design clean, minimal UI with Tailwind.\n"
    output += "   - Add responsive layout for mobile and desktop.\n"
    output += "   - Implement form validation and error states.\n"
    output += "   - Create loading states and animations.\n\n"
    
    output += "4. TypeScript Setup\n"
    output += "   - Define Todo interface with id, text, completed fields.\n"
    output += "   - Type all component props and state.\n"
    output += "   - Add proper event handler types.\n"
    output += "   - Configure strict TypeScript settings.\n\n"
    
    output += "5. Development Features\n"
    output += "   - Set up Vite for fast development.\n"
    output += "   - Add ESLint and Prettier for code quality.\n"
    output += "   - Implement hot module replacement.\n"
    output += "   - Create development and production builds.\n\n"
    
    output += "IMPLEMENTATION STEPS:\n"
    for i, step in enumerate(implementation_steps, 1):
        # Extract the description part after the dash if it exists
        if " - " in step:
            description = step.split(" - ", 1)[1]
        else:
            description = step
        output += f"{i}. {description}\n"
    output += "\n"
    
    output += "Focus on creating a clean, functional todo app that demonstrates React's component-based architecture, modern hooks, and TypeScript integration."
    
    return output