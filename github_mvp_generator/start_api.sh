#!/bin/bash

# Script to start the GitHub MVP Generator API server

echo "Starting GitHub MVP Generator API server..."
echo "=========================================="
echo "API will be available at: http://localhost:8000"
echo "Press Ctrl+C to stop the server"
echo ""

# Activate virtual environment and start the API server
source venv/bin/activate
python api.py