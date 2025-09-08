class PromptGenerator:
    """Generates MVP prompts based on GitHub repository analysis."""
    
    def __init__(self):
        pass
    
    def determine_project_type(self, repo_data):
        """Determine the project type based on repository analysis."""
        language = repo_data.get('language', '') or ''
        language = language.lower()
        frameworks = [f.lower() for f in repo_data.get('frameworks', [])]
        description = repo_data.get('description', '') or ''
        description = description.lower()
        
        # Determine project type based on language, frameworks and description
        if 'react' in frameworks or 'next.js' in frameworks:
            if ('component' in description and 'library' in description) or 'component library' in description:
                return 'React Component Library'
            else:
                return 'React Web Application'
        elif 'vue' in frameworks:
            return 'Vue.js Web Application'
        elif 'angular' in frameworks:
            return 'Angular Web Application'
        elif 'django' in frameworks:
            return 'Django Web Application'
        elif 'flask' in frameworks:
            return 'Flask Web Application'
        elif 'fastapi' in frameworks:
            return 'FastAPI Web Application'
        elif 'express' in frameworks:
            return 'Express.js Web Application'
        elif language == 'python':
            return 'Python Application'
        elif language == 'javascript':
            # Special case for React in frameworks
            if 'react' in frameworks:
                return 'React Web Application'
            return 'JavaScript Application'
        else:
            return f'{language.capitalize()} Application' if language else 'Application'
    
    def determine_tech_stack(self, repo_data):
        """Determine the technology stack."""
        tech_stack = []
        
        language = repo_data.get('language')
        if language:
            tech_stack.append(language)
            
        frameworks = [f.lower() for f in repo_data.get('frameworks', [])]
        tech_stack.extend(repo_data.get('frameworks', []))  # Add original case frameworks
        
        # Check for common technologies in file names
        contents = repo_data.get('contents', [])
        file_names = [item.get('name', '').lower() for item in contents]
        
        # Database detection
        if any('mongo' in name or 'mongodb' in name for name in file_names):
            tech_stack.append('MongoDB')
        if any('sql' in name for name in file_names):
            tech_stack.append('SQL')
        if any('postgres' in name for name in file_names):
            tech_stack.append('PostgreSQL')
            
        # CSS frameworks
        if any('tailwind' in name for name in file_names):
            tech_stack.append('Tailwind CSS')
        if any('bootstrap' in name for name in file_names):
            tech_stack.append('Bootstrap')
            
        # Build tools
        if any('webpack' in name for name in file_names):
            tech_stack.append('Webpack')
        if any('vite' in name for name in file_names):
            tech_stack.append('Vite')
            
        # Testing frameworks
        if any('jest' in name for name in file_names):
            tech_stack.append('Jest')
        if any('pytest' in name for name in file_names):
            tech_stack.append('Pytest')
            
        return tech_stack
    
    def determine_architecture(self, repo_data):
        """Determine the architecture pattern."""
        frameworks = [f.lower() for f in repo_data.get('frameworks', [])]
        language = repo_data.get('language', '') or ''
        language = language.lower()
        
        if 'react' in frameworks or 'vue' in frameworks or 'angular' in frameworks:
            return 'Frontend SPA with component-based architecture'
        elif 'django' in frameworks:
            return 'Backend MVC with frontend templates'
        elif 'flask' in frameworks or 'fastapi' in frameworks:
            return 'Backend API with frontend separation'
        elif 'express' in frameworks:
            return 'Node.js API server'
        elif language == 'python':
            return 'Python application architecture'
        else:
            return 'Standard application architecture'
    
    def identify_key_features(self, repo_data):
        """Identify key features from the repository."""
        features = []
        description = repo_data.get('description', '') or ''
        description = description.lower()
        contents = repo_data.get('contents', [])
        file_names = [item.get('name', '').lower() for item in contents]
        frameworks = [f.lower() for f in repo_data.get('frameworks', [])]
        
        # Feature detection based on description and file names
        if 'component' in description or any('component' in name for name in file_names):
            features.append('Component System - Reusable UI components')
            
        if any('state' in name or 'store' in name for name in file_names):
            features.append('State Management - Centralized state handling')
            
        if any('test' in name for name in file_names):
            features.append('Testing - Unit and integration tests')
            
        if 'react' in frameworks:
            features.append('React Hooks - Functional components with hooks')
            
        if 'vue' in frameworks:
            features.append('Vue Composition API - Modern Vue development')
            
        if 'tailwind' in file_names or 'tailwind' in description:
            features.append('Modern Styling - Utility-first CSS framework')
            
        if any('api' in name or 'service' in name for name in file_names):
            features.append('API Integration - RESTful API consumption')
            
        if any('auth' in name or 'login' in name for name in file_names):
            features.append('Authentication - User login and session management')
            
        # Add general features based on repository size and stars
        stars = repo_data.get('stars', 0)
        if stars > 10000:
            features.append('Scalable Architecture - Designed for high usage')
        elif stars > 1000:
            features.append('Well-structured Code - Organized project layout')
        elif stars > 100:
            features.append('Well-structured Code - Organized project layout')
            
        # If no specific features detected, add generic ones
        if not features:
            features = [
                'Modular Design - Well-organized code structure',
                'Documentation - Clear usage instructions',
                'Error Handling - Proper exception management'
            ]
            
        return features[:5]  # Limit to 5 features
    
    def determine_complexity_level(self, repo_data):
        """Determine the complexity level."""
        stars = repo_data.get('stars', 0)
        forks = repo_data.get('forks', 0)
        language = repo_data.get('language', '').lower()
        
        # Simple heuristic for complexity based on popularity and language
        score = stars + forks
        
        if score > 10000:
            return 'Advanced'
        elif score > 1000:
            return 'Intermediate to Advanced'
        elif score > 100:
            return 'Beginner to Intermediate'
        else:
            return 'Beginner'
    
    def generate_mvp_guidance(self, repo_data):
        """Generate MVP implementation guidance."""
        frameworks = [f.lower() for f in repo_data.get('frameworks', [])]
        language = repo_data.get('language', '') or ''
        language = language.lower()
        
        guidance = []
        
        if 'react' in frameworks:
            guidance = [
                'Core Components - Create main App component with state management',
                'Component Hierarchy - Build reusable UI components with props',
                'State Management - Use hooks for local state management',
                'Event Handling - Implement user interactions and form handling',
                'Styling - Add CSS modules or styled components for styling'
            ]
        elif 'vue' in frameworks:
            guidance = [
                'Vue Instance - Set up main Vue application instance',
                'Component System - Create single file components (SFC)',
                'Vue Router - Implement navigation and routing',
                'State Management - Use Pinia or Vuex for state',
                'Directives - Utilize built-in Vue directives'
            ]
        elif 'django' in frameworks:
            guidance = [
                'Project Structure - Create Django project and apps',
                'Models - Define data models and relationships',
                'Views - Implement views for handling requests',
                'Templates - Create HTML templates for rendering',
                'URLs - Set up URL routing and mapping'
            ]
        elif 'flask' in frameworks:
            guidance = [
                'Application Setup - Initialize Flask application',
                'Routing - Define URL routes and handlers',
                'Templates - Use Jinja2 for HTML templating',
                'Database - Integrate SQLAlchemy for data models',
                'Extensions - Add Flask extensions for functionality'
            ]
        elif language == 'python':
            guidance = [
                'Project Structure - Organize code into modules and packages',
                'Dependencies - Manage requirements with pip',
                'Documentation - Write docstrings and README files',
                'Testing - Implement unit tests with unittest or pytest',
                'Packaging - Prepare for distribution with setup.py'
            ]
        else:
            guidance = [
                'Project Setup - Initialize project with standard structure',
                'Dependencies - Manage project dependencies',
                'Modular Design - Organize code into logical modules',
                'Documentation - Create README and usage instructions',
                'Testing - Implement basic testing strategy'
            ]
            
        return guidance
    
    def generate_implementation_steps(self, repo_data):
        """Generate step-by-step implementation guide."""
        frameworks = [f.lower() for f in repo_data.get('frameworks', [])]
        language = repo_data.get('language', '') or ''
        language = language.lower()
        
        steps = []
        
        if 'react' in frameworks:
            steps = [
                'Initialize React project with Create React App or Vite',
                'Install required dependencies and libraries',
                'Set up project structure with components directory',
                'Create main App component with basic layout',
                'Implement routing with React Router',
                'Build reusable UI components',
                'Add state management with hooks',
                'Implement form handling and validation',
                'Add styling with CSS or styling library',
                'Test and optimize the application'
            ]
        elif 'vue' in frameworks:
            steps = [
                'Initialize Vue project with Vue CLI or Vite',
                'Install required dependencies',
                'Set up project structure',
                'Create main App component',
                'Implement Vue Router for navigation',
                'Build component hierarchy',
                'Add state management',
                'Implement forms and user interactions',
                'Add styling and responsive design',
                'Test and build for production'
            ]
        elif 'django' in frameworks:
            steps = [
                'Initialize Django project with django-admin',
                'Create Django apps for different features',
                'Define data models in models.py',
                'Set up database and run migrations',
                'Implement views for handling requests',
                'Create templates for HTML rendering',
                'Configure URLs and routing',
                'Add static files and media handling',
                'Implement user authentication',
                'Test and deploy the application'
            ]
        elif language == 'python':
            steps = [
                'Set up Python virtual environment',
                'Initialize project directory structure',
                'Create main application file',
                'Implement core functionality',
                'Add required dependencies to requirements.txt',
                'Write unit tests for core features',
                'Create documentation and usage instructions',
                'Set up CI/CD configuration',
                'Package application for distribution',
                'Test installation and usage'
            ]
        else:
            steps = [
                'Initialize project with standard structure',
                'Set up development environment',
                'Create main application files',
                'Implement core functionality',
                'Add documentation and examples',
                'Write tests for key features',
                'Configure build and deployment',
                'Optimize for performance',
                'Test across different environments',
                'Prepare release package'
            ]
            
        return steps
    
    def generate_prompt(self, repo_data, repo_url):
        """Generate the complete MVP prompt."""
        project_type = self.determine_project_type(repo_data)
        tech_stack = self.determine_tech_stack(repo_data)
        architecture = self.determine_architecture(repo_data)
        key_features = self.identify_key_features(repo_data)
        complexity = self.determine_complexity_level(repo_data)
        guidance = self.generate_mvp_guidance(repo_data)
        steps = self.generate_implementation_steps(repo_data)
        
        # Format the output
        prompt = f"Build an MVP inspired by: @{repo_url}\n\n"
        prompt += f"PROJECT TYPE: {project_type}\n"
        prompt += f"TECH STACK: {', '.join(tech_stack) if tech_stack else 'Not detected'}\n"
        prompt += f"ARCHITECTURE: {architecture}\n\n"
        
        prompt += "KEY FEATURES:\n"
        for i, feature in enumerate(key_features, 1):
            prompt += f"{i}. {feature}\n"
        prompt += "\n"
        
        prompt += f"COMPLEXITY LEVEL: {complexity}\n\n"
        
        prompt += "MVP GUIDANCE:\n"
        for i, guide in enumerate(guidance, 1):
            prompt += f"{i}. {guide}\n"
        prompt += "\n"
        
        prompt += "IMPLEMENTATION STEPS:\n"
        for i, step in enumerate(steps, 1):
            prompt += f"{i}. {step}\n"
        prompt += "\n"
        
        prompt += "Focus on creating a clean, functional implementation that demonstrates the core concepts of the original project."
        
        return prompt