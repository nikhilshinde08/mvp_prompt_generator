"""User preferences system for the GitHub MVP Generator."""

import json
import os
from typing import Dict, Any
from datetime import datetime


class UserPreferences:
    """Manages user preferences and settings."""
    
    def __init__(self, preferences_file: str = "user_preferences.json"):
        self.preferences_file = preferences_file
        self.preferences = self._load_preferences()
    
    def _load_preferences(self) -> Dict[str, Any]:
        """Load existing preferences from file."""
        if os.path.exists(self.preferences_file):
            try:
                with open(self.preferences_file, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return self._get_default_preferences()
        return self._get_default_preferences()
    
    def _get_default_preferences(self) -> Dict[str, Any]:
        """Get default preferences."""
        return {
            "default_provider": "groq",
            "preferred_tech_stacks": [],
            "preferred_project_types": [],
            "last_used": None,
            "usage_count": 0
        }
    
    def _save_preferences(self):
        """Save preferences to file."""
        try:
            with open(self.preferences_file, 'w') as f:
                json.dump(self.preferences, f, indent=2)
        except IOError as e:
            print(f"Warning: Could not save preferences: {e}")
    
    def update_provider_preference(self, provider: str):
        """Update the preferred AI provider."""
        self.preferences["default_provider"] = provider
        self.preferences["last_used"] = datetime.now().isoformat()
        self.preferences["usage_count"] = self.preferences.get("usage_count", 0) + 1
        self._save_preferences()
    
    def add_preferred_tech_stack(self, tech_stack: str):
        """Add a preferred tech stack."""
        if "preferred_tech_stacks" not in self.preferences:
            self.preferences["preferred_tech_stacks"] = []
        
        if tech_stack not in self.preferences["preferred_tech_stacks"]:
            self.preferences["preferred_tech_stacks"].append(tech_stack)
            self._save_preferences()
    
    def add_preferred_project_type(self, project_type: str):
        """Add a preferred project type."""
        if "preferred_project_types" not in self.preferences:
            self.preferences["preferred_project_types"] = []
        
        if project_type not in self.preferences["preferred_project_types"]:
            self.preferences["preferred_project_types"].append(project_type)
            self._save_preferences()
    
    def get_preferred_provider(self) -> str:
        """Get the preferred AI provider."""
        return self.preferences.get("default_provider", "groq")
    
    def get_preferred_tech_stacks(self) -> list:
        """Get preferred tech stacks."""
        return self.preferences.get("preferred_tech_stacks", [])
    
    def get_preferred_project_types(self) -> list:
        """Get preferred project types."""
        return self.preferences.get("preferred_project_types", [])
    
    def get_usage_stats(self) -> Dict[str, Any]:
        """Get usage statistics."""
        return {
            "usage_count": self.preferences.get("usage_count", 0),
            "last_used": self.preferences.get("last_used"),
            "first_used": self.preferences.get("first_used", "Unknown")
        }
    
    def get_all_preferences(self) -> Dict[str, Any]:
        """Get all preferences."""
        return self.preferences


# Global user preferences instance
user_preferences = UserPreferences()