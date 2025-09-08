# GitHub MVP Generator

This project requires Python 3.7+

## Dependencies
- requests: For making HTTP requests to GitHub API
- pygithub: Python wrapper for GitHub API
- python-dotenv: For loading environment variables
- jinja2: For templating the output

Install dependencies with:
```bash
pip install -r requirements.txt
```

## GitHub API Rate Limits

GitHub's API has rate limits:
- Unauthenticated requests: 60 requests per hour
- Authenticated requests: 5000 requests per hour

To authenticate, create a GitHub personal access token:
1. Go to https://github.com/settings/tokens
2. Generate a new token with appropriate permissions
3. Add it to a `.env` file as `GITHUB_TOKEN=your_token_here`