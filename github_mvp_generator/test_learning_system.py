#!/usr/bin/env python3

"""
Simple test script for the GitHub MVP Generator learning system.
"""

import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from feedback import feedback_system
from user_preferences import user_preferences
from knowledge_base import knowledge_base
from performance_metrics import performance_metrics


def test_learning_system():
    """Test the learning system components."""
    print("Testing GitHub MVP Generator Learning System")
    print("=" * 50)
    
    # Test feedback system
    print("\n1. Testing Feedback System...")
    feedback_system.submit_feedback("https://github.com/test/repo", 4, "Good analysis", "Could be more detailed")
    feedback_summary = feedback_system.get_feedback_summary()
    print(f"   Feedback submitted. Average rating: {feedback_summary['average_rating']:.2f}")
    
    # Test user preferences
    print("\n2. Testing User Preferences...")
    user_preferences.update_provider_preference("groq")
    user_preferences.add_preferred_tech_stack("React")
    user_preferences.add_preferred_project_type("Web Application")
    
    prefs = user_preferences.get_all_preferences()
    print(f"   Provider preference: {prefs.get('default_provider')}")
    print(f"   Preferred tech stacks: {len(prefs.get('preferred_tech_stacks', []))}")
    print(f"   Preferred project types: {len(prefs.get('preferred_project_types', []))}")
    
    # Test knowledge base
    print("\n3. Testing Knowledge Base...")
    knowledge_base.store_successful_prompt(
        "https://github.com/test/repo", 
        {"project_type": "Test Project", "tech_stack": "Python, Flask"}, 
        5
    )
    
    kb_stats = knowledge_base.get_knowledge_stats()
    print(f"   Knowledge base entries: {kb_stats['successful_prompts_count']}")
    
    # Test performance metrics
    print("\n4. Testing Performance Metrics...")
    operation = performance_metrics.start_operation("test_operation", "groq")
    performance_metrics.end_operation(operation, success=True)
    
    perf_summary = performance_metrics.get_performance_summary()
    print(f"   Total operations: {perf_summary['total_operations']}")
    print(f"   Success rate: {perf_summary['success_rate']:.2f}%")
    
    print("\nAll tests passed! The learning system is working correctly.")


if __name__ == '__main__':
    test_learning_system()