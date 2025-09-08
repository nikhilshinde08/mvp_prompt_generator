#!/usr/bin/env bash

# Run all tests for the GitHub MVP Generator

echo "Running GitHub MVP Generator tests..."
echo "====================================="

# Activate virtual environment
source venv/bin/activate

# Run unit tests
python -m unittest tests/test_generator.py

echo ""
echo "Test execution completed."