"""OpenAI provider implementation for the GitHub MVP Generator."""

import os
from typing import Dict, Any
from openai import OpenAI
from ai.client import AIProvider
from config import GITHUB_TOKEN


class OpenAIProvider(AIProvider):
    """OpenAI provider implementation."""
    
    def __init__(self):
        # Get API key from environment variable
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable not set")
        
        self.client = OpenAI(api_key=api_key)
        self.model = os.getenv('OPENAI_MODEL', 'gpt-4o-mini')
    
    def generate_text(self, prompt: str, **kwargs) -> str:
        """Generate text using OpenAI's API."""
        # Default parameters
        params = {
            'model': self.model,
            'messages': [{'role': 'user', 'content': prompt}],
            'temperature': 0.7,
            'max_tokens': 1000,
        }
        
        # Override with any provided parameters
        params.update(kwargs)
        
        response = self.client.chat.completions.create(**params)
        return response.choices[0].message.content.strip()
    
    def get_model_name(self) -> str:
        """Get the name of the model being used."""
        return self.model