# Deploying to Render.com

This guide explains how to deploy the GitHub MVP Generator application to Render.com as separate services.

## Prerequisites

1. A Render.com account (free tier available)
2. A Groq API key (get one from [Groq Console](https://console.groq.com/keys))

## Deployment Steps

### 1. Fork the Repository

First, fork this repository to your GitHub account so you can make configuration changes.

### 2. Deploy the Backend API Service

1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click "New" and select "Web Service"
3. Connect your GitHub account and select your forked repository
4. Set the following configuration:
   - **Name**: `github-mvp-generator-api`
   - **Runtime**: Python 3
   - **Region**: Choose the region closest to you
   - **Branch**: main
   - **Root Directory**: Leave empty
   - **Build Command**: `./github_mvp_generator/build.sh`
   - **Start Command**: `./github_mvp_generator/start.sh`
   - **Plan**: Free
   - **Auto Deploy**: Yes (recommended)

5. Add environment variables:
   - `GROQ_API_KEY`: Your Groq API key (keep it secret)
   - `AI_PROVIDER`: `groq` (default)

6. Click "Create Web Service"

7. Wait for the deployment to complete (this may take a few minutes)
8. Note the URL of your deployed backend service (e.g., `https://github-mvp-generator-api-xyz1.onrender.com`)

### 3. Deploy the Frontend Service

1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click "New" and select "Web Service"
3. Connect your GitHub account and select your forked repository
4. Set the following configuration:
   - **Name**: `github-mvp-generator-frontend`
   - **Runtime**: Node
   - **Region**: Choose the region closest to you
   - **Branch**: main
   - **Root Directory**: Leave empty
   - **Build Command**: `npm install && npm run build`
   - **Start Command**: `npm run start`
   - **Plan**: Free
   - **Auto Deploy**: Yes (recommended)

5. Add environment variables:
   - `NEXT_PUBLIC_BACKEND_API_URL`: The URL of your deployed backend service
   - Example: `https://github-mvp-generator-api-xyz1.onrender.com`

6. Click "Create Web Service"

7. Wait for the deployment to complete (this may take a few minutes)

## Environment Variables

### Backend (API)
- `GROQ_API_KEY`: Your Groq API key (required)
- `AI_PROVIDER`: Set to `groq` (default)
- `GITHUB_TOKEN`: Optional GitHub token for higher rate limits

### Frontend
- `NEXT_PUBLIC_BACKEND_API_URL`: URL of your deployed backend service

## Connecting the Services

After deploying both services:

1. If you didn't know your backend URL during frontend deployment:
   - Go to your frontend service on Render
   - Click "Environment" in the sidebar
   - Update `NEXT_PUBLIC_BACKEND_API_URL` with your actual backend URL
   - Click "Save Changes" to redeploy

2. The frontend will automatically make API calls to your backend service

## Testing the Deployment

After both services are deployed:

1. Visit your frontend URL (e.g., `https://github-mvp-generator-frontend-xyz1.onrender.com`)
2. You should see the GitHub MVP Generator interface
3. Enter a GitHub repository URL (e.g., `https://github.com/facebook/react`)
4. Click "Generate MVP Prompt"
5. The frontend will call your backend API to generate the prompt
6. You can also check your backend directly:
   - Health check: `https://your-backend-url.onrender.com/health`
   - API endpoints: `https://your-backend-url.onrender.com/`

## Updating Services

Render automatically redeploys your services when you push to your connected GitHub repository.

To manually redeploy:
1. Go to your service on Render
2. Click "Manual Deploy" 
3. Select "Clear build cache & deploy"

## Domain Configuration (Optional)

You can add custom domains to both services in the Render dashboard:
1. Go to your service
2. Click "Settings"
3. Scroll to "Custom Domains"
4. Follow the instructions to add your domain

The application will be available at your Render URLs:
- Frontend: `https://github-mvp-generator-frontend-xyz1.onrender.com`
- Backend API: `https://github-mvp-generator-api-xyz1.onrender.com`

## Troubleshooting

### Common Issues

1. **Frontend can't connect to backend**:
   - Verify `NEXT_PUBLIC_BACKEND_API_URL` is set correctly in the frontend service
   - Check that the backend service is running (check logs)
   - Ensure the backend URL is accessible via browser

2. **Backend fails to start**:
   - Check logs for error messages
   - Verify `GROQ_API_KEY` is correctly set
   - Ensure all dependencies are installed correctly

3. **Rate limiting**:
   - Add a `GITHUB_TOKEN` environment variable to increase GitHub API rate limits

### Checking Logs

1. Go to your service on Render
2. Click "Logs" in the sidebar
3. View real-time logs or historical logs
4. Look for error messages or warnings

### Service Health

1. Backend health check: `https://your-backend-url.onrender.com/health`
2. Frontend health check: Visit your frontend URL - it should load the application