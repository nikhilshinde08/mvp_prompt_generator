#!/bin/bash
# Build script for the backend API

echo "Building GitHub MVP Generator Backend..."

# Activate virtual environment
source venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt

echo "Backend build completed."