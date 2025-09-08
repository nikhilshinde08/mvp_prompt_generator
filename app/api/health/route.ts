import { type NextRequest, NextResponse } from "next/server"

export async function GET(request: NextRequest) {
  return NextResponse.json({
    status: "healthy",
    message: "GitHub MVP Generator Frontend is running",
    timestamp: new Date().toISOString()
  })
}