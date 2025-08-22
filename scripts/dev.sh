#!/bin/bash

# Development script for Recruitment Flow AI
# This script starts both frontend and backend development servers

set -e

echo "🚀 Starting Recruitment Flow AI Development Environment"

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed. Please install Node.js 18 or higher."
    exit 1
fi

# Check if Python is installed
if ! command -v python &> /dev/null; then
    echo "❌ Python is not installed. Please install Python 3.11 or higher."
    exit 1
fi

# Check if npm is installed
if ! command -v npm &> /dev/null; then
    echo "❌ npm is not installed. Please install npm."
    exit 1
fi

echo "✅ Prerequisites check passed"

# Install root dependencies
echo "📦 Installing root dependencies..."
npm install

# Install frontend dependencies
echo "📦 Installing frontend dependencies..."
cd apps/web
npm install
cd ../..

# Install backend dependencies
echo "📦 Installing backend dependencies..."
cd apps/api
pip install -e .
cd ../..

# Install package dependencies
echo "📦 Installing package dependencies..."
for package in packages/*; do
    if [ -d "$package" ] && [ -f "$package/package.json" ]; then
        echo "📦 Installing dependencies for $package..."
        cd "$package"
        npm install
        cd ../..
    fi
done

# Check if .env files exist
if [ ! -f ".env" ]; then
    echo "⚠️  .env file not found. Creating from template..."
    cp env.example .env
    echo "📝 Please update .env with your configuration values"
fi

# Start development servers
echo "🚀 Starting development servers..."

# Start backend in background
echo "🔧 Starting backend server..."
cd apps/api
python -m uvicorn recruitment_flow_api.main:app --reload --host 0.0.0.0 --port 8000 &
BACKEND_PID=$!
cd ../..

# Wait a moment for backend to start
sleep 3

# Start frontend
echo "🎨 Starting frontend server..."
cd apps/web
npm run dev &
FRONTEND_PID=$!
cd ../..

echo "✅ Development environment started!"
echo "📱 Frontend: http://localhost:3000"
echo "🔧 Backend: http://localhost:8000"
echo "📚 API Docs: http://localhost:8000/docs"

# Function to cleanup on exit
cleanup() {
    echo "🛑 Shutting down development servers..."
    kill $FRONTEND_PID 2>/dev/null || true
    kill $BACKEND_PID 2>/dev/null || true
    exit 0
}

# Set up signal handlers
trap cleanup SIGINT SIGTERM

# Wait for processes
wait
