"""Groq provider implementation for the GitHub MVP Generator."""

import os
from groq import Groq
from ai.client import AIProvider


class GroqProvider(AIProvider):
    """Groq provider implementation."""
    
    def __init__(self):
        # Get API key from environment variable
        api_key = os.getenv('GROQ_API_KEY')
        if not api_key:
            raise ValueError("GROQ_API_KEY environment variable not set")
        
        self.client = Groq(api_key=api_key)
        # Use the specified model or default to openai/gpt-oss-120b
        self.model = os.getenv('GROQ_MODEL', 'openai/gpt-oss-120b')
    
    def generate_text(self, prompt: str, **kwargs) -> str:
        """Generate text using Groq's API."""
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