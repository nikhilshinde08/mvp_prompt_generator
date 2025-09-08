#!/usr/bin/env python3

"""
GitHub MVP Generator - Turn any GitHub repo into an MVP prompt

This script demonstrates how to use the GitHub MVP Generator tool
to reverse engineer open-source projects into ready-to-use prompts.

Example usage:
    python demo.py https://github.com/facebook/react
"""

import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from github_parser.analyzer import GitHubRepoAnalyzer
from prompt_generator.generator import PromptGenerator
from config import GITHUB_TOKEN

def main():
    # Example 1: Using the actual tool with a GitHub repository
    print("=" * 60)
    print("GITHUB MVP GENERATOR DEMO")
    print("=" * 60)
    
    # Initialize analyzer and generator
    analyzer = GitHubRepoAnalyzer(GITHUB_TOKEN)
    generator = PromptGenerator()
    
    # Example repository (using a simple one to avoid rate limits)
    repo_url = "https://github.com/jlevy/og-equation"
    
    print(f"Analyzing repository: {repo_url}")
    print("-" * 60)
    
    try:
        # Analyze the repository
        repo_data = analyzer.analyze_repo(repo_url)
        
        # Generate the MVP prompt
        prompt = generator.generate_prompt(repo_data, repo_url)
        
        # Output the result
        print("GENERATED MVP PROMPT:")
        print("-" * 60)
        print(prompt)
        
    except Exception as e:
        print(f"Error analyzing repository: {e}")
        print("This might be due to GitHub API rate limits or repository not found.")
    
    print("\n" + "=" * 60)
    print("EXAMPLE OUTPUT FORMAT")
    print("=" * 60)
    
    # Example 2: Show the exact format from the requirements
    from examples.generate_example import generate_example_output
    example_output = generate_example_output()
    print(example_output)

if __name__ == '__main__':
    main()