"""Adaptive prompt system for the GitHub MVP Generator."""

import json
import os
from typing import Dict, Any, List
from datetime import datetime


class AdaptivePromptSystem:
    """Adapts prompt generation based on feedback and usage patterns."""
    
    def __init__(self, adaptive_file: str = "adaptive_prompts.json"):
        self.adaptive_file = adaptive_file
        self.adaptive_data = self._load_adaptive_data()
    
    def _load_adaptive_data(self) -> Dict[str, Any]:
        """Load existing adaptive data from file."""
        if os.path.exists(self.adaptive_file):
            try:
                with open(self.adaptive_file, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return self._get_default_adaptive_data()
        return self._get_default_adaptive_data()
    
    def _get_default_adaptive_data(self) -> Dict[str, Any]:
        """Get default adaptive data structure."""
        return {
            "prompt_templates": {},
            "feedback_adjustments": {},
            "success_patterns": {},
            "last_updated": datetime.now().isoformat()
        }
    
    def _save_adaptive_data(self):
        """Save adaptive data to file."""
        self.adaptive_data["last_updated"] = datetime.now().isoformat()
        try:
            with open(self.adaptive_file, 'w') as f:
                json.dump(self.adaptive_data, f, indent=2)
        except IOError as e:
            print(f"Warning: Could not save adaptive data: {e}")
    
    def adjust_prompt_template(self, template_name: str, feedback_rating: int, 
                             feedback_comments: str = ""):
        """Adjust a prompt template based on feedback."""
        if "feedback_adjustments" not in self.adaptive_data:
            self.adaptive_data["feedback_adjustments"] = {}
        
        if template_name not in self.adaptive_data["feedback_adjustments"]:
            self.adaptive_data["feedback_adjustments"][template_name] = {
                "total_rating": 0,
                "feedback_count": 0,
                "comments": [],
                "adjustments": []
            }
        
        # Update feedback stats
        self.adaptive_data["feedback_adjustments"][template_name]["total_rating"] += feedback_rating
        self.adaptive_data["feedback_adjustments"][template_name]["feedback_count"] += 1
        
        # Store comments if provided
        if feedback_comments:
            self.adaptive_data["feedback_adjustments"][template_name]["comments"].append({
                "rating": feedback_rating,
                "comment": feedback_comments,
                "timestamp": datetime.now().isoformat()
            })
        
        self._save_adaptive_data()
    
    def get_template_performance(self, template_name: str) -> Dict[str, Any]:
        """Get performance metrics for a template."""
        template_data = self.adaptive_data.get("feedback_adjustments", {}).get(template_name, {})
        if not template_data:
            return {"average_rating": 0, "feedback_count": 0}
        
        feedback_count = template_data.get("feedback_count", 0)
        total_rating = template_data.get("total_rating", 0)
        average_rating = total_rating / feedback_count if feedback_count > 0 else 0
        
        return {
            "average_rating": average_rating,
            "feedback_count": feedback_count,
            "comments": template_data.get("comments", [])
        }
    
    def store_successful_pattern(self, pattern_key: str, pattern_data: Dict[str, Any]):
        """Store a successful generation pattern."""
        if "success_patterns" not in self.adaptive_data:
            self.adaptive_data["success_patterns"] = {}
        
        self.adaptive_data["success_patterns"][pattern_key] = {
            "pattern_data": pattern_data,
            "timestamp": datetime.now().isoformat(),
            "success_count": self.adaptive_data["success_patterns"].get(pattern_key, {}).get("success_count", 0) + 1
        }
        self._save_adaptive_data()
    
    def get_success_patterns(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Get the most successful patterns."""
        patterns = []
        for key, data in self.adaptive_data.get("success_patterns", {}).items():
            patterns.append({
                "key": key,
                "data": data.get("pattern_data", {}),
                "success_count": data.get("success_count", 0),
                "timestamp": data.get("timestamp")
            })
        
        # Sort by success count
        patterns.sort(key=lambda x: x["success_count"], reverse=True)
        return patterns[:limit]
    
    def adapt_prompt_based_on_feedback(self, template_name: str, current_prompt: str) -> str:
        """Adapt a prompt based on feedback patterns."""
        # This is a simplified implementation
        # In a real system, this would use more sophisticated NLP techniques
        template_performance = self.get_template_performance(template_name)
        
        # If we have enough feedback and it's mostly positive, we can reinforce the pattern
        if template_performance["feedback_count"] > 3 and template_performance["average_rating"] > 4:
            # Store this as a successful pattern
            pattern_key = f"{template_name}_{int(template_performance['average_rating'] * 10)}"
            self.store_successful_pattern(pattern_key, {
                "template_name": template_name,
                "prompt": current_prompt,
                "average_rating": template_performance["average_rating"]
            })
        
        # If we have negative feedback, we might want to adjust
        # For now, we'll just return the original prompt
        return current_prompt
    
    def get_adaptation_stats(self) -> Dict[str, Any]:
        """Get statistics about prompt adaptations."""
        return {
            "templates_with_feedback": len(self.adaptive_data.get("feedback_adjustments", {})),
            "successful_patterns": len(self.adaptive_data.get("success_patterns", {})),
            "last_updated": self.adaptive_data.get("last_updated")
        }


# Global adaptive prompt system instance
adaptive_prompt_system = AdaptivePromptSystem()