# GitHub MVP Generator

A Python tool that transforms any GitHub repository into an MVP (Minimum Viable Product) prompt for bootstrapping new projects based on proven open-source implementations.

## What It Does

This tool analyzes GitHub repositories and generates structured MVP prompts that can be used to:
- Bootstrap new projects based on proven open-source implementations
- Learn how popular projects are structured
- Create implementation plans for new features
- Generate coding exercises and assignments

## Features

- Analyze any public GitHub repository
- Generate structured MVP prompts with project type, tech stack, and architecture
- Provide implementation guidance and step-by-step instructions
- Support for various project types and technologies
- **AI-Powered Generation** - Uses Groq's openai/gpt-oss-120b model for accurate analysis
- **Learning System** - Improves with each use through feedback and pattern recognition

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd github-mvp-generator
```

2. Run the setup script:
```bash
./setup.sh
```

Or manually set up:

2a. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

2b. Install dependencies:
```bash
pip install -r requirements.txt
```

2c. Create a `.env` file with your API keys:
```bash
cp .env.example .env
# Edit .env to add your API keys
```

## AI-Powered Generation

The tool uses Groq's openai/gpt-oss-120b model to generate accurate and detailed MVP prompts:

### Setup Groq API

1. Get a Groq API key:
   - Use the provided API key or get your own from [Groq](https://console.groq.com/keys)
   - Add to your `.env` file:
     ```
     GROQ_API_KEY=your_groq_api_key_here
     ```

### Configuration

You can configure AI settings in your `.env` file:
```env
# Choose provider (groq)
AI_PROVIDER=groq

# Model selection
GROQ_MODEL=openai/gpt-oss-120b
```

## Learning System

The GitHub MVP Generator includes an intelligent learning system that improves with each use:

### Feedback Loop
Provide feedback on generated prompts to help the system learn:
```bash
python main.py <repo_url> --feedback 4 "Good structure but could include more tech details"
```

### Adaptive Generation
The system adapts prompt generation based on:
- User preferences and history
- Feedback patterns
- Successful generation templates
- Performance metrics

### Knowledge Base
The system builds a knowledge base of:
- Repository analysis patterns
- Successful prompt templates
- Tech stack combinations
- Framework signatures

### Performance Tracking
Monitor system performance with:
```bash
python main.py --stats
```

## Usage

### Command Line Interface

#### Basic Usage
```bash
python main.py <github_repo_url>
```

#### Specify AI Provider
```bash
python main.py <github_repo_url> --provider groq
```

#### Provide Feedback
```bash
python main.py <github_repo_url> --feedback RATING "Your feedback comments"
```

Examples:
```bash
python main.py https://github.com/facebook/react
python main.py https://github.com/torvalds/linux --feedback 5 "Excellent analysis of the kernel architecture"
```

With a GitHub token:
```bash
python main.py https://github.com/facebook/react --token YOUR_GITHUB_TOKEN
```

#### View System Statistics
```bash
python main.py --stats
```

### API Endpoints

The GitHub MVP Generator also provides a REST API for programmatic access:

#### Start the API Server
```bash
python api.py
```

#### API Endpoints

1. **Generate MVP Prompt**
   - Endpoint: `POST /api/generate`
   - Description: Generate an MVP prompt for a GitHub repository
   - Request Body:
     ```json
     {
       "repo_url": "https://github.com/facebook/react",
       "provider": "groq",  // Optional
       "token": "YOUR_GITHUB_TOKEN"  // Optional
     }
     ```
   - Response:
     ```json
     {
       "repo_url": "https://github.com/facebook/react",
       "prompt": "Generated MVP prompt...",
       "provider": "groq"
     }
     ```

2. **Submit Feedback**
   - Endpoint: `POST /api/feedback`
   - Description: Submit feedback for a generated prompt
   - Request Body:
     ```json
     {
       "repo_url": "https://github.com/facebook/react",
       "rating": 4,
       "comments": "Good analysis",
       "improvements": "Could include more tech details"
     }
     ```
   - Response:
     ```json
     {
       "message": "Feedback submitted successfully"
     }
     ```

3. **Get System Statistics**
   - Endpoint: `GET /api/stats`
   - Description: Get system performance and usage statistics
   - Response:
     ```json
     {
       "performance": {...},
       "knowledge_base": {...},
       "feedback": {...},
       "preferences": {...}
     }
     ```

4. **Get User Preferences**
   - Endpoint: `GET /api/preferences`
   - Description: Get current user preferences
   - Response:
     ```json
     {
       "default_provider": "groq",
       "preferred_tech_stacks": [...],
       "preferred_project_types": [...],
       "usage_count": 5
     }
     ```

## Example Output

```
Build an MVP inspired by: @https://github.com/facebook/react

PROJECT TYPE: JavaScript UI Library (React)
TECH STACK: JavaScript, React, React Native, Vue.js, Angular, Express.js, Node.js, npm, ESLint, Prettier, EditorConfig, Watchman, NVM, Git, GitHub (including Actions/workflows), CodeSandbox.
ARCHITECTURE: **Architecture Overview**

| Aspect | What the repo tells us |
|--------|------------------------|
| **Overall pattern** | A **monolithic, library-first** codebase that is shipped as an npm package. It does not contain separate services or a dedicated backend; instead it provides a set of reusable JavaScript modules that can be consumed by any front-end (or server-side) application. |
| **Frontend / Backend separation** | The project itself is **frontend-oriented** (the React UI library). The only "backend-ish" piece is a small Express-based entry point used for documentation / demo servers and for server-side rendering helpers. This is bundled together with the library rather than being a separate micro-service. |
| **Microservices vs. Monolith** | **Monolith** – all source lives in a single repository and is built/published as one package (`react`). The repository does not expose independent deployable services. |
| **Component-based architecture** | React is fundamentally **component-centric**. The code is organized into small, isolated modules (e.g., `ReactElement`, `ReactDOM`, `hooks`, `scheduler`, etc.) that export functions/classes. Each module follows the **single-responsibility principle** and can be imported individually. |
| **Data-flow patterns** | - **One-way (unidirectional) data flow**: Props flow down, events flow up. 
- **Virtual DOM diffing** and **reconciliation** handle state changes efficiently. 
- **Hooks** provide a functional, declarative way to manage state and side-effects. 
- No built-in global state store (Redux, Context API are optional add-ons). |
| **Deployment / Distribution** | - Packaged and published to **npm** as a CommonJS/ESM bundle. 
- Consumed by any front-end framework (React, Vue, Angular) via the standard JavaScript module system. 
- The small Express server (used for docs, SSR demos) can be run locally with `npm start` but is not part of the production deployment of consumer apps. |
| **Tooling / Build** | Uses standard JavaScript tooling: ESLint, Prettier, Babel/TypeScript (if present), Jest for tests, and a CI pipeline (GitHub Actions). The presence of `.codesandbox`, `.watchmanconfig`, etc., indicates a developer-friendly environment rather than a runtime architecture. |

### Concise Description
The **React** repository is a **monolithic, component-based JavaScript library** that follows a **unidirectional data-flow** model. It is built as a single npm package, with a small Express server only for documentation/SSR demos, not a separate backend service. The architecture emphasizes modular, reusable UI components and hooks, and is intended to be consumed by any front-end stack (React, Vue, Angular) rather than being a multi-service application. Deployment is simply publishing the compiled bundles to npm, after which consumer applications handle their own front-end/back-end separation.

KEY FEATURES:
1. Declarative component-based UI rendering
2. Efficient Virtual DOM diffing and updates
3. Cross-platform support for web and native (React Native)
4. Extensive ecosystem of reusable components and tools

COMPLEXITY LEVEL: Advanced

MVP GUIDANCE:
1. **Define a core, modular component library** – Start by designing a small set of reusable UI components (e.g., Button, Input, Card) that follow a single-responsibility principle and can be imported individually, mirroring React's component-centric architecture.
2. **Adopt unidirectional data flow with hooks** – Implement state management using functional hooks (e.g., `useState`, `useEffect`) so that props flow downwards and events bubble up, ensuring predictable updates and easy testing.
3. **Set up a lightweight Express demo server** – Create a minimal Express application that serves a static documentation site and provides a server-side rendering (SSR) endpoint for your components, allowing stakeholders to preview the UI without building a full backend.
4. **Configure a robust build and publishing pipeline** – Use Babel (or TypeScript) to compile source to both CommonJS and ES-module formats, integrate ESLint/Prettier for code quality, add Jest for unit tests, and automate npm publishing with GitHub Actions to deliver a single npm package.
5. **Provide clear consumption examples for multiple frameworks** – Write short usage demos showing how the library can be imported in plain React, React Native, Vue, and Angular projects, demonstrating its framework-agnostic nature and encouraging broader adoption.
6. **Implement a basic CI/CD workflow** – Set up GitHub Actions to run linting, tests, and bundle generation on every push, and to publish a prerelease tag for each merged PR, ensuring that the MVP stays stable and continuously deliverable.
7. **Document the component API and contribution guidelines** – Create a concise README, JSDoc comments, and a living style guide (e.g., using Storybook) that outlines props, events, and styling conventions, making it easy for other developers to extend the library in the future.

IMPLEMENTATION STEPS:
1. **Initialize a monorepo and scaffold the library**
2. **Set up the development environment & tooling**
3. **Add TypeScript (or Babel) compilation pipeline**
4. **Design the component-based module layout**
5. **Implement a minimal Virtual DOM & reconciler**
6. **Add a lightweight Express demo server (docs/SSR)**
7. **Configure CI/CD with GitHub Actions**
8. Checkout code.
9. Set up Node (`actions/setup-node@v4`).
10. Install deps, run lint, format check, run tests, and build the library.
11. **Write a minimal usage example and publish to CodeSandbox**
12. **Prepare the package for npm distribution**
13. **Document the MVP (README, API docs, contribution guide)**

Focus on creating a clean, functional implementation that demonstrates the core concepts of the original project.
```

## API Rate Limits

GitHub's API has rate limits:
- Unauthenticated requests: 60 requests per hour
- Authenticated requests: 5000 requests per hour

To increase your rate limit, create a GitHub personal access token:
1. Go to https://github.com/settings/tokens
2. Generate a new token with appropriate permissions
3. Add it to your `.env` file or use the `--token` flag

## Project Structure

```
github-mvp-generator/
├── main.py                 # Main CLI interface
├── api.py                  # REST API interface
├── api_endpoints.json      # API documentation
├── config.py               # Configuration settings
├── requirements.txt        # Python dependencies
├── README.md               # This file
├── .env                    # Environment configuration
├── .gitignore             # Git ignore patterns
├── setup.sh               # Setup script
├── run.sh                 # Run script
├── run_tests.sh           # Test script
├── demo.py                # Demo script
├── demo_learning.py        # Learning system demo
├── test_learning_system.py # Learning system tests
├── test_api.py            # API tests
├── feedback.py             # Feedback system
├── user_preferences.py     # User preferences system
├── knowledge_base.py       # Knowledge base system
├── performance_metrics.py  # Performance metrics system
├── adaptive_prompt.py      # Adaptive prompt system
├── github_parser/         # GitHub repository analysis
│   └── analyzer.py        # Repository analyzer
├── ai/                    # AI-powered generation
│   ├── client.py          # AI client abstraction
│   ├── generator.py       # AI-powered generator
│   ├── providers/         # AI provider implementations
│   │   ├── openai.py      # OpenAI provider
│   │   └── groq.py        # Groq provider
│   └── templates/         # AI prompt templates
├── examples/              # Example scripts
│   └── generate_example.py # Example output generator
├── tests/                 # Unit tests
│   └── test_generator.py  # Test cases
└── docs/                  # Documentation
    ├── installation.md    # Installation guide
    ├── usage.md           # Usage instructions
    └── examples.md        # Usage examples
```

## Testing

Run the unit tests:
```bash
./run_tests.sh
```

Or manually:
```bash
source venv/bin/activate
python -m unittest tests/test_generator.py
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a pull request

## License

MIT License