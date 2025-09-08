#!/usr/bin/env bash

# Setup script for GitHub MVP Generator

echo "Setting up GitHub MVP Generator..."
echo "================================="

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "Creating .env file..."
    cp .env.example .env
    echo "Please add your GitHub personal access token and Groq API key to .env file"
fi

echo ""
echo "Setup completed successfully!"
echo ""
echo "To use the tool:"
echo "1. Activate the virtual environment: source venv/bin/activate"
echo "2. Add your API keys to the .env file:"
echo "   - For Groq: GROQ_API_KEY=your_key_here"
echo "3. Run the tool: python main.py <github_repo_url>"
echo ""
echo "Example usage:"
echo "python main.py https://github.com/facebook/react"
echo ""
echo "To run tests:"
echo "python -m unittest tests/test_generator.py"