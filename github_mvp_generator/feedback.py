"""Feedback system for the GitHub MVP Generator."""

import json
import os
from typing import Dict, Any
from datetime import datetime


class FeedbackSystem:
    """Collects and manages user feedback on generated prompts."""
    
    def __init__(self, feedback_file: str = "feedback.json"):
        self.feedback_file = feedback_file
        self.feedback_data = self._load_feedback()
    
    def _load_feedback(self) -> Dict[str, Any]:
        """Load existing feedback data from file."""
        if os.path.exists(self.feedback_file):
            try:
                with open(self.feedback_file, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return {"feedback_entries": []}
        return {"feedback_entries": []}
    
    def _save_feedback(self):
        """Save feedback data to file."""
        try:
            with open(self.feedback_file, 'w') as f:
                json.dump(self.feedback_data, f, indent=2)
        except IOError as e:
            print(f"Warning: Could not save feedback data: {e}")
    
    def submit_feedback(self, repo_url: str, rating: int, comments: str = "", 
                       improvements: str = ""):
        """Submit feedback for a generated prompt.
        
        Args:
            repo_url: The GitHub repository URL
            rating: Rating from 1-5 (1=poor, 5=excellent)
            comments: General comments about the prompt
            improvements: Specific suggestions for improvement
        """
        if not 1 <= rating <= 5:
            raise ValueError("Rating must be between 1 and 5")
        
        feedback_entry = {
            "timestamp": datetime.now().isoformat(),
            "repo_url": repo_url,
            "rating": rating,
            "comments": comments,
            "improvements": improvements
        }
        
        self.feedback_data["feedback_entries"].append(feedback_entry)
        self._save_feedback()
        
        # Print confirmation
        print(f"Feedback submitted for {repo_url} (Rating: {rating}/5)")
    
    def get_average_rating(self) -> float:
        """Calculate the average rating of all feedback."""
        entries = self.feedback_data["feedback_entries"]
        if not entries:
            return 0.0
        
        total_rating = sum(entry["rating"] for entry in entries)
        return total_rating / len(entries)
    
    def get_feedback_summary(self) -> Dict[str, Any]:
        """Get a summary of all feedback."""
        entries = self.feedback_data["feedback_entries"]
        if not entries:
            return {"total_feedback": 0, "average_rating": 0.0}
        
        ratings = [entry["rating"] for entry in entries]
        rating_counts = {i: ratings.count(i) for i in range(1, 6)}
        
        return {
            "total_feedback": len(entries),
            "average_rating": self.get_average_rating(),
            "rating_distribution": rating_counts,
            "recent_feedback": entries[-5:]  # Last 5 entries
        }
    
    def get_feedback_for_repo(self, repo_url: str) -> list:
        """Get all feedback entries for a specific repository."""
        return [
            entry for entry in self.feedback_data["feedback_entries"]
            if entry["repo_url"] == repo_url
        ]


# Global feedback system instance
feedback_system = FeedbackSystem()