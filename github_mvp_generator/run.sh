#!/usr/bin/env bash

# Run the GitHub MVP Generator

echo "GitHub MVP Generator"
echo "===================="

# Activate virtual environment
source venv/bin/activate

# Run the main script
python main.py "$@"