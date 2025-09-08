#!/usr/bin/env python3

"""
Test script to verify the MVP generator changes
"""

import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from github_mvp_generator.github_parser.analyzer import GitHubRepoAnalyzer
from github_mvp_generator.config import GITHUB_TOKEN, AI_PROVIDER
from github_mvp_generator.ai.generator import AIEnhancedGenerator

def test_mvp_generation():
    """Test MVP generation with a sample repository"""
    # Using a popular repository for testing
    test_repo_url = "https://github.com/facebook/react"
    
    try:
        # Initialize analyzer
        analyzer = GitHubRepoAnalyzer(GITHUB_TOKEN)
        
        print(f"Analyzing repository: {test_repo_url}")
        
        # Analyze the repository
        repo_data = analyzer.analyze_repo(test_repo_url)
        
        # Use AI-enhanced generation
        ai_generator = AIEnhancedGenerator(AI_PROVIDER if AI_PROVIDER != 'none' else 'openai')
        prompt = ai_generator.generate_prompt(repo_data, test_repo_url)
        
        print("Generated MVP Prompt:")
        print("="*50)
        print(prompt)
        
        # Check if the prompt contains repository-specific content
        if "facebook/react" in prompt and "React" in prompt:
            print("\n✓ Test passed: Prompt contains repository-specific content")
        else:
            print("\n✗ Test failed: Prompt may not be repository-specific")
            
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    return True

if __name__ == '__main__':
    test_mvp_generation()