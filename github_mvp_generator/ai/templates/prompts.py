"""
AI prompt templates for project type analysis (FINAL VERSION, CLEAN).
- Uses "Reference Examples" internally (not embedded).
- All prompts request DETAILED, REPO-SPECIFIC outputs (not generic).
- Templates use Jinja-style placeholders ({{...}}) and loops for file lists.
"""

# ----------------------------
# Prompt templates
# ----------------------------

PROJECT_TYPE_PROMPT = """
You are a senior software analyst with deep experience classifying and describing GitHub repositories.
Task: Determine the PROJECT TYPE and provide a DETAILED justification (1–2 sentences) explaining your reasoning.

Repository Context:
Repository Name: {{repo_name}}
Primary Language: {{language}}
Frameworks Detected: {{frameworks}}
Description: {{description}}

File Structure:
{% for item in contents %}
- {{ item.name }}
{% endfor %}

Analysis Steps (follow exactly):
1. Explain how the primary language influences the project type.
2. Explain how the detected frameworks/libraries influence the classification.
3. Use the repository name and description to infer purpose.
4. Validate assumptions against the file structure (mention 1–2 files that support your conclusion).
5. Output the PROJECT TYPE in a single line, followed by a 1–2 sentence justification.

Output Requirements:
- Include "PROJECT TYPE:" followed by the type.
- Immediately below, include "REASONING:" with 1–2 sentences.
"""

TECH_STACK_PROMPT = """
Task: Identify the complete TECHNOLOGY STACK used in the repository and provide brief context for each major item.

Repository Details:
- Repository Name: {{repo_name}}
- Primary Language: {{language}}
- Frameworks Detected: {{frameworks}}
- Description: {{description}}

File Structure:
{% for item in contents %}
- {{ item.name }}
{% endfor %}

Analysis Steps:
1. Enumerate programming languages and runtimes.
2. Enumerate frameworks and libraries; add 1-line role for each.
3. List databases, storage, and important tools (CI, containerization, packaging).
4. If uncertain, mark as "inferred" and explain.

Output Requirements:
- "TECH STACK:" block with comma-separated list.
- Below: bullet notes describing major items.
"""

FEATURES_PROMPT = """
Task: Extract 3–5 KEY FEATURES of the project (focus on what it does). For each, provide a short explanatory sentence.

Repository Info:
- Repository Name: {{repo_name}}
- Primary Language: {{language}}
- Frameworks Detected: {{frameworks}}
- Description: {{description}}
Stars: {{stars}}
Forks: {{forks}}

File Structure:
{% for item in contents %}
- {{ item.name }}
{% endfor %}

Analysis Steps:
1. Identify 3–5 core capabilities.
2. Add a 1-sentence explanation for each.
3. Prioritize user-facing and developer tooling features.

Output Requirements:
KEY FEATURES:
1. Feature — explanation.
2. Feature — explanation.
(3–5 total)
"""

ARCHITECTURE_PROMPT = """
Task: Describe the ARCHITECTURE of the project in 4–8 sentences. Mention pattern, components, data flow, and deployment if possible.

Repository Info:
- Repository Name: {{repo_name}}
- Primary Language: {{language}}
- Frameworks Detected: {{frameworks}}
- Description: {{description}}

File Structure:
{% for item in contents %}
- {{ item.name }}
{% endfor %}

Analysis Steps:
1. Identify frontend/backend separation and modules.
2. Describe data flow and persistence.
3. State if monolithic, modular, microservices, or CLI.
4. Note deployment/runtime constraints.

Output Requirements:
- "ARCHITECTURE:" followed by 4–8 sentence paragraph.
"""

COMPLEXITY_PROMPT = """
Task: Assess the COMPLEXITY LEVEL of the project and justify with 2–4 bullets.

Repository Info:
- Repository Name: {{repo_name}}
- Primary Language: {{language}}
- Frameworks Detected: {{frameworks}}
- Description: {{description}}
Stars: {{stars}}
Forks: {{forks}}

Analysis Steps:
1. Consider stars/forks, stack complexity, and file list size.
2. Choose: "Beginner", "Beginner to Intermediate", "Intermediate", "Intermediate to Advanced", "Advanced".
3. Provide 2–4 supporting bullets.

Output Requirements:
COMPLEXITY LEVEL: <label>
REASONS:
- Reason 1
- Reason 2
"""

MVP_GUIDANCE_PROMPT = """
Role: Expert software consultant. Produce highly detailed, repo-specific MVP guidance.

Input:
Repository Name: {{repo_name}}
Project Type: {{project_type}}
Technology Stack: {{tech_stack}}
Architecture: {{architecture}}
Key Features:
{% for feature in features %}
- {{ feature }}
{% endfor %}
File Structure:
{% for item in contents %}
- {{ item.name }}
{% endfor %}

Task: Produce 6-8 highly detailed repo-specific guidance sections (3-6 sentences each) that will help developers quickly create an MVP clone of this repository. Each section must include:
- Descriptive title that clearly explains the focus area
- Detailed explanation of what to implement and why
- 2-4 exact files from File Structure to edit/create with specific paths
- Exact commands needed (package manager, build tools, etc.)
- Complete code snippet (8-15 lines) with filename comment
- Common pitfalls developers face + how to avoid them
- Best practices specific to this repository's patterns

Additional Requirements:
- Reference specific files, patterns, and conventions from the original repo
- Include technology-specific details based on the tech stack
- Focus on the most important 20% of features that deliver 80% of value
- Prioritize implementation order that builds a working core quickly
- Mention any unique architectural patterns or design decisions
- Include testing considerations specific to this repo's approach

Extra Outputs:
- DETAILED FILE-TO-FEATURE MAP: map each key feature to specific files with implementation notes
- BRANCHING STRATEGY: recommended git branching with 4-5 specific commit messages
- QUICK START: 3-5 commands to get a basic version running immediately
"""

IMPLEMENTATION_STEPS_PROMPT = """
Task: Provide 12 CONCRETE, repo-specific implementation steps with extensive detail. Each step must be actionable with exact commands, file paths, and code snippets.

Repository Context:
Repository Name: {{repo_name}}
Project Type: {{project_type}}
Technology Stack: {{tech_stack}}
Architecture: {{architecture}}
Key Features:
{% for feature in features %}
- {{ feature }}
{% endfor %}
File Structure:
{% for item in contents %}
- {{ item.name }}
{% endfor %}

Rules for Each Step:
1. Numbered list 1–12 with clear, actionable titles
2. Each step = Goal + Files to create/edit + Exact commands + Complete code/config snippet (8-15 lines with filename)
3. Include dependency installation commands with exact package names
4. Show configuration file changes with complete content
5. If no clear entrypoint, infer one (mark "inferred") with reasoning
6. Reference repo-specific CI/Docker files if they exist
7. Include testing steps specific to each implementation
8. Add verification commands to confirm successful implementation

Extra Outputs (Detailed):
- COMPLETE FILE CHANGES: comprehensive list of 15-30 files needed for full MVP with brief purpose
- VALIDATION TESTS: 5-7 specific tests to verify functionality (curl commands, manual checks, unit tests)
- CI/CD UPGRADES: 6-8 steps to enhance workflow (reference specific workflow paths)
- PERFORMANCE OPTIMIZATIONS: 4-6 repo-specific optimizations to implement
"""
