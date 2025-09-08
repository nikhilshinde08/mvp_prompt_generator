"""AI client abstraction for the GitHub MVP Generator."""

from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional
import os
from config import GITHUB_TOKEN


class AIProvider(ABC):
    """Abstract base class for AI providers."""
    
    @abstractmethod
    def generate_text(self, prompt: str, **kwargs) -> str:
        """Generate text using the AI model."""
        pass
    
    @abstractmethod
    def get_model_name(self) -> str:
        """Get the name of the model being used."""
        pass


class AIClient:
    """AI client that can use different providers."""
    
    def __init__(self, provider: str = "openai"):
        self.provider = provider
        self._client = self._initialize_client()
    
    def _initialize_client(self) -> AIProvider:
        """Initialize the appropriate AI provider client."""
        if self.provider == "openai":
            from ai.providers.openai import OpenAIProvider
            return OpenAIProvider()
        elif self.provider == "groq":
            from ai.providers.groq import GroqProvider
            return GroqProvider()
        else:
            raise ValueError(f"Unsupported AI provider: {self.provider}")
    
    def generate_text(self, prompt: str, **kwargs) -> str:
        """Generate text using the configured AI provider."""
        try:
            return self._client.generate_text(prompt, **kwargs)
        except Exception as e:
            print(f"Warning: AI generation failed with {self.provider}: {e}")
            print("Falling back to rule-based generation")
            raise e  # Re-raise to be handled by caller
    
    def get_model_name(self) -> str:
        """Get the name of the model being used."""
        return self._client.get_model_name()