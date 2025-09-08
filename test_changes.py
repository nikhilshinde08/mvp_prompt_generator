#!/usr/bin/env python3

"""
Simple test to verify the changes to the MVP generator
"""

import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import the modified modules
from github_mvp_generator.ai.templates.prompts import MVP_GUIDANCE_PROMPT, IMPLEMENTATION_STEPS_PROMPT

def test_prompt_templates():
    """Test that the prompt templates have been updated correctly"""
    print("Testing MVP Guidance Prompt Template:")
    print("="*50)
    
    # Check if the MVP guidance prompt has been updated with more detailed requirements
    if "highly detailed" in MVP_GUIDANCE_PROMPT and "6-8 highly detailed repo-specific guidance sections" in MVP_GUIDANCE_PROMPT:
        print("✓ MVP Guidance Prompt has been updated with more detailed requirements")
    else:
        print("✗ MVP Guidance Prompt may not have been updated correctly")
    
    # Check for specific detailed requirements
    if "Descriptive title" in MVP_GUIDANCE_PROMPT and "Complete code snippet" in MVP_GUIDANCE_PROMPT:
        print("✓ MVP Guidance Prompt includes requirements for detailed content")
    else:
        print("✗ MVP Guidance Prompt may be missing detailed content requirements")
        
    print("\nTesting Implementation Steps Prompt Template:")
    print("="*50)
    
    # Check if the implementation steps prompt has been updated with more detailed requirements
    if "12 CONCRETE" in IMPLEMENTATION_STEPS_PROMPT and "extensive detail" in IMPLEMENTATION_STEPS_PROMPT:
        print("✓ Implementation Steps Prompt has been updated with more detailed requirements")
    else:
        print("✗ Implementation Steps Prompt may not have been updated correctly")
    
    # Check for specific detailed requirements
    if "Complete code/config snippet" in IMPLEMENTATION_STEPS_PROMPT and "verification commands" in IMPLEMENTATION_STEPS_PROMPT:
        print("✓ Implementation Steps Prompt includes requirements for detailed content")
    else:
        print("✗ Implementation Steps Prompt may be missing detailed content requirements")

def test_ai_generator_modifications():
    """Test that the AI generator has been modified correctly"""
    # Read the AI generator file
    with open("github_mvp_generator/ai/generator.py", "r") as f:
        content = f.read()
    
    print("\nTesting AI Generator Modifications:")
    print("="*50)
    
    # Check if the new method has been added
    if "generate_detailed_mvp_guidance" in content:
        print("✓ generate_detailed_mvp_guidance method has been added")
    else:
        print("✗ generate_detailed_mvp_guidance method may be missing")
    
    # Check if the _generate_final_format method has been updated
    if "_detailed_mvp_guidance" in content:
        print("✓ _generate_final_format method uses detailed MVP guidance")
    else:
        print("✗ _generate_final_format method may not use detailed MVP guidance")
    
    # Check if the generate_prompt method has been updated
    if "self._detailed_mvp_guidance = detailed_guidance" in content:
        print("✓ generate_prompt method stores detailed guidance for later use")
    else:
        print("✗ generate_prompt method may not store detailed guidance")

if __name__ == '__main__':
    test_prompt_templates()
    test_ai_generator_modifications()
    print("\n" + "="*50)
    print("Test completed. Check the results above.")
