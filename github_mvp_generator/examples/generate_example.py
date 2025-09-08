#!/usr/bin/env python3

def generate_example_output():
    # Generate prompt with the exact format from requirements
    project_type = "React Component Library & Todo Application"
    tech_stack = ["React", "TypeScript", "Vite", "Tailwind CSS", "Local Storage"]
    architecture = "Frontend SPA with component-based architecture"
    key_features = [
        "Component System - Reusable UI components with props and state management",
        "State Management - Local state with useState and useEffect hooks",
        "Todo Functionality - Add, edit, delete, and toggle todo items",
        "TypeScript Integration - Full type safety for components and data",
        "Modern Styling - Tailwind CSS for responsive design"
    ]
    complexity = "Beginner to Medium"
    
    # MVP Guidance (from requirements)
    mvp_guidance = [
        "Core Components - Create TodoApp main component with state management",
        "Build TodoItem component for individual tasks",
        "Add TodoForm component for adding new items",
        "Implement TodoList component for rendering items",
        "State Management - Use useState for todos array and form inputs",
        "Implement useEffect for localStorage persistence",
        "Add toggle, delete, and edit functionality",
        "Create custom hooks for todo operations",
        "User Interface - Design clean, minimal UI with Tailwind",
        "Add responsive layout for mobile and desktop",
        "Implement form validation and error states",
        "Create loading states and animations",
        "TypeScript Setup - Define Todo interface with id, text, completed fields",
        "Type all component props and state",
        "Add proper event handler types",
        "Configure strict TypeScript settings",
        "Development Features - Set up Vite for fast development",
        "Add ESLint and Prettier for code quality",
        "Implement hot module replacement",
        "Create development and production builds"
    ]
    
    # Implementation steps (from requirements)
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
    
    # Format the output exactly as specified
    prompt = f"Build an MVP inspired by: @https://github.com/facebook/react\n\n"
    prompt += f"PROJECT TYPE: {project_type}\n"
    prompt += f"TECH STACK: {', '.join(tech_stack)}\n"
    prompt += f"ARCHITECTURE: {architecture}\n\n"
    
    prompt += "KEY FEATURES:\n"
    for i, feature in enumerate(key_features, 1):
        prompt += f"{i}. {feature}\n"
    prompt += "\n"
    
    prompt += f"COMPLEXITY LEVEL: {complexity}\n\n"
    
    prompt += "MVP GUIDANCE:\n"
    for i, guide in enumerate(mvp_guidance, 1):
        # Format with indentation for sub-items
        if " - " in guide and not guide.startswith(("Core Components", "State Management", "User Interface", "TypeScript Setup", "Development Features")):
            prompt += f"   - {guide}\n"
        else:
            prompt += f"{i}. {guide}\n"
    prompt += "\n"
    
    prompt += "IMPLEMENTATION STEPS:\n"
    for i, step in enumerate(implementation_steps, 1):
        prompt += f"{i}. {step}\n"
    prompt += "\n"
    
    prompt += "Focus on creating a clean, functional todo app that demonstrates React's component-based architecture, modern hooks, and TypeScript integration."
    
    return prompt

if __name__ == '__main__':
    # Generate and print the example output
    example_output = generate_example_output()
    print(example_output)