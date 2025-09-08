"""Knowledge base system for the GitHub MVP Generator."""

import json
import os
import hashlib
from typing import Dict, Any, List
from datetime import datetime


class KnowledgeBase:
    """Stores and manages learned patterns and successful generations."""
    
    def __init__(self, knowledge_file: str = "knowledge_base.json"):
        self.knowledge_file = knowledge_file
        self.knowledge_data = self._load_knowledge()
    
    def _load_knowledge(self) -> Dict[str, Any]:
        """Load existing knowledge from file."""
        if os.path.exists(self.knowledge_file):
            try:
                with open(self.knowledge_file, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return self._get_default_knowledge()
        return self._get_default_knowledge()
    
    def _get_default_knowledge(self) -> Dict[str, Any]:
        """Get default knowledge structure."""
        return {
            "framework_signatures": {},
            "successful_prompts": {},
            "repo_patterns": {},
            "tech_stack_combinations": {},
            "last_updated": datetime.now().isoformat()
        }
    
    def _save_knowledge(self):
        """Save knowledge to file."""
        self.knowledge_data["last_updated"] = datetime.now().isoformat()
        try:
            with open(self.knowledge_file, 'w') as f:
                json.dump(self.knowledge_data, f, indent=2)
        except IOError as e:
            print(f"Warning: Could not save knowledge base: {e}")
    
    def _get_repo_hash(self, repo_url: str) -> str:
        """Generate a hash for a repository URL."""
        return hashlib.md5(repo_url.encode()).hexdigest()
    
    def store_framework_signature(self, language: str, frameworks: List[str], signature: Dict[str, Any]):
        """Store a framework signature for a language/framework combination."""
        key = f"{language}:{','.join(frameworks)}"
        if "framework_signatures" not in self.knowledge_data:
            self.knowledge_data["framework_signatures"] = {}
        
        self.knowledge_data["framework_signatures"][key] = {
            "signature": signature,
            "timestamp": datetime.now().isoformat(),
            "language": language,
            "frameworks": frameworks
        }
        self._save_knowledge()
    
    def get_framework_signature(self, language: str, frameworks: List[str]) -> Dict[str, Any]:
        """Retrieve a framework signature."""
        key = f"{language}:{','.join(frameworks)}"
        return self.knowledge_data.get("framework_signatures", {}).get(key, {}).get("signature", {})
    
    def store_successful_prompt(self, repo_url: str, prompt_data: Dict[str, Any], rating: int = 5):
        """Store a successful prompt generation."""
        repo_hash = self._get_repo_hash(repo_url)
        if "successful_prompts" not in self.knowledge_data:
            self.knowledge_data["successful_prompts"] = {}
        
        self.knowledge_data["successful_prompts"][repo_hash] = {
            "repo_url": repo_url,
            "prompt_data": prompt_data,
            "rating": rating,
            "timestamp": datetime.now().isoformat()
        }
        self._save_knowledge()
    
    def get_successful_prompt(self, repo_url: str) -> Dict[str, Any]:
        """Retrieve a successful prompt generation."""
        repo_hash = self._get_repo_hash(repo_url)
        return self.knowledge_data.get("successful_prompts", {}).get(repo_hash, {})
    
    def store_repo_pattern(self, repo_url: str, pattern_data: Dict[str, Any]):
        """Store a repository pattern."""
        repo_hash = self._get_repo_hash(repo_url)
        if "repo_patterns" not in self.knowledge_data:
            self.knowledge_data["repo_patterns"] = {}
        
        self.knowledge_data["repo_patterns"][repo_hash] = {
            "repo_url": repo_url,
            "pattern_data": pattern_data,
            "timestamp": datetime.now().isoformat()
        }
        self._save_knowledge()
    
    def get_repo_pattern(self, repo_url: str) -> Dict[str, Any]:
        """Retrieve a repository pattern."""
        repo_hash = self._get_repo_hash(repo_url)
        return self.knowledge_data.get("repo_patterns", {}).get(repo_hash, {})
    
    def store_tech_stack_combination(self, tech_stack: str, project_type: str, success_count: int = 1):
        """Store a successful tech stack combination."""
        if "tech_stack_combinations" not in self.knowledge_data:
            self.knowledge_data["tech_stack_combinations"] = {}
        
        key = f"{tech_stack}:{project_type}"
        if key in self.knowledge_data["tech_stack_combinations"]:
            # Increment success count
            current_count = self.knowledge_data["tech_stack_combinations"][key].get("success_count", 0)
            self.knowledge_data["tech_stack_combinations"][key]["success_count"] = current_count + success_count
        else:
            self.knowledge_data["tech_stack_combinations"][key] = {
                "tech_stack": tech_stack,
                "project_type": project_type,
                "success_count": success_count,
                "timestamp": datetime.now().isoformat()
            }
        self._save_knowledge()
    
    def get_best_tech_stacks_for_project_type(self, project_type: str, limit: int = 5) -> List[Dict[str, Any]]:
        """Get the best tech stacks for a project type based on success count."""
        combinations = []
        for key, data in self.knowledge_data.get("tech_stack_combinations", {}).items():
            if data.get("project_type") == project_type:
                combinations.append(data)
        
        # Sort by success count
        combinations.sort(key=lambda x: x.get("success_count", 0), reverse=True)
        return combinations[:limit]
    
    def get_knowledge_stats(self) -> Dict[str, Any]:
        """Get statistics about the knowledge base."""
        return {
            "framework_signatures_count": len(self.knowledge_data.get("framework_signatures", {})),
            "successful_prompts_count": len(self.knowledge_data.get("successful_prompts", {})),
            "repo_patterns_count": len(self.knowledge_data.get("repo_patterns", {})),
            "tech_stack_combinations_count": len(self.knowledge_data.get("tech_stack_combinations", {})),
            "last_updated": self.knowledge_data.get("last_updated")
        }


# Global knowledge base instance
knowledge_base = KnowledgeBase()