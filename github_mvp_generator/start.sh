#!/bin/bash
# Start script for the backend API

echo "Starting GitHub MVP Generator Backend API..."
echo "API will be available at: http://0.0.0.0:$PORT"
echo "Press Ctrl+C to stop the server"
echo ""

# Start the API server
python api.py