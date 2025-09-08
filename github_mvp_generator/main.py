#!/usr/bin/env python3

"""
GitHub MVP Generator - Turn any GitHub repo into an MVP prompt

This is the main command-line interface for the GitHub MVP Generator.
It analyzes GitHub repositories and generates structured MVP prompts
for bootstrapping new projects based on proven open-source implementations.

Usage:
    python main.py <github_repo_url> [--token GITHUB_TOKEN] [--provider PROVIDER]

Examples:
    python main.py https://github.com/facebook/react
    python main.py https://github.com/tensorflow/tensorflow --token YOUR_TOKEN
    python main.py https://github.com/facebook/react --provider groq
"""

import argparse
import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from github_parser.analyzer import GitHubRepoAnalyzer
from config import GITHUB_TOKEN, AI_PROVIDER
from feedback import feedback_system
from performance_metrics import performance_metrics
from knowledge_base import knowledge_base
from user_preferences import user_preferences

def main():
    parser = argparse.ArgumentParser(
        description='Generate MVP prompts from GitHub repositories',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument('repo_url', help='GitHub repository URL')
    parser.add_argument('--token', help='GitHub personal access token (optional but recommended)')
    parser.add_argument('--provider', choices=['openai', 'groq'], 
                       help='AI provider to use (openai or groq)')
    parser.add_argument('--feedback', nargs=2, metavar=('RATING', 'COMMENTS'),
                       help='Provide feedback on the previous generation (rating 1-5 and comments)')
    parser.add_argument('--stats', action='store_true',
                       help='Show system statistics and performance metrics')
    
    args = parser.parse_args()
    
    # Handle stats request
    if args.stats:
        print("\n" + "="*50)
        print("SYSTEM STATISTICS")
        print("="*50)
        
        # Performance metrics
        perf_summary = performance_metrics.get_performance_summary()
        print(f"\nPerformance Metrics:")
        print(f"  Total Operations: {perf_summary['total_operations']}")
        print(f"  Success Rate: {perf_summary['success_rate']:.2f}%")
        print(f"  Average Response Time: {perf_summary['average_response_time']:.2f}s")
        
        # Knowledge base stats
        kb_stats = knowledge_base.get_knowledge_stats()
        print(f"\nKnowledge Base:")
        print(f"  Framework Signatures: {kb_stats['framework_signatures_count']}")
        print(f"  Successful Prompts: {kb_stats['successful_prompts_count']}")
        print(f"  Repo Patterns: {kb_stats['repo_patterns_count']}")
        print(f"  Tech Stack Combinations: {kb_stats['tech_stack_combinations_count']}")
        
        # User preferences
        prefs = user_preferences.get_all_preferences()
        print(f"\nUser Preferences:")
        print(f"  Default Provider: {prefs.get('default_provider', 'Not set')}")
        print(f"  Usage Count: {prefs.get('usage_count', 0)}")
        print(f"  Preferred Tech Stacks: {len(prefs.get('preferred_tech_stacks', []))}")
        print(f"  Preferred Project Types: {len(prefs.get('preferred_project_types', []))}")
        
        # Feedback summary
        feedback_summary = feedback_system.get_feedback_summary()
        print(f"\nFeedback:")
        print(f"  Total Feedback: {feedback_summary['total_feedback']}")
        print(f"  Average Rating: {feedback_summary['average_rating']:.2f}/5")
        
        return
    
    # Handle feedback submission
    if args.feedback:
        try:
            rating = int(args.feedback[0])
            comments = args.feedback[1]
            # For now, we'll use a placeholder repo URL since we don't have access to the previous one
            # In a more complete implementation, we'd store the last repo URL
            feedback_system.submit_feedback("last_repo", rating, comments)
            print("Feedback submitted successfully!")
            return
        except (ValueError, IndexError):
            print("Error: Invalid feedback format. Use: --feedback RATING COMMENTS")
            sys.exit(1)
    
    # Start performance tracking
    operation = performance_metrics.start_operation("mvp_generation", args.provider or AI_PROVIDER)
    
    # Use provided token or token from config
    github_token = args.token or GITHUB_TOKEN
    
    try:
        # Initialize analyzer
        analyzer = GitHubRepoAnalyzer(github_token)
        
        print(f"Analyzing repository: {args.repo_url}")
        
        # Analyze the repository
        repo_data = analyzer.analyze_repo(args.repo_url)
        
        # Use AI-enhanced generation only
        provider = args.provider or AI_PROVIDER
        if provider == 'none':
            # If no provider specified, default to openai
            provider = 'openai'
            
        from ai.generator import AIEnhancedGenerator
        ai_generator = AIEnhancedGenerator(provider)
        prompt = ai_generator.generate_prompt(repo_data, args.repo_url)
        print(f"Using AI provider: {provider}")
        
        # End performance tracking
        performance_metrics.end_operation(operation, success=True)
        
        # Output the result
        print("\n" + "="*50)
        print("GENERATED MVP PROMPT")
        print("="*50)
        print(prompt)
        
        # Show feedback option
        print("\n" + "="*50)
        print("PROVIDE FEEDBACK")
        print("="*50)
        print("Rate this generation quality (1-5):")
        print("1=Very Poor, 2=Poor, 3=Average, 4=Good, 5=Excellent")
        print("Example: python main.py <repo_url> --feedback 4 'Good structure but missing tech details'")
        print("View stats: python main.py --stats")
        
    except Exception as e:
        # End performance tracking with error
        performance_metrics.end_operation(operation, success=False, error=str(e))
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    main()