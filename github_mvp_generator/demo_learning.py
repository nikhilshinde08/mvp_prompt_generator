#!/usr/bin/env python3

"""
Demo script for the GitHub MVP Generator learning system.
"""

import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from github_parser.analyzer import GitHubRepoAnalyzer
from config import GITHUB_TOKEN
from feedback import feedback_system
from performance_metrics import performance_metrics
from knowledge_base import knowledge_base
from user_preferences import user_preferences


def demo_learning_system():
    """Demonstrate the learning capabilities of the system."""
    print("GitHub MVP Generator - Learning System Demo")
    print("=" * 50)
    
    # Show initial stats
    print("\nInitial System Stats:")
    kb_stats = knowledge_base.get_knowledge_stats()
    print(f"Knowledge Base Entries: {kb_stats['repo_patterns_count']}")
    
    prefs = user_preferences.get_all_preferences()
    print(f"User Preferences: {prefs.get('usage_count', 0)} previous usages")
    
    # Simulate a repository analysis
    print("\nAnalyzing a sample repository...")
    analyzer = GitHubRepoAnalyzer(GITHUB_TOKEN)
    
    # Start performance tracking
    operation = performance_metrics.start_operation("demo_analysis")
    
    try:
        # Analyze a popular repository
        repo_data = analyzer.analyze_repo("https://github.com/facebook/react")
        print("Repository analysis completed successfully!")
        
        # End performance tracking
        performance_metrics.end_operation(operation, success=True)
        
        # Show what we learned
        print(f"\nWhat we learned from this repository:")
        print(f"  Name: {repo_data.get('name')}")
        print(f"  Language: {repo_data.get('language')}")
        print(f"  Frameworks: {', '.join(repo_data.get('frameworks', []))}")
        print(f"  Stars: {repo_data.get('stars', 0)}")
        
        # Show that we cached this analysis
        kb_stats = knowledge_base.get_knowledge_stats()
        print(f"\nKnowledge Base now has {kb_stats['repo_patterns_count']} cached analyses")
        
    except Exception as e:
        # End performance tracking with error
        performance_metrics.end_operation(operation, success=False, error=str(e))
        print(f"Error during analysis: {e}")
    
    # Show performance metrics
    print("\nPerformance Metrics:")
    perf_summary = performance_metrics.get_performance_summary()
    print(f"  Total Operations: {perf_summary['total_operations']}")
    print(f"  Success Rate: {perf_summary['success_rate']:.2f}%")
    print(f"  Average Response Time: {perf_summary['average_response_time']:.2f}s")
    
    # Show user preferences
    print("\nUser Preferences:")
    prefs = user_preferences.get_all_preferences()
    print(f"  Usage Count: {prefs.get('usage_count', 0)}")
    print(f"  Preferred Provider: {prefs.get('default_provider', 'Not set')}")
    if prefs.get('preferred_tech_stacks'):
        print(f"  Preferred Tech Stacks: {', '.join(prefs.get('preferred_tech_stacks', [])[:3])}")
    if prefs.get('preferred_project_types'):
        print(f"  Preferred Project Types: {', '.join(prefs.get('preferred_project_types', [])[:3])}")
    
    print("\nNext time you run this, the system will:")
    print("  - Use cached analysis for faster results")
    print("  - Apply your preferred settings automatically")
    print("  - Leverage learned patterns for better accuracy")


if __name__ == '__main__':
    demo_learning_system()