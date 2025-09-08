#!/usr/bin/env python3

"""
Script to display the actual prompts sent to the AI model
"""

import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from jinja2 import Template
from ai.templates.prompts import (
    PROJECT_TYPE_PROMPT,
    TECH_STACK_PROMPT,
    FEATURES_PROMPT,
    ARCHITECTURE_PROMPT,
    COMPLEXITY_PROMPT,
    MVP_GUIDANCE_PROMPT,
    IMPLEMENTATION_STEPS_PROMPT
)

def render_template(template_str, context):
    """Render a Jinja2 template with the given context."""
    template = Template(template_str)
    return template.render(context)

def show_prompts():
    """Show examples of the prompts that are sent to the AI model."""
    
    # Sample repository data
    sample_repo_data = {
        'name': 'facebook/react',
        'language': 'JavaScript',
        'frameworks': ['React'],
        'description': 'A declarative, efficient, and flexible JavaScript library for building user interfaces.',
        'contents': [
            {'name': 'package.json'},
            {'name': 'README.md'},
            {'name': 'src'},
            {'name': 'examples'},
            {'name': 'public'},
        ],
        'stars': 200000,
        'forks': 40000
    }
    
    project_type_context = {
        'repo_name': sample_repo_data['name'],
        'language': sample_repo_data['language'],
        'frameworks': ', '.join(sample_repo_data['frameworks']),
        'description': sample_repo_data['description'],
        'contents': sample_repo_data['contents'][:20]
    }
    
    print("=" * 60)
    print("PROJECT TYPE PROMPT")
    print("=" * 60)
    prompt = render_template(PROJECT_TYPE_PROMPT, project_type_context)
    print(prompt)
    
    print("\n" + "=" * 60)
    print("TECH STACK PROMPT")
    print("=" * 60)
    prompt = render_template(TECH_STACK_PROMPT, project_type_context)
    print(prompt)
    
    print("\n" + "=" * 60)
    print("FEATURES PROMPT")
    print("=" * 60)
    features_context = project_type_context.copy()
    features_context['stars'] = sample_repo_data['stars']
    features_context['forks'] = sample_repo_data['forks']
    prompt = render_template(FEATURES_PROMPT, features_context)
    print(prompt)
    
    print("\n" + "=" * 60)
    print("ARCHITECTURE PROMPT")
    print("=" * 60)
    prompt = render_template(ARCHITECTURE_PROMPT, project_type_context)
    print(prompt)
    
    print("\n" + "=" * 60)
    print("COMPLEXITY PROMPT")
    print("=" * 60)
    prompt = render_template(COMPLEXITY_PROMPT, features_context)
    print(prompt)
    
    # Sample results for MVP guidance
    sample_results = {
        'project_type': 'JavaScript UI Library',
        'tech_stack': ['JavaScript', 'React', 'Node.js'],
        'architecture': 'Component-based architecture',
        'key_features': [
            'Declarative component-based UI rendering',
            'Efficient Virtual DOM diffing and updates',
            'Cross-platform support'
        ]
    }
    
    print("\n" + "=" * 60)
    print("MVP GUIDANCE PROMPT")
    print("=" * 60)
    mvp_guidance_context = {
        'repo_name': sample_repo_data['name'],
        'project_type': sample_results['project_type'],
        'tech_stack': ', '.join(sample_results['tech_stack']),
        'architecture': sample_results['architecture'],
        'features': sample_results['key_features']
    }
    prompt = render_template(MVP_GUIDANCE_PROMPT, mvp_guidance_context)
    print(prompt)
    
    print("\n" + "=" * 60)
    print("IMPLEMENTATION STEPS PROMPT")
    print("=" * 60)
    prompt = render_template(IMPLEMENTATION_STEPS_PROMPT, mvp_guidance_context)
    print(prompt)

if __name__ == '__main__':
    show_prompts()
