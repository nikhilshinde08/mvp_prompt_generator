"use client"

import { useState, useEffect } from "react"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Textarea } from "@/components/ui/textarea"
import { Badge } from "@/components/ui/badge"
import { GitBranch, Link, Sparkles, Copy, Check } from "lucide-react"
import { useToast } from "@/hooks/use-toast"
import { FeedbackForm } from "@/components/feedback-form"

export default function HomePage() {
  const [githubUrl, setGithubUrl] = useState("")
  const [generatedPrompt, setGeneratedPrompt] = useState("")
  const [isGenerating, setIsGenerating] = useState(false)
  const [copied, setCopied] = useState(false)
  const [stats, setStats] = useState<any>(null)
  const [showFeedback, setShowFeedback] = useState(false)
  const { toast } = useToast()

  // Fetch stats on component mount
  useEffect(() => {
    fetchStats()
  }, [])

  const fetchStats = async () => {
    try {
      const backendUrl = process.env.NEXT_PUBLIC_BACKEND_API_URL || "http://localhost:5000"
      const response = await fetch(`${backendUrl}/api/stats`)
      
      if (response.ok) {
        const data = await response.json()
        setStats(data)
      }
    } catch (error) {
      console.error("Failed to fetch stats:", error)
    }
  }

  const generatePrompt = async () => {
    if (!githubUrl.trim()) {
      toast({
        title: "Error",
        description: "Please enter a GitHub repository URL",
        variant: "destructive",
      })
      return
    }

    setIsGenerating(true)
    setShowFeedback(false)

    try {
      const response = await fetch("/api/generate-prompt", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ githubUrl: githubUrl.trim() }),
      })

      const data = await response.json()

      if (!response.ok) {
        throw new Error(data.error || "Failed to generate prompt")
      }

      setGeneratedPrompt(data.prompt)
      toast({
        title: "Success",
        description: "MVP prompt generated successfully!",
      })
    } catch (error) {
      toast({
        title: "Error",
        description: error instanceof Error ? error.message : "Failed to generate prompt",
        variant: "destructive",
      })
    } finally {
      setIsGenerating(false)
    }
  }

  const copyToClipboard = async () => {
    try {
      await navigator.clipboard.writeText(generatedPrompt)
      setCopied(true)
      toast({
        title: "Copied!",
        description: "Prompt copied to clipboard",
      })
      setTimeout(() => setCopied(false), 2000)
    } catch (err) {
      toast({
        title: "Error",
        description: "Failed to copy to clipboard",
        variant: "destructive",
      })
    }
  }

  const handleFeedbackSubmitted = () => {
    setShowFeedback(false)
    fetchStats() // Refresh stats after feedback submission
    toast({
      title: "Thank You!",
      description: "Your feedback helps us improve.",
    })
  }

  return (
    <div className="min-h-screen bg-background">
      {/* Header */}
      <header className="border-b bg-card/50 backdrop-blur-sm sticky top-0 z-50">
        <div className="container mx-auto px-4 py-4">
          <div className="flex items-center gap-3">
            <div className="flex items-center gap-2">
              <GitBranch className="h-8 w-8 text-primary" />
              <h1 className="text-2xl font-bold text-card-foreground">GitHub MVP Generator</h1>
            </div>
            <Badge variant="secondary" className="ml-auto">
              AI-Powered
            </Badge>
          </div>
        </div>
      </header>

      <main className="container mx-auto px-4 py-8 max-w-4xl">
        {/* Hero Section */}
        <section className="text-center space-y-4 mb-12">
          <h2 className="text-4xl font-bold text-balance text-foreground">Generate MVP Prompts from GitHub Repos</h2>
          <p className="text-xl text-muted-foreground max-w-2xl mx-auto text-pretty">
            Paste any GitHub repository URL and get an intelligent, comprehensive prompt for building your MVP
          </p>
        </section>

        {/* Stats Section */}
        {stats && (
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-8">
            <Card>
              <CardContent className="p-4 text-center">
                <div className="text-2xl font-bold">{stats.performance?.total_operations || 0}</div>
                <div className="text-sm text-muted-foreground">Total Generations</div>
              </CardContent>
            </Card>
            <Card>
              <CardContent className="p-4 text-center">
                <div className="text-2xl font-bold">{stats.performance?.success_rate ? `${Math.round(stats.performance.success_rate)}%` : '0%'}</div>
                <div className="text-sm text-muted-foreground">Success Rate</div>
              </CardContent>
            </Card>
            <Card>
              <CardContent className="p-4 text-center">
                <div className="text-2xl font-bold">{stats.feedback?.total_feedback || 0}</div>
                <div className="text-sm text-muted-foreground">Feedback Received</div>
              </CardContent>
            </Card>
            <Card>
              <CardContent className="p-4 text-center">
                <div className="text-2xl font-bold">{stats.feedback?.average_rating ? stats.feedback.average_rating.toFixed(1) : '0.0'}</div>
                <div className="text-sm text-muted-foreground">Average Rating</div>
              </CardContent>
            </Card>
          </div>
        )}

        {/* Input Section */}
        <Card className="mb-8">
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <Link className="h-5 w-5" />
              GitHub Repository URL
            </CardTitle>
            <CardDescription>Enter the URL of the GitHub repository you want to analyze</CardDescription>
          </CardHeader>
          <CardContent className="space-y-4">
            <div className="flex gap-2">
              <Input
                placeholder="https://github.com/username/repository"
                value={githubUrl}
                onChange={(e) => setGithubUrl(e.target.value)}
                className="flex-1"
              />
              <Button onClick={generatePrompt} disabled={isGenerating} className="gap-2">
                {isGenerating ? (
                  <>
                    <div className="animate-spin rounded-full h-4 w-4 border-2 border-current border-t-transparent" />
                    Analyzing...
                  </>
                ) : (
                  <>
                    <Sparkles className="h-4 w-4" />
                    Generate Prompt
                  </>
                )}
              </Button>
            </div>
            <p className="text-sm text-muted-foreground">
              Example: https://github.com/facebook/react or https://github.com/vercel/next.js
            </p>
          </CardContent>
        </Card>

        {/* Generated Prompt Section */}
        {generatedPrompt && (
          <Card className="mb-8">
            <CardHeader>
              <div className="flex items-center justify-between">
                <CardTitle className="flex items-center gap-2">
                  <Sparkles className="h-5 w-5" />
                  Generated MVP Prompt
                </CardTitle>
                <Button variant="outline" size="sm" onClick={copyToClipboard} className="gap-2 bg-transparent">
                  {copied ? (
                    <>
                      <Check className="h-4 w-4" />
                      Copied
                    </>
                  ) : (
                    <>
                      <Copy className="h-4 w-4" />
                      Copy
                    </>
                  )}
                </Button>
              </div>
              <CardDescription>
                Use this prompt with your favorite AI assistant to get detailed MVP guidance
              </CardDescription>
            </CardHeader>
            <CardContent>
              <Textarea value={generatedPrompt} readOnly className="min-h-[400px] font-mono text-sm" />
            </CardContent>
          </Card>
        )}

        {/* Feedback Section */}
        {generatedPrompt && !showFeedback && (
          <div className="mb-8 text-center">
            <Button onClick={() => setShowFeedback(true)} variant="outline">
              Provide Feedback on This Prompt
            </Button>
          </div>
        )}

        {showFeedback && generatedPrompt && (
          <div className="mb-8">
            <FeedbackForm 
              githubUrl={githubUrl} 
              onFeedbackSubmitted={handleFeedbackSubmitted} 
            />
          </div>
        )}

        {/* How it Works */}
        <section className="mt-12 space-y-6">
          <h3 className="text-2xl font-semibold text-foreground text-center">How It Works</h3>
          <div className="grid gap-6 md:grid-cols-3">
            <Card>
              <CardHeader>
                <div className="flex items-center gap-2">
                  <div className="w-8 h-8 rounded-full bg-primary text-primary-foreground flex items-center justify-center font-bold">
                    1
                  </div>
                  <CardTitle className="text-lg">Paste GitHub URL</CardTitle>
                </div>
              </CardHeader>
              <CardContent>
                <p className="text-sm text-muted-foreground">
                  Simply paste any public GitHub repository URL into the input field above
                </p>
              </CardContent>
            </Card>

            <Card>
              <CardHeader>
                <div className="flex items-center gap-2">
                  <div className="w-8 h-8 rounded-full bg-primary text-primary-foreground flex items-center justify-center font-bold">
                    2
                  </div>
                  <CardTitle className="text-lg">AI Analysis</CardTitle>
                </div>
              </CardHeader>
              <CardContent>
                <p className="text-sm text-muted-foreground">
                  Our system analyzes the repository structure, technologies, and creates a tailored prompt
                </p>
              </CardContent>
            </Card>

            <Card>
              <CardHeader>
                <div className="flex items-center gap-2">
                  <div className="w-8 h-8 rounded-full bg-primary text-primary-foreground flex items-center justify-center font-bold">
                    3
                  </div>
                  <CardTitle className="text-lg">Get MVP Plan</CardTitle>
                </div>
              </CardHeader>
              <CardContent>
                <p className="text-sm text-muted-foreground">
                  Copy the generated prompt and use it with any AI assistant to get your MVP development plan
                </p>
              </CardContent>
            </Card>
          </div>
        </section>
      </main>

      {/* Footer */}
      <footer className="border-t bg-card/30 mt-16">
        <div className="container mx-auto px-4 py-8">
          <div className="text-center text-sm text-muted-foreground">
            <p>GitHub MVP Generator - Transform repositories into actionable MVP plans</p>
            <p className="mt-2">Built with AI, designed for developers</p>
          </div>
        </div>
      </footer>
    </div>
  )
}
