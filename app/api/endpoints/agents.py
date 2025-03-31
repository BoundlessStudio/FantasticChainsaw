from fastapi import APIRouter, HTTPException, Depends, BackgroundTasks
from app.schemas.agent import AgentRequest, AgentResponse, AgentConfig
from app.services.agent_service import AgentService
from app.core.config import settings
from typing import Any, Dict, List

router = APIRouter()

@router.post("/run", response_model=AgentResponse)
async def run_agent(request: AgentRequest) -> Any:
    """Run an agent with a specific prompt"""
    if not settings.OPENAI_API_KEY:
        raise HTTPException(
            status_code=500,
            detail="OpenAI API key not configured"
        )
    
    try:
        agent_service = AgentService()
        
        # Use the new multi-agent method
        result = await agent_service.run_agent_async(
            prompt=request.prompt, 
            agents=request.agents,
            default_agent_index=request.default_agent_index
        )
        
        # Return structured response
        return result
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error running agent: {str(e)}"
        )