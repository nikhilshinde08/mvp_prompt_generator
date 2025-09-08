import { type NextRequest, NextResponse } from "next/server"

export async function POST(request: NextRequest) {
  try {
    const { githubUrl } = await request.json()

    // Validate GitHub URL format
    const githubRegex = /^https:\/\/github\.com\/[\w\-.]+\/[\w\-.]+\/?$/
    if (!githubUrl || !githubRegex.test(githubUrl.trim())) {
      return NextResponse.json(
        { error: "Please enter a valid GitHub repository URL (e.g., https://github.com/user/repo)" },
        { status: 400 },
      )
    }

    // Extract repository information
    const repoName = githubUrl.split("/").slice(-2).join("/")

    // Call our Python backend API
    const backendUrl = process.env.BACKEND_API_URL || "http://localhost:8000"
    
    const response = await fetch(`${backendUrl}/api/generate`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ 
        repo_url: githubUrl,
        provider: "groq" // Default to Groq, can be changed based on env or user preference
      }),
    })

    if (!response.ok) {
      const errorData = await response.json()
      throw new Error(errorData.error || "Failed to generate prompt from backend")
    }

    const data = await response.json()

    return NextResponse.json({
      prompt: data.prompt,
      repoName,
      success: true,
    })
  } catch (error) {
    console.error("Error generating prompt:", error)
    return NextResponse.json({ 
      error: error instanceof Error ? error.message : "Failed to generate prompt. Please try again." 
    }, { status: 500 })
  }
}
