# AI Prompts Used by GitHub MVP Generator

This document contains all the prompts that are sent to the AI model (Groq's openai/gpt-oss-120b) when generating MVP prompts from GitHub repositories.

## 1. Project Type Prompt

```
Analyze the following GitHub repository information and determine the project type:

Repository Name: {{repo_name}}
Primary Language: {{language}}
Frameworks Detected: {{frameworks}}
Description: {{description}}

File Structure:
{% for item in contents %}
- {{ item.name }}{% endfor %}

Based on this information, determine what type of project this is. Consider:
1. The primary programming language
2. Frameworks and libraries used
3. The repository name and description
4. Files in the repository

Respond with just the project type (e.g., "React Web Application", "FastAPI Web Service", etc.).
```

## 2. Technology Stack Prompt

```
Analyze the following GitHub repository information and identify the complete technology stack:

Repository Name: {{repo_name}}
Primary Language: {{language}}
Frameworks Detected: {{frameworks}}
Description: {{description}}

File Structure:
{% for item in contents %}
- {{ item.name }}{% endfor %}

Identify all technologies, frameworks, libraries, databases, and tools used in this project. 
Be comprehensive but concise. Respond with a comma-separated list of technologies.
```

## 3. Key Features Prompt

```
Analyze the following GitHub repository information and identify the key features:

Repository Name: {{repo_name}}
Primary Language: {{language}}
Frameworks Detected: {{frameworks}}
Description: {{description}}

File Structure:
{% for item in contents %}
- {{ item.name }}{% endfor %}

Stars: {{stars}}
Forks: {{forks}}

Based on this information, identify 3-5 key features of this project. Focus on what the project does,
not how it's implemented. Each feature should be a concise phrase.

Respond with a numbered list of features:
1. Feature 1
2. Feature 2
3. Feature 3
```

## 4. Architecture Prompt

```
Analyze the following GitHub repository information and describe the architecture:

Repository Name: {{repo_name}}
Primary Language: {{language}}
Frameworks Detected: {{frameworks}}
Description: {{description}}

File Structure:
{% for item in contents %}
- {{ item.name }}{% endfor %}

Based on this information, describe the architecture pattern of this project. 
Consider things like:
- Frontend/backend separation
- Microservices vs monolith
- Component-based architecture
- Data flow patterns
- Deployment architecture

Respond with a concise description of the architecture.
```

## 5. Complexity Level Prompt

```
Analyze the following GitHub repository information and assess the complexity level:

Repository Name: {{repo_name}}
Primary Language: {{language}}
Frameworks Detected: {{frameworks}}
Description: {{description}}

Stars: {{stars}}
Forks: {{forks}}

Based on this information, assess the complexity level of this project. 
Consider factors like:
- Number of stars and forks (popularity/usage)
- Technology stack complexity
- Project size (inferred from file structure)

Respond with just the complexity level (e.g., "Beginner", "Beginner to Intermediate", 
"Intermediate", "Intermediate to Advanced", "Advanced").
```

## 6. MVP Guidance Prompt

```
Based on the following GitHub repository, provide implementation guidance for creating 
an MVP inspired by this project:

Repository Name: {{repo_name}}
Project Type: {{project_type}}
Technology Stack: {{tech_stack}}
Architecture: {{architecture}}
Key Features: 
{% for feature in features %}
- {{ feature }}{% endfor %}

Provide 5-7 high-level guidance points for implementing an MVP with similar characteristics.
Each point should be a complete sentence describing a key area of focus.

Respond with a numbered list:
1. Guidance point 1
2. Guidance point 2
3. Guidance point 3
```

## 7. Implementation Steps Prompt

```
Based on the following GitHub repository, provide step-by-step implementation instructions 
for creating an MVP inspired by this project:

Repository Name: {{repo_name}}
Project Type: {{project_type}}
Technology Stack: {{tech_stack}}
Architecture: {{architecture}}
Key Features: 
{% for feature in features %}
- {{ feature }}{% endfor %}

Provide 10 concrete implementation steps to build an MVP with similar characteristics.
Each step should be a clear action item.

Respond with a numbered list:
1. Implementation step 1
2. Implementation step 2
3. Implementation step 3
```