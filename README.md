# OpenAI Agents API

A FastAPI-based backend for interacting with the OpenAI Agents SDK.

## Features

- RESTful API for running AI agents
- Interactive web demo
- Customizable agent instructions
- Structured response handling

## Project Structure

```
app/
├── api/             # API endpoints
│   └── endpoints/  # API route handlers
├── core/           # Core configuration
├── db/             # Database models and session
├── models/         # Pydantic models
├── schemas/        # API schemas
├── services/       # Business logic
├── static/         # Static files
└── templates/      # HTML templates
```

## Setup

1. Clone this repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file with:
   ```
   OPENAI_API_KEY=your_api_key_here
   SECRET_KEY=your_secret_key_here
   ```

## Running the Application

```bash
python main.py
```

Then visit:
- API: http://localhost:8000/api/v1
- API Documentation: http://localhost:8000/docs
- Web Demo: http://localhost:8000

## API Endpoints

- `POST /api/v1/agents/run` - Run an agent with a prompt

## Development

### Testing

```bash
pyttest tests/
```

### Building Docker Image

```bash
docker build -t openai-agents-api .
```
