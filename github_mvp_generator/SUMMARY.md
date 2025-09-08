# GitHub MVP Generator - Project Summary

This project implements a Python tool that transforms any GitHub repository into an MVP (Minimum Viable Product) prompt for bootstrapping new projects based on proven open-source implementations.

## Project Structure

```
github-mvp-generator/
├── main.py                 # Main CLI interface
├── config.py               # Configuration settings
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── .env.example           # Example environment file
├── .gitignore             # Git ignore patterns
├── setup.sh               # Setup script
├── run.sh                 # Run script
├── run_tests.sh           # Test script
├── demo.py                # Demo script
├── github_parser/         # GitHub repository analysis
│   └── analyzer.py        # Repository analyzer
├── prompt_generator/      # MVP prompt generation
│   └── generator.py       # Prompt generator
├── examples/              # Example scripts
│   └── generate_example.py # Example output generator
├── tests/                 # Unit tests
│   └── test_generator.py  # Test cases
└── docs/                  # Documentation
    ├── installation.md    # Installation guide
    ├── usage.md           # Usage instructions
    └── examples.md        # Usage examples
```

## Key Features Implemented

1. **GitHub Repository Analysis**:
   - Parses GitHub URLs to extract owner and repository name
   - Uses GitHub API to retrieve repository information
   - Analyzes repository contents to detect technologies and frameworks
   - Identifies primary programming language

2. **MVP Prompt Generation**:
   - Determines project type based on detected technologies
   - Identifies technology stack from repository files
   - Generates architecture description
   - Lists key features based on repository analysis
   - Assesses complexity level based on repository popularity
   - Provides implementation guidance and steps

3. **Command-Line Interface**:
   - Simple CLI for analyzing repositories
   - Support for GitHub personal access tokens
   - Clear output formatting

4. **Example Output Generation**:
   - Script to generate the exact output format specified in requirements
   - Demonstrates the tool's capabilities

## Technologies Used

- **Python**: Core programming language
- **Requests**: HTTP library for GitHub API calls
- **PyGithub**: Python wrapper for GitHub API
- **python-dotenv**: Environment variable management
- **Jinja2**: Templating engine (for future expansion)

## How It Works

1. **Repository Analysis**:
   - The `GitHubRepoAnalyzer` class parses the GitHub URL and uses the GitHub API to retrieve repository information
   - It analyzes the repository contents to detect frameworks, languages, and technologies

2. **Prompt Generation**:
   - The `PromptGenerator` class uses the analyzed data to generate a structured MVP prompt
   - It determines project type, tech stack, architecture, and other components based on the analysis

3. **Output Formatting**:
   - The tool formats the output in a clear, structured way that can be used as a prompt for AI systems or as a blueprint for implementation

## Example Usage

```bash
# Analyze a GitHub repository
python main.py https://github.com/facebook/react

# With GitHub token for higher rate limits
python main.py https://github.com/facebook/react --token YOUR_TOKEN
```

## Testing

The project includes unit tests for core functionality:
```bash
python -m unittest tests/test_generator.py
```

## Future Improvements

1. **Enhanced Technology Detection**:
   - More sophisticated analysis of repository files
   - Better detection of databases, CSS frameworks, build tools, etc.

2. **Template System**:
   - Use Jinja2 templates for more flexible output formatting
   - Support for different output formats (JSON, YAML, etc.)

3. **Caching**:
   - Cache GitHub API responses to reduce API usage
   - Store analyzed repositories for faster subsequent analysis

4. **Web Interface**:
   - Create a web-based interface for easier use
   - Allow users to save and share generated prompts

5. **Batch Processing**:
   - Analyze multiple repositories at once
   - Compare different repositories

This tool successfully fulfills the requirements of turning GitHub repositories into structured MVP prompts that can be used to bootstrap new projects based on proven open-source implementations.