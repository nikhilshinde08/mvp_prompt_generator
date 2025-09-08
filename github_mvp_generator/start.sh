#!/bin/bash
# Start script for the backend API

# Activate virtual environment
source venv/bin/activate

# Set default port if not provided
export PORT=${PORT:-8000}

echo "Starting GitHub MVP Generator Backend API..."
echo "API will be available at: http://0.0.0.0:$PORT"
echo "Press Ctrl+C to stop the server"
echo ""

# Start the API server
python api.py