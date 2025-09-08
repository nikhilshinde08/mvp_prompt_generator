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

1. **Backend fails to start**: Check that your `GROQ_API_KEY` is correctly set
2. **Frontend can't connect to backend**: Verify `NEXT_PUBLIC_BACKEND_API_URL` is set correctly
3. **Rate limiting**: Add a `GITHUB_TOKEN` to increase GitHub API rate limits

## Domain Configuration (Optional)

You can add custom domains to both services in the Render dashboard:
1. Go to your service
2. Click "Settings"
3. Scroll to "Custom Domains"
4. Follow the instructions to add your domain

The application will be available at your Render URLs:
- Frontend: `https://github-mvp-generator-frontend-xyz1.onrender.com`
- Backend API: `https://github-mvp-generator-api-xyz1.onrender.com`