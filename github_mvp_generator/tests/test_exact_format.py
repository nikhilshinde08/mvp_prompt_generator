#!/usr/bin/env python3

# Test to verify that our tool generates the exact format specified in the requirements

import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from examples.generate_example import generate_example_output

def test_exact_format():
    """Test that our tool generates the exact format specified in the requirements."""
    output = generate_example_output()
    
    # Check that it contains all the required sections
    assert "Build an MVP inspired by: @https://github.com/facebook/react" in output
    assert "PROJECT TYPE: React Component Library & Todo Application" in output
    assert "TECH STACK: React, TypeScript, Vite, Tailwind CSS, Local Storage" in output
    assert "ARCHITECTURE: Frontend SPA with component-based architecture" in output
    
    # Check that it has the right number of key features
    assert "KEY FEATURES:" in output
    assert "1. Component System - Reusable UI components with props and state management" in output
    assert "2. State Management - Local state with useState and useEffect hooks" in output
    assert "3. Todo Functionality - Add, edit, delete, and toggle todo items" in output
    assert "4. TypeScript Integration - Full type safety for components and data" in output
    assert "5. Modern Styling - Tailwind CSS for responsive design" in output
    
    # Check complexity level
    assert "COMPLEXITY LEVEL: Beginner to Medium" in output
    
    # Check MVP guidance sections
    assert "MVP GUIDANCE:" in output
    assert "1. Core Components - Create TodoApp main component with state management" in output
    assert "2. Build TodoItem component for individual tasks" in output
    assert "3. Add TodoForm component for adding new items" in output
    assert "4. Implement TodoList component for rendering items" in output
    
    # Check implementation steps
    assert "IMPLEMENTATION STEPS:" in output
    assert "1. Initialize React + TypeScript + Vite project" in output
    assert "10. Test and deploy the application" in output
    
    # Check final message
    assert "Focus on creating a clean, functional todo app that demonstrates React's component-based architecture, modern hooks, and TypeScript integration." in output
    
    print("All tests passed! The tool generates the exact format specified in the requirements.")

if __name__ == '__main__':
    test_exact_format()