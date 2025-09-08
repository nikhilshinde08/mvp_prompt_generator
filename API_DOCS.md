# GitHub MVP Generator API Documentation

## Overview

The GitHub MVP Generator provides a REST API for generating MVP prompts from GitHub repositories and collecting user feedback to improve the system over time.

## Base URL

```
http://localhost:8000
```

## Endpoints

### Generate MVP Prompt

Generate an MVP prompt for a GitHub repository.

**URL**: `POST /api/generate`

**Request Body**:
```json
{
  "repo_url": "string (required) - GitHub repository URL",
  "provider": "string (optional) - AI provider (groq or openai)",
  "token": "string (optional) - GitHub personal access token"
}
```

**Response**:
```json
{
  "repo_url": "string - GitHub repository URL",
  "prompt": "string - Generated MVP prompt",
  "provider": "string - AI provider used"
}
```

### Submit Feedback

Submit feedback for a generated prompt.

**URL**: `POST /api/feedback`

**Request Body**:
```json
{
  "repo_url": "string (required) - GitHub repository URL",
  "rating": "integer (required) - Rating from 1-5",
  "comments": "string (optional) - General comments",
  "improvements": "string (optional) - Suggestions for improvement"
}
```

**Response**:
```json
{
  "message": "string - Confirmation message"
}
```

### Get System Statistics

Get system statistics and performance metrics.

**URL**: `GET /api/stats`

**Response**:
```json
{
  "performance": {
    "total_operations": "integer",
    "success_rate": "float",
    "average_response_time": "float"
  },
  "knowledge_base": {
    "framework_signatures_count": "integer",
    "successful_prompts_count": "integer",
    "repo_patterns_count": "integer"
  },
  "feedback": {
    "total_feedback": "integer",
    "average_rating": "float"
  },
  "preferences": {
    "default_provider": "string",
    "usage_count": "integer"
  }
}
```

### Get User Preferences

Get current user preferences.

**URL**: `GET /api/preferences`

**Response**:
```json
{
  "default_provider": "string",
  "preferred_tech_stacks": "array",
  "preferred_project_types": "array",
  "usage_count": "integer",
  "last_used": "string"
}
```

## Usage Examples

### Generate MVP Prompt
```bash
curl -X POST http://localhost:8000/api/generate \
  -H "Content-Type: application/json" \
  -d '{"repo_url": "https://github.com/facebook/react"}'
```

### Submit Feedback
```bash
curl -X POST http://localhost:8000/api/feedback \
  -H "Content-Type: application/json" \
  -d '{
    "repo_url": "https://github.com/facebook/react",
    "rating": 4,
    "comments": "Good analysis",
    "improvements": "Could include more tech details"
  }'
```

### Get Stats
```bash
curl http://localhost:8000/api/stats
```

### Get Preferences
```bash
curl http://localhost:8000/api/preferences
```