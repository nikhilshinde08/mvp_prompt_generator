#!/bin/bash

# Script to start both the backend API and frontend development server

echo "Starting GitHub MVP Generator (Backend + Frontend)"
echo "================================================="

# Start backend API in background
echo "Starting backend API server..."
cd github_mvp_generator
source venv/bin/activate
python api.py > ../backend.log 2>&1 &
BACKEND_PID=$!
cd ..

# Wait a moment for backend to start
sleep 3

# Start frontend development server
echo "Starting frontend development server..."
npm run dev > frontend.log 2>&1 &
FRONTEND_PID=$!

echo ""
echo "Services started:"
echo "  Backend API: http://localhost:8000"
echo "  Frontend: http://localhost:3000"
echo ""
echo "Backend logs: backend.log"
echo "Frontend logs: frontend.log"
echo ""
echo "Press Ctrl+C to stop both services"

# Cleanup function
cleanup() {
    echo ""
    echo "Stopping services..."
    kill $BACKEND_PID $FRONTEND_PID 2>/dev/null
    wait $BACKEND_PID $FRONTEND_PID 2>/dev/null
    echo "Services stopped."
    exit 0
}

# Trap Ctrl+C
trap cleanup INT

# Wait for processes
wait $BACKEND_PID $FRONTEND_PID