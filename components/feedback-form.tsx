"use client"

import { useState } from "react"
import { Button } from "@/components/ui/button"
import { Textarea } from "@/components/ui/textarea"
import { Label } from "@/components/ui/label"
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { useToast } from "@/hooks/use-toast"
import { Star } from "lucide-react"

export function FeedbackForm({ githubUrl, onFeedbackSubmitted }: { githubUrl: string; onFeedbackSubmitted: () => void }) {
  const [rating, setRating] = useState<string>("")
  const [comments, setComments] = useState("")
  const [improvements, setImprovements] = useState("")
  const [isSubmitting, setIsSubmitting] = useState(false)
  const { toast } = useToast()

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    
    if (!rating) {
      toast({
        title: "Error",
        description: "Please select a rating",
        variant: "destructive",
      })
      return
    }

    setIsSubmitting(true)

    try {
      const response = await fetch("/api/submit-feedback", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ 
          githubUrl, 
          rating: parseInt(rating), 
          comments, 
          improvements 
        }),
      })

      const data = await response.json()

      if (!response.ok) {
        throw new Error(data.error || "Failed to submit feedback")
      }

      toast({
        title: "Success",
        description: "Thank you for your feedback!",
      })
      
      // Reset form
      setRating("")
      setComments("")
      setImprovements("")
      
      // Notify parent component
      onFeedbackSubmitted()
    } catch (error) {
      toast({
        title: "Error",
        description: error instanceof Error ? error.message : "Failed to submit feedback",
        variant: "destructive",
      })
    } finally {
      setIsSubmitting(false)
    }
  }

  return (
    <Card>
      <CardHeader>
        <CardTitle>Provide Feedback</CardTitle>
        <CardDescription>Help us improve by rating the generated prompt and sharing your thoughts</CardDescription>
      </CardHeader>
      <CardContent>
        <form onSubmit={handleSubmit} className="space-y-6">
          <div className="space-y-2">
            <Label>Rating</Label>
            <RadioGroup value={rating} onValueChange={setRating} className="flex gap-4">
              {[1, 2, 3, 4, 5].map((value) => (
                <div key={value} className="flex items-center space-x-2">
                  <RadioGroupItem value={value.toString()} id={`rating-${value}`} />
                  <Label htmlFor={`rating-${value}`} className="flex items-center gap-1 cursor-pointer">
                    {value} <Star className="h-4 w-4 fill-yellow-400 text-yellow-400" />
                  </Label>
                </div>
              ))}
            </RadioGroup>
          </div>

          <div className="space-y-2">
            <Label htmlFor="comments">Comments</Label>
            <Textarea
              id="comments"
              placeholder="What did you like about the generated prompt?"
              value={comments}
              onChange={(e) => setComments(e.target.value)}
            />
          </div>

          <div className="space-y-2">
            <Label htmlFor="improvements">Suggestions for Improvement</Label>
            <Textarea
              id="improvements"
              placeholder="How could we make the prompt better?"
              value={improvements}
              onChange={(e) => setImprovements(e.target.value)}
            />
          </div>

          <Button type="submit" disabled={isSubmitting} className="w-full">
            {isSubmitting ? "Submitting..." : "Submit Feedback"}
          </Button>
        </form>
      </CardContent>
    </Card>
  )
}