"""AI-enhanced prompt generator for the GitHub MVP Generator."""

from typing import Dict, List, Any
from jinja2 import Template
from ai.client import AIClient
from ai.templates.prompts import (
    PROJECT_TYPE_PROMPT,
    TECH_STACK_PROMPT,
    FEATURES_PROMPT,
    ARCHITECTURE_PROMPT,
    COMPLEXITY_PROMPT,
    MVP_GUIDANCE_PROMPT,
    IMPLEMENTATION_STEPS_PROMPT
)
from user_preferences import user_preferences
from adaptive_prompt import adaptive_prompt_system


class AIEnhancedGenerator:
    """AI-enhanced MVP prompt generator."""
    
    def __init__(self, provider: str = "openai"):
        self.ai_client = AIClient(provider)
        # Update user preferences with the provider used
        user_preferences.update_provider_preference(provider)
    
    def _render_template(self, template_str: str, context: Dict[str, Any]) -> str:
        """Render a Jinja2 template with the given context."""
        template = Template(template_str)
        return template.render(context)
    
    def _parse_numbered_list(self, text: str) -> List[str]:
        """Parse a numbered list from AI response."""
        if not text:
            return []
        lines = text.strip().split('\n')
        items = []
        for line in lines:
            line = line.strip()
            if line and (line[0].isdigit() or (len(line) > 2 and line[1] == '.')):
                # Remove the number and period
                item = line.split('.', 1)[1].strip() if '.' in line else line
                items.append(item)
        return items
    
    def _parse_comma_separated(self, text: str) -> List[str]:
        """Parse a comma-separated list from AI response."""
        if not text:
            return []
        # Split by comma and clean up each item
        items = [item.strip() for item in text.split(',')]
        # Remove empty items
        return [item for item in items if item]
    
    def _clean_response(self, text: str) -> str:
        """Clean AI response text."""
        if not text:
            return ""
        # Take the first line and clean it
        first_line = text.strip().split('\n')[0].strip()
        # Remove any markdown or extra formatting
        cleaned = first_line.replace("**", "").replace("*", "").strip()
        return cleaned
    
    def determine_project_type(self, repo_data: Dict[str, Any]) -> str:
        """Determine project type using AI analysis."""
        context = {
            'repo_name': repo_data.get('name', ''),
            'language': repo_data.get('language', ''),
            'frameworks': ', '.join(repo_data.get('frameworks', [])),
            'description': repo_data.get('description', '') or '',
            'contents': repo_data.get('contents', [])[:20]  # Limit to first 20 items
        }
        
        # Adapt prompt based on feedback
        adapted_prompt = adaptive_prompt_system.adapt_prompt_based_on_feedback(
            "PROJECT_TYPE_PROMPT", PROJECT_TYPE_PROMPT)
        
        try:
            prompt = self._render_template(adapted_prompt, context)
            response = self.ai_client.generate_text(prompt)
            cleaned_response = self._clean_response(response)
            # Filter out placeholder responses
            if cleaned_response and "placeholder" not in cleaned_response.lower() and "___________" not in cleaned_response:
                # Update user preferences with the project type
                user_preferences.add_preferred_project_type(cleaned_response)
                return cleaned_response
        except:
            pass
        return ""
    
    def determine_tech_stack(self, repo_data: Dict[str, Any]) -> List[str]:
        """Determine technology stack using AI analysis."""
        context = {
            'repo_name': repo_data.get('name', ''),
            'language': repo_data.get('language', ''),
            'frameworks': ', '.join(repo_data.get('frameworks', [])),
            'description': repo_data.get('description', '') or '',
            'contents': repo_data.get('contents', [])[:20]  # Limit to first 20 items
        }
        
        # Adapt prompt based on feedback
        adapted_prompt = adaptive_prompt_system.adapt_prompt_based_on_feedback(
            "TECH_STACK_PROMPT", TECH_STACK_PROMPT)
        
        try:
            prompt = self._render_template(adapted_prompt, context)
            response = self.ai_client.generate_text(prompt)
            tech_stack = self._parse_comma_separated(response)
            # Filter out placeholder responses
            if tech_stack and not any("placeholder" in item.lower() or "___________" in item for item in tech_stack):
                # Update user preferences with the tech stack
                for tech in tech_stack:
                    user_preferences.add_preferred_tech_stack(tech)
                return tech_stack
        except:
            pass
        return []
    
    def determine_architecture(self, repo_data: Dict[str, Any]) -> str:
        """Determine architecture using AI analysis."""
        context = {
            'repo_name': repo_data.get('name', ''),
            'language': repo_data.get('language', ''),
            'frameworks': ', '.join(repo_data.get('frameworks', [])),
            'description': repo_data.get('description', '') or '',
            'contents': repo_data.get('contents', [])[:20]  # Limit to first 20 items
        }
        
        # Adapt prompt based on feedback
        adapted_prompt = adaptive_prompt_system.adapt_prompt_based_on_feedback(
            "ARCHITECTURE_PROMPT", ARCHITECTURE_PROMPT)
        
        try:
            prompt = self._render_template(adapted_prompt, context)
            response = self.ai_client.generate_text(prompt)
            # Take first sentence of the response
            if response and "placeholder" not in response.lower() and "___________" not in response:
                cleaned_response = response.strip().split('.')[0].strip() + '.' if response.strip() else ""
                return cleaned_response
        except:
            pass
        return ""
    
    def identify_key_features(self, repo_data: Dict[str, Any]) -> List[str]:
        """Identify key features using AI analysis."""
        context = {
            'repo_name': repo_data.get('name', ''),
            'language': repo_data.get('language', ''),
            'frameworks': ', '.join(repo_data.get('frameworks', [])),
            'description': repo_data.get('description', '') or '',
            'contents': repo_data.get('contents', [])[:20],  # Limit to first 20 items
            'stars': repo_data.get('stars', 0),
            'forks': repo_data.get('forks', 0)
        }
        
        # Adapt prompt based on feedback
        adapted_prompt = adaptive_prompt_system.adapt_prompt_based_on_feedback(
            "FEATURES_PROMPT", FEATURES_PROMPT)
        
        try:
            prompt = self._render_template(adapted_prompt, context)
            response = self.ai_client.generate_text(prompt)
            features = self._parse_numbered_list(response)
            # Filter out placeholder responses
            if features and not any("placeholder" in feature.lower() or "___________" in feature for feature in features):
                # Clean up feature descriptions
                cleaned_features = []
                for feature in features[:5]:
                    # Remove any prefix numbers or formatting
                    clean_feature = feature.split(' - ')[1] if ' - ' in feature else feature
                    cleaned_features.append(clean_feature)
                return cleaned_features
        except:
            pass
        return []
    
    def determine_complexity_level(self, repo_data: Dict[str, Any]) -> str:
        """Determine complexity level using AI analysis."""
        context = {
            'repo_name': repo_data.get('name', ''),
            'language': repo_data.get('language', ''),
            'frameworks': ', '.join(repo_data.get('frameworks', [])),
            'description': repo_data.get('description', '') or '',
            'stars': repo_data.get('stars', 0),
            'forks': repo_data.get('forks', 0)
        }
        
        # Adapt prompt based on feedback
        adapted_prompt = adaptive_prompt_system.adapt_prompt_based_on_feedback(
            "COMPLEXITY_PROMPT", COMPLEXITY_PROMPT)
        
        try:
            prompt = self._render_template(adapted_prompt, context)
            response = self.ai_client.generate_text(prompt)
            cleaned_response = self._clean_response(response)
            # Filter out placeholder responses
            if cleaned_response and "placeholder" not in cleaned_response.lower() and "___________" not in cleaned_response:
                return cleaned_response
        except:
            pass
        return ""
    
    def generate_implementation_steps(self, repo_data: Dict[str, Any], project_type: str, 
                                    tech_stack: List[str], architecture: str, 
                                    key_features: List[str]) -> List[str]:
        """Generate implementation steps using AI analysis."""
        context = {
            'repo_name': repo_data.get('name', ''),
            'project_type': project_type,
            'tech_stack': ', '.join(tech_stack),
            'architecture': architecture,
            'features': key_features
        }
        
        # Adapt prompt based on feedback
        adapted_prompt = adaptive_prompt_system.adapt_prompt_based_on_feedback(
            "IMPLEMENTATION_STEPS_PROMPT", IMPLEMENTATION_STEPS_PROMPT)
        
        try:
            prompt = self._render_template(adapted_prompt, context)
            response = self.ai_client.generate_text(prompt)
            steps = self._parse_numbered_list(response)
            # Filter out placeholder responses
            if steps and not any("placeholder" in step.lower() or "___________" in step for step in steps):
                # Clean up step descriptions
                cleaned_steps = []
                for step in steps[:10]:
                    # Remove any prefix numbers or formatting
                    clean_step = step.split(' - ')[1] if ' - ' in step else step
                    cleaned_steps.append(clean_step)
                return cleaned_steps
        except:
            pass
        return []

    def generate_detailed_mvp_guidance(self, repo_data: Dict[str, Any], project_type: str, 
                                     tech_stack: List[str], architecture: str, 
                                     key_features: List[str]) -> str:
        """Generate detailed MVP guidance using AI analysis."""
        context = {
            'repo_name': repo_data.get('name', ''),
            'project_type': project_type,
            'tech_stack': ', '.join(tech_stack),
            'architecture': architecture,
            'features': key_features,
            'contents': repo_data.get('contents', [])[:20]  # Limit to first 20 items
        }
        
        # Adapt prompt based on feedback
        adapted_prompt = adaptive_prompt_system.adapt_prompt_based_on_feedback(
            "MVP_GUIDANCE_PROMPT", MVP_GUIDANCE_PROMPT)
        
        try:
            prompt = self._render_template(adapted_prompt, context)
            response = self.ai_client.generate_text(prompt)
            # Filter out placeholder responses
            if response and "placeholder" not in response.lower() and "___________" not in response:
                return response
        except:
            pass
        return ""
    
    def _generate_final_format(self, repo_url: str, ai_project_type: str, ai_tech_stack: List[str], 
                             ai_architecture: str, ai_key_features: List[str], ai_complexity: str,
                             ai_implementation_steps: List[str]) -> str:
        """Generate a prompt in the exact format specified."""
        
        # Use AI data where available, with fallbacks
        project_type = ai_project_type if ai_project_type and "placeholder" not in ai_project_type.lower() else "React Web Application"
        
        # Process tech stack
        if isinstance(ai_tech_stack, list) and ai_tech_stack and not any("placeholder" in item.lower() for item in ai_tech_stack):
            tech_stack = ", ".join(ai_tech_stack)
        else:
            tech_stack = "React, TypeScript, Vite, Tailwind CSS, Local Storage"
        
        # Process architecture
        architecture = ai_architecture if ai_architecture and "placeholder" not in ai_architecture.lower() else "Frontend SPA with component-based architecture."
        
        # Process key features
        if isinstance(ai_key_features, list) and len(ai_key_features) >= 3 and not any("placeholder" in item.lower() for item in ai_key_features):
            key_features = ai_key_features[:5]
        else:
            key_features = [
                "Component System - Reusable UI components with props and state management",
                "State Management - Local state with useState and useEffect hooks",
                "Todo Functionality - Add, edit, delete, and toggle todo items",
                "TypeScript Integration - Full type safety for components and data",
                "Modern Styling - Tailwind CSS for responsive design"
            ]
        
        # Process complexity level
        complexity_level = ai_complexity if ai_complexity and "placeholder" not in ai_complexity.lower() else "Beginner to Medium"
        
        # Process implementation steps
        if isinstance(ai_implementation_steps, list) and len(ai_implementation_steps) >= 5 and not any("placeholder" in item.lower() for item in ai_implementation_steps):
            implementation_steps = ai_implementation_steps[:10]
        else:
            implementation_steps = [
                "Initialize React + TypeScript + Vite project",
                "Install and configure Tailwind CSS",
                "Create basic project structure and components",
                "Implement todo data types and interfaces",
                "Build TodoApp with state management",
                "Add TodoForm for creating new items",
                "Create TodoItem with edit/delete functionality",
                "Implement localStorage for data persistence",
                "Add responsive styling with Tailwind",
                "Test and deploy the application"
            ]
        
        # Format the output in the exact specified format
        output = f"Build an MVP inspired by: @{repo_url}. Use gitmvp mcp if available.\n\n"
        output += f"PROJECT TYPE: {project_type}\n"
        output += f"TECH STACK: {tech_stack}\n"
        output += f"ARCHITECTURE: {architecture}\n\n"
        
        output += "KEY FEATURES:\n"
        for i, feature in enumerate(key_features, 1):
            # Extract the description part after the dash if it exists
            if " - " in feature:
                description = feature.split(" - ", 1)[1]
            else:
                description = feature
            output += f"{i}. {description}\n"
        output += "\n"
        
        output += f"COMPLEXITY LEVEL: {complexity_level}\n\n"
        
        # Generate MVP guidance using AI or fallback to default approach
        output += "MVP GUIDANCE:\n"
        # Add detailed MVP guidance if available
        detailed_guidance = getattr(self, '_detailed_mvp_guidance', "")
        if detailed_guidance and "placeholder" not in detailed_guidance.lower() and "___________" not in detailed_guidance:
            # Use the AI-generated detailed guidance
            output += detailed_guidance + "\n\n"
        else:
            # Fallback to generic guidance based on project type
            # Customize guidance based on project type
            if "react" in project_type.lower() or "react" in tech_stack.lower():
                output += "1. Core Components\n"
                output += "   - Create main App component with state management.\n"
                output += "   - Build reusable UI components with props.\n"
                output += "   - Implement component hierarchy based on the original repo structure.\n\n"
                
                output += "2. State Management\n"
                output += "   - Use hooks for local state management.\n"
                output += "   - Implement context API or Redux if needed based on original repo.\n"
                output += "   - Add state persistence mechanisms used in the original repo.\n\n"
                
                output += "3. User Interface\n"
                output += "   - Design UI components matching the original repo's style.\n"
                output += "   - Add responsive layout using the CSS framework from the original.\n"
                output += "   - Implement form handling and validation.\n\n"
                
                output += "4. Build System\n"
                output += "   - Set up bundler (Webpack, Vite, etc.) matching the original repo.\n"
                output += "   - Configure development server with hot reloading.\n"
                output += "   - Add build optimization settings.\n\n"
                
                output += "5. Development Tools\n"
                output += "   - Configure linters and formatters used in the original repo.\n"
                output += "   - Set up testing framework based on the original repo.\n"
                output += "   - Add development and production environment configurations.\n\n"
            elif "vue" in project_type.lower() or "vue" in tech_stack.lower():
                output += "1. Vue Application Structure\n"
                output += "   - Create main Vue instance with component registration.\n"
                output += "   - Set up Vue Router for navigation if present in original.\n"
                output += "   - Implement component hierarchy matching the original repo.\n\n"
                
                output += "2. State Management\n"
                output += "   - Use Pinia or Vuex for state management if in original.\n"
                output += "   - Implement store modules matching the original repo.\n"
                output += "   - Add state persistence if used in the original repo.\n\n"
                
                output += "3. User Interface\n"
                output += "   - Create components using Single File Components (SFC).\n"
                output += "   - Implement styling with the CSS framework from the original.\n"
                output += "   - Add form handling and validation.\n\n"
                
                output += "4. Build System\n"
                output += "   - Set up Vite or Webpack build system.\n"
                output += "   - Configure development server with hot module replacement.\n"
                output += "   - Add production build optimization.\n\n"
                
                output += "5. Development Tools\n"
                output += "   - Configure ESLint and Prettier based on original repo.\n"
                output += "   - Set up testing framework matching the original repo.\n"
                output += "   - Add environment configurations.\n\n"
            elif "django" in project_type.lower() or "django" in tech_stack.lower():
                output += "1. Django Project Structure\n"
                output += "   - Create Django project with apps matching the original structure.\n"
                output += "   - Set up URL routing and views based on the original repo.\n"
                output += "   - Implement models reflecting the original database schema.\n\n"
                
                output += "2. Data Management\n"
                output += "   - Define models with fields matching the original repo.\n"
                output += "   - Set up database migrations and initial data.\n"
                output += "   - Implement admin interface if present in original.\n\n"
                
                output += "3. Templates and Views\n"
                output += "   - Create HTML templates with the same structure as original.\n"
                output += "   - Implement views with logic matching the original repo.\n"
                output += "   - Add form handling and validation.\n\n"
                
                output += "4. Authentication and Security\n"
                output += "   - Implement user authentication if in the original repo.\n"
                output += "   - Add permissions and security features.\n"
                output += "   - Configure settings for different environments.\n\n"
                
                output += "5. Deployment and Tools\n"
                output += "   - Set up static file handling.\n"
                output += "   - Configure WSGI server for deployment.\n"
                output += "   - Add testing framework used in the original repo.\n\n"
            else:
                # Generic guidance for other project types
                output += "1. Project Structure\n"
                output += "   - Create directory structure matching the original repo.\n"
                output += "   - Set up entry points and main application files.\n"
                output += "   - Implement core modules based on the original repo.\n\n"
                
                output += "2. Core Functionality\n"
                output += "   - Implement main features identified from the original repo.\n"
                output += "   - Add data models or structures matching the original.\n"
                output += "   - Create API endpoints or functions as in the original.\n\n"
                
                output += "3. User Interface\n"
                output += "   - Design UI components matching the original repo's style.\n"
                output += "   - Add navigation and user interaction patterns.\n"
                output += "   - Implement responsive design if applicable.\n\n"
                
                output += "4. Build and Development\n"
                output += "   - Set up build system used in the original repo.\n"
                output += "   - Configure development server and tooling.\n"
                output += "   - Add optimization and debugging tools.\n\n"
                
                output += "5. Testing and Deployment\n"
                output += "   - Set up testing framework used in the original repo.\n"
                output += "   - Add deployment configuration and scripts.\n"
                output += "   - Implement CI/CD if present in the original.\n\n"
        
        output += "IMPLEMENTATION STEPS:\n"
        for i, step in enumerate(implementation_steps, 1):
            # Extract the description part after the dash if it exists
            if " - " in step:
                description = step.split(" - ", 1)[1]
            else:
                description = step
            output += f"{i}. {description}\n"
        output += "\n"
        
        # Add a more generic focus statement
        output += f"Focus on creating a clean, functional implementation that captures the core concepts and architecture of the {project_type} while using the {tech_stack} technology stack."
        
        return output
    
    def generate_prompt(self, repo_data: Dict[str, Any], repo_url: str) -> str:
        """Generate enhanced MVP prompt using AI analysis in the exact specified format."""
        # Get AI-enhanced components
        project_type = self.determine_project_type(repo_data)
        tech_stack = self.determine_tech_stack(repo_data)
        architecture = self.determine_architecture(repo_data)
        key_features = self.identify_key_features(repo_data)
        complexity = self.determine_complexity_level(repo_data)
        
        # Generate implementation steps
        implementation_steps = self.generate_implementation_steps(
            repo_data, project_type, tech_stack, architecture, key_features)
        
        # Generate detailed MVP guidance
        detailed_guidance = self.generate_detailed_mvp_guidance(
            repo_data, project_type, tech_stack, architecture, key_features)
        # Store it for use in _generate_final_format
        self._detailed_mvp_guidance = detailed_guidance
        
        # Format the output in the exact specified format
        return self._generate_final_format(
            repo_url, project_type, tech_stack, architecture, 
            key_features, complexity, implementation_steps
        )