# GitHub MVP Generator Frontend

A Next.js frontend application for the GitHub MVP Generator that integrates with the Python backend API.

## Features

- Generate MVP prompts from GitHub repository URLs
- Provide feedback on generated prompts
- View system statistics and performance metrics
- Copy generated prompts to clipboard
- Responsive design with Tailwind CSS

## Getting Started

### Prerequisites

- Node.js 18+
- npm (comes with Node.js)

### Installation

1. Install dependencies:
```bash
npm install
```

2. Create a `.env.local` file with the backend API URL:
```bash
NEXT_PUBLIC_BACKEND_API_URL=http://localhost:8000
```

### Development

Start the development server:
```bash
npm run dev
```

The frontend will be available at http://localhost:3000

### Building for Production

```bash
npm run build
npm start
```

## Project Structure

```
app/                    # Next.js app router pages
components/             # React components
components/ui/          # Shadcn UI components
hooks/                  # Custom React hooks
lib/                    # Utility functions
public/                 # Static assets
styles/                 # Global styles
```

## API Integration

The frontend communicates with the Python backend through these endpoints:

- `POST /api/generate-prompt` - Generate MVP prompt (proxies to backend)
- `POST /api/submit-feedback` - Submit feedback (proxies to backend)
- `GET /api/stats` - Get system statistics (called directly from frontend)

## Dependencies

- Next.js 14
- React 18
- Tailwind CSS
- Shadcn UI components
- Lucide React icons
```