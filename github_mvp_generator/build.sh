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

# Install Python dependencies
pip install -r requirements.txt

echo "Backend build completed successfully."