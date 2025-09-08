# Deploying to Render.com

This guide explains how to deploy the GitHub MVP Generator application to Render.com.

## Prerequisites

1. A Render.com account (free tier available)
2. A Groq API key (get one from [Groq Console](https://console.groq.com/keys))

## Deployment Steps

### 1. Fork the Repository

First, fork this repository to your GitHub account so you can make configuration changes.

### 2. Create Services on Render

1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click "New" and select "Web Service"
3. Connect your GitHub account and select your forked repository

### 3. Deploy the Backend API

1. Create a new Web Service with these settings:
   - **Name**: `github-mvp-generator-api`
   - **Runtime**: Python 3
   - **Build Command**: `./github_mvp_generator/build.sh`
   - **Start Command**: `./github_mvp_generator/start.sh`
   - **Plan**: Free

2. Add environment variables:
   - `GROQ_API_KEY`: Your Groq API key (keep it secret)
   - `AI_PROVIDER`: `groq` (default)

3. Click "Create Web Service"

### 4. Deploy the Frontend

1. Create another Web Service with these settings:
   - **Name**: `github-mvp-generator-frontend`
   - **Runtime**: Node
   - **Build Command**: `npm install && npm run build`
   - **Start Command**: `npm run start`
   - **Plan**: Free

2. Add environment variables:
   - `NEXT_PUBLIC_BACKEND_API_URL`: The URL of your deployed backend service (will be available after backend deployment)
   - Example: `https://github-mvp-generator-api-xyz1.onrender.com`

3. Click "Create Web Service"

### 5. Update Frontend Configuration (if needed)

If you need to update the backend URL after deployment:

1. Go to your frontend service on Render
2. Go to "Environment" tab
3. Update `NEXT_PUBLIC_BACKEND_API_URL` with the correct backend URL
4. Redeploy the frontend

## Environment Variables

### Backend (API)
- `GROQ_API_KEY`: Your Groq API key (required)
- `AI_PROVIDER`: Set to `groq` (default)
- `GITHUB_TOKEN`: Optional GitHub token for higher rate limits

### Frontend
- `NEXT_PUBLIC_BACKEND_API_URL`: URL of your backend API service

## Automatic Deployments

Render automatically redeploys your services when you push to your connected GitHub repository.

## Troubleshooting

### Backend Issues

1. **Port already in use**: 
   - Make sure no other processes are running on the same port
   - The backend automatically uses the PORT environment variable provided by Render
   - Locally, you can specify a different port: `PORT=8001 ./github_mvp_generator/start.sh`

2. **Python not found**: 
   - Ensure the virtual environment is properly set up
   - The build script will create and activate the virtual environment
   - Run `./github_mvp_generator/build.sh` first to set up dependencies

3. **Missing dependencies**: 
   - Check that `requirements.txt` is properly configured
   - The build script will install all required Python packages

4. **API key issues**: 
   - Verify your `GROQ_API_KEY` is correctly set in environment variables
   - Check the API key is valid and has not expired

### Frontend Issues

1. **Backend connection problems**:
   - Verify `NEXT_PUBLIC_BACKEND_API_URL` is set correctly
   - Check that the backend service is running
   - Ensure the backend URL matches the actual deployed URL

2. **Build failures**:
   - Check Node.js version compatibility
   - Ensure all npm dependencies are correctly installed
   - Clear npm cache if needed: `npm cache clean --force`

### Testing Locally

1. **Start backend**:
   ```bash
   cd github_mvp_generator
   ./build.sh
   ./start.sh
   ```

2. **Test backend**:
   ```bash
   curl http://localhost:8000/health
   ```

3. **Start frontend**:
   ```bash
   npm install
   npm run dev
   ```

## Domain Configuration (Optional)

You can add custom domains to both services in the Render dashboard:
1. Go to your service
2. Click "Settings"
3. Scroll to "Custom Domains"
4. Follow the instructions to add your domain

The application will be available at your Render URLs:
- Frontend: `https://github-mvp-generator-frontend-xyz1.onrender.com`
- Backend API: `https://github-mvp-generator-api-xyz1.onrender.com`