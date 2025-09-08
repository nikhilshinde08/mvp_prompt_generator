from knowledge_base import knowledge_base


class GitHubRepoAnalyzer:
    """Analyzes GitHub repositories to extract key information for MVP generation."""
    
    def __init__(self, github_token=None):
        self.github_token = github_token
        self.headers = {
            'Accept': 'application/vnd.github.v3+json',
            'User-Agent': 'GitHub-MVP-Generator'
        }
        if self.github_token:
            self.headers['Authorization'] = f'token {self.github_token}'
    
    def parse_repo_url(self, url):
        """Extract owner and repo name from GitHub URL."""
        # Handle different GitHub URL formats
        if 'github.com' not in url:
            raise ValueError('Invalid GitHub URL')
            
        # Remove trailing slash if present
        url = url.rstrip('/')
        
        # Extract owner and repo from URL
        parts = url.split('/')
        if len(parts) < 2:
            raise ValueError('Invalid GitHub URL format')
            
        owner = parts[-2]
        repo = parts[-1]
        
        return owner, repo
    
    def get_repo_info(self, owner, repo):
        """Get basic repository information."""
        import requests
        from config import GITHUB_API_URL
        
        url = f'{GITHUB_API_URL}/repos/{owner}/{repo}'
        response = requests.get(url, headers=self.headers)
        
        # If we get a 401, try without authentication
        if response.status_code == 401:
            response = requests.get(url)
        
        if response.status_code != 200:
            raise Exception(f'GitHub API error: {response.status_code} - {response.text}')
            
        return response.json()
    
    def get_repo_contents(self, owner, repo, path=''):
        """Get repository contents."""
        import requests
        from config import GITHUB_API_URL
        
        url = f'{GITHUB_API_URL}/repos/{owner}/{repo}/contents/{path}'
        response = requests.get(url, headers=self.headers)
        
        # If we get a 401, try without authentication
        if response.status_code == 401:
            response = requests.get(url)
        
        if response.status_code != 200:
            raise Exception(f'GitHub API error: {response.status_code} - {response.text}')
            
        return response.json()
    
    def get_primary_language(self, owner, repo):
        """Get the primary language of the repository."""
        import requests
        from config import GITHUB_API_URL
        
        url = f'{GITHUB_API_URL}/repos/{owner}/{repo}/languages'
        response = requests.get(url, headers=self.headers)
        
        # If we get a 401, try without authentication
        if response.status_code == 401:
            response = requests.get(url)
        
        if response.status_code != 200:
            raise Exception(f'GitHub API error: {response.status_code} - {response.text}')
            
        languages = response.json()
        if not languages:
            return None
            
        # Return the language with the most bytes
        return max(languages, key=languages.get)
    
    def detect_framework(self, contents):
        """Detect framework based on repository files."""
        # This is a simplified detection method
        # In a real implementation, this would be more sophisticated
        
        # Look for common framework indicators
        framework_indicators = {
            'React': ['package.json', 'react', 'jsx'],
            'Vue': ['package.json', 'vue'],
            'Angular': ['package.json', 'angular'],
            'Next.js': ['next.config.js', 'next'],
            'Django': ['manage.py', 'django'],
            'Flask': ['app.py', 'flask'],
            'FastAPI': ['main.py', 'fastapi'],
            'Express': ['package.json', 'express'],
            'Spring': ['pom.xml', 'spring'],
        }
        
        detected_frameworks = []
        
        # Check file names and content
        for item in contents:
            name = item.get('name', '').lower()
            for framework, indicators in framework_indicators.items():
                if any(indicator in name for indicator in indicators):
                    if framework not in detected_frameworks:
                        detected_frameworks.append(framework)
        
        return detected_frameworks
    
    def analyze_repo(self, repo_url):
        """Main method to analyze a GitHub repository."""
        owner, repo = self.parse_repo_url(repo_url)
        
        # Check if we have a pattern stored for this repository
        repo_pattern = knowledge_base.get_repo_pattern(repo_url)
        if repo_pattern:
            print("Using cached analysis for this repository")
            return repo_pattern.get("pattern_data", {})
        
        # Get repository information
        repo_info = self.get_repo_info(owner, repo)
        
        # Get repository contents (top level)
        contents = self.get_repo_contents(owner, repo)
        
        # Get primary language
        primary_language = self.get_primary_language(owner, repo)
        
        # Detect frameworks
        frameworks = self.detect_framework(contents)
        
        # Create analysis result
        analysis_result = {
            'owner': owner,
            'repo': repo,
            'name': repo_info.get('name'),
            'description': repo_info.get('description'),
            'language': primary_language,
            'frameworks': frameworks,
            'stars': repo_info.get('stargazers_count', 0),
            'forks': repo_info.get('forks_count', 0),
            'contents': contents
        }
        
        # Store the pattern for future use
        knowledge_base.store_repo_pattern(repo_url, analysis_result)
        
        return analysis_result