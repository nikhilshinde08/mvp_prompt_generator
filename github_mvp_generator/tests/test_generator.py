import unittest
from github_parser.analyzer import GitHubRepoAnalyzer
from prompt_generator.generator import PromptGenerator

class TestGitHubRepoAnalyzer(unittest.TestCase):
    
    def setUp(self):
        self.analyzer = GitHubRepoAnalyzer()
    
    def test_parse_repo_url(self):
        # Test standard URL format
        owner, repo = self.analyzer.parse_repo_url('https://github.com/facebook/react')
        self.assertEqual(owner, 'facebook')
        self.assertEqual(repo, 'react')
        
        # Test URL with trailing slash
        owner, repo = self.analyzer.parse_repo_url('https://github.com/facebook/react/')
        self.assertEqual(owner, 'facebook')
        self.assertEqual(repo, 'react')
        
        # Test invalid URL
        with self.assertRaises(ValueError):
            self.analyzer.parse_repo_url('https://gitlab.com/facebook/react')

class TestPromptGenerator(unittest.TestCase):
    
    def setUp(self):
        self.generator = PromptGenerator()
        self.sample_repo_data = {
            'owner': 'facebook',
            'repo': 'react',
            'name': 'react',
            'description': 'A declarative, efficient, and flexible JavaScript library for building user interfaces.',
            'language': 'JavaScript',
            'frameworks': ['React'],
            'stars': 200000,
            'forks': 40000,
            'contents': [
                {'name': 'package.json'},
                {'name': 'README.md'},
                {'name': 'src'},
                {'name': 'examples'}
            ]
        }
    
    def test_determine_project_type(self):
        project_type = self.generator.determine_project_type(self.sample_repo_data)
        self.assertEqual(project_type, 'React Web Application')
    
    def test_determine_tech_stack(self):
        tech_stack = self.generator.determine_tech_stack(self.sample_repo_data)
        self.assertIn('JavaScript', tech_stack)
        self.assertIn('React', tech_stack)
    
    def test_generate_prompt(self):
        prompt = self.generator.generate_prompt(self.sample_repo_data, 'https://github.com/facebook/react')
        self.assertIn('Build an MVP inspired by: @https://github.com/facebook/react', prompt)
        self.assertIn('PROJECT TYPE:', prompt)
        self.assertIn('TECH STACK:', prompt)

if __name__ == '__main__':
    unittest.main()