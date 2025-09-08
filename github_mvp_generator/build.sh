#!/bin/bash
# Build script for the backend API

# Change to the script's directory
cd "$(dirname "$0")"

echo "Building GitHub MVP Generator Backend..."

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install Python dependencies directly
echo "Installing Python dependencies..."
pip install requests==2.31.0 pygithub==2.1.1 python-dotenv==1.0.0 jinja2==3.1.2 openai==1.106.1 groq==0.13.1 flask==2.3.2 flask-cors==4.0.0

echo "Backend build completed successfully."