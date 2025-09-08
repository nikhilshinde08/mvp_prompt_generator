from flask import Flask, request, jsonify
from flask_cors import CORS
from github_parser.analyzer import GitHubRepoAnalyzer
from ai.generator import AIEnhancedGenerator
from config import GITHUB_TOKEN, AI_PROVIDER
from feedback import feedback_system
from user_preferences import user_preferences
from knowledge_base import knowledge_base
from performance_metrics import performance_metrics
import os
import sys
import time

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def home():
    return jsonify({
        "message": "GitHub MVP Generator API",
        "endpoints": {
            "generate_mvp": "POST /api/generate",
            "submit_feedback": "POST /api/feedback",
            "get_stats": "GET /api/stats",
            "get_preferences": "GET /api/preferences"
        }
    })

@app.route('/api/generate', methods=['POST'])
def generate_mvp():
    """Generate MVP prompt for a GitHub repository"""
    data = request.get_json()
    
    if not data or 'repo_url' not in data:
        return jsonify({"error": "repo_url is required"}), 400
    
    repo_url = data['repo_url']
    provider = data.get('provider', AI_PROVIDER)
    github_token = data.get('token', GITHUB_TOKEN)
    
    try:
        # Start performance tracking
        operation = performance_metrics.start_operation("mvp_generation", provider)
        
        # Initialize analyzer
        analyzer = GitHubRepoAnalyzer(github_token)
        
        # Analyze the repository
        repo_data = analyzer.analyze_repo(repo_url)
        
        # Generate MVP prompt
        ai_generator = AIEnhancedGenerator(provider)
        prompt = ai_generator.generate_prompt(repo_data, repo_url)
        
        # End performance tracking
        performance_metrics.end_operation(operation, success=True)
        
        return jsonify({
            "repo_url": repo_url,
            "prompt": prompt,
            "provider": provider
        })
        
    except Exception as e:
        # End performance tracking with error
        if 'operation' in locals():
            performance_metrics.end_operation(operation, success=False, error=str(e))
        return jsonify({"error": str(e)}), 500

@app.route('/api/feedback', methods=['POST'])
def submit_feedback():
    """Submit feedback for a generated prompt"""
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "Request body is required"}), 400
    
    required_fields = ['repo_url', 'rating']
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400
    
    try:
        feedback_system.submit_feedback(
            data['repo_url'],
            data['rating'],
            data.get('comments', ''),
            data.get('improvements', '')
        )
        
        return jsonify({"message": "Feedback submitted successfully"})
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get system statistics"""
    try:
        perf_summary = performance_metrics.get_performance_summary()
        kb_stats = knowledge_base.get_knowledge_stats()
        feedback_summary = feedback_system.get_feedback_summary()
        prefs = user_preferences.get_all_preferences()
        
        return jsonify({
            "performance": perf_summary,
            "knowledge_base": kb_stats,
            "feedback": feedback_summary,
            "preferences": {
                "default_provider": prefs.get('default_provider'),
                "usage_count": prefs.get('usage_count', 0),
                "preferred_tech_stacks_count": len(prefs.get('preferred_tech_stacks', [])),
                "preferred_project_types_count": len(prefs.get('preferred_project_types', []))
            }
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/preferences', methods=['GET'])
def get_preferences():
    """Get user preferences"""
    try:
        prefs = user_preferences.get_all_preferences()
        return jsonify(prefs)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/health')
def health_check():
    """Health check endpoint for deployment verification"""
    return jsonify({
        "status": "healthy",
        "message": "GitHub MVP Generator API is running",
        "timestamp": str(int(time.time()))
    })

if __name__ == '__main__':
    # Use the PORT environment variable from Render.com, default to 8000 for local development
    port = int(os.environ.get('PORT', 8000))
    app.run(debug=False, host='0.0.0.0', port=port)