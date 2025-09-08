import { type NextRequest, NextResponse } from "next/server"

export async function POST(request: NextRequest) {
  try {
    const { githubUrl, rating, comments, improvements } = await request.json()

    // Validate required fields
    if (!githubUrl || rating === undefined || rating < 1 || rating > 5) {
      return NextResponse.json(
        { error: "Please provide a valid GitHub URL and rating (1-5)" },
        { status: 400 },
      )
    }

    // Call our Python backend API to submit feedback
    const backendUrl = process.env.BACKEND_API_URL || "http://localhost:8000"
    
    const response = await fetch(`${backendUrl}/api/feedback`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ 
        repo_url: githubUrl,
        rating: rating,
        comments: comments || "",
        improvements: improvements || ""
      }),
    })

    if (!response.ok) {
      const errorData = await response.json()
      throw new Error(errorData.error || "Failed to submit feedback to backend")
    }

    return NextResponse.json({
      message: "Feedback submitted successfully",
      success: true,
    })
  } catch (error) {
    console.error("Error submitting feedback:", error)
    return NextResponse.json({ 
      error: error instanceof Error ? error.message : "Failed to submit feedback. Please try again." 
    }, { status: 500 })
  }
}