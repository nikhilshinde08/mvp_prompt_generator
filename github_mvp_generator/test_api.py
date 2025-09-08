#!/usr/bin/env python3

"""
Test script for the GitHub MVP Generator API endpoints.
"""

import requests
import json

# API base URL
BASE_URL = "http://localhost:5000"

def test_api_endpoints():
    """Test the API endpoints"""
    print("Testing GitHub MVP Generator API")
    print("=" * 40)
    
    # Test home endpoint
    print("\n1. Testing home endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/")
        print(f"   Status Code: {response.status_code}")
        print(f"   Response: {response.json()}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Test stats endpoint
    print("\n2. Testing stats endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/api/stats")
        print(f"   Status Code: {response.status_code}")
        if response.status_code == 200:
            stats = response.json()
            print(f"   Total Operations: {stats.get('performance', {}).get('total_operations', 0)}")
            print(f"   Knowledge Base Entries: {stats.get('knowledge_base', {}).get('repo_patterns_count', 0)}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Test preferences endpoint
    print("\n3. Testing preferences endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/api/preferences")
        print(f"   Status Code: {response.status_code}")
        if response.status_code == 200:
            prefs = response.json()
            print(f"   Default Provider: {prefs.get('default_provider', 'Not set')}")
            print(f"   Usage Count: {prefs.get('usage_count', 0)}")
    except Exception as e:
        print(f"   Error: {e}")
    
    print("\nAPI tests completed!")

if __name__ == '__main__':
    test_api_endpoints()