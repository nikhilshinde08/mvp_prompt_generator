# AI-Powered GitHub MVP Generator

This document explains how to use the AI-powered features of the GitHub MVP Generator.

## Overview

The GitHub MVP Generator now uses only AI-powered analysis to generate MVP prompts. It leverages large language models to provide accurate and detailed analysis of GitHub repositories.

## Supported AI Providers

1. **OpenAI** - GPT models (gpt-4o-mini, gpt-4, etc.)
2. **Groq** - Llama models (llama3, mixtral, etc.)

## Setup

### 1. Get API Keys

#### OpenAI
1. Visit [OpenAI Platform](https://platform.openai.com/api-keys)
2. Create an account or sign in
3. Generate a new API key
4. Copy the key for use in configuration

#### Groq
1. Visit [Groq Console](https://console.groq.com/keys)
2. Create an account or sign in
3. Generate a new API key
4. Copy the key for use in configuration

### 2. Configure Environment Variables

Add your API keys to the `.env` file:

```env
# For OpenAI
OPENAI_API_KEY=your_openai_api_key_here

# For Groq
GROQ_API_KEY=your_groq_api_key_here
```

### 3. Provider Selection

In your `.env` file, select your preferred provider:

```env
# Choose provider (openai or groq)
AI_PROVIDER=openai
```

## Usage

### Command Line Options

```bash
# Use default provider (as configured in .env)
python main.py <github_repo_url>

# Specify provider explicitly
python main.py <github_repo_url> --provider openai
python main.py <github_repo_url> --provider groq
```

### Examples

```bash
# AI-powered generation with default provider
python main.py https://github.com/facebook/react

# AI-powered generation with OpenAI
python main.py https://github.com/facebook/react --provider openai

# AI-powered generation with Groq
python main.py https://github.com/facebook/react --provider groq
```

## Benefits of AI-Powered Generation

1. **Deep Understanding** - AI can parse README files and documentation to better understand project purpose
2. **Accurate Technology Detection** - AI can identify technologies not easily detected by file names alone
3. **Detailed Feature Extraction** - AI can extract meaningful features from project descriptions
4. **Context-Aware Guidance** - AI-generated guidance is more specific to the actual project
5. **Improved Implementation Steps** - AI can suggest more relevant implementation approaches

## Cost Considerations

- **OpenAI**: Pay-per-use pricing based on tokens consumed
- **Groq**: Free tier with rate limits, paid tiers for higher usage

Monitor your usage to manage costs appropriately.

## Troubleshooting

### API Key Issues
- Ensure API keys are correctly set in `.env` file
- Verify keys have appropriate permissions
- Check for typos or extra spaces

### Rate Limiting
- Both providers have rate limits
- Consider using different providers for different projects
- Implement retry logic for production use

### Model Selection
- Different models have different capabilities
- `gpt-4` and `llama3` are generally more capable but more expensive
- `gpt-4o-mini` and smaller models are more cost-effective for simpler tasks