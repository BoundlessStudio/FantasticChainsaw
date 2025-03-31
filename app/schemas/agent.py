from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, List

class AgentConfig(BaseModel):
    name: str = Field(default="Assistant", description="The name of the agent")
    instructions: str = Field(default="You are a helpful assistant", description="Instructions for the agent")
    model: Optional[str] = Field(default=None, description="The model to use for the agent")
    tools: Optional[List[Dict[str, Any]]] = Field(default=None, description="Tools available to the agent")
    
    class Config:
        extra = "allow"  # Allow extra fields to support future Agent parameters

class AgentRequest(BaseModel):
    prompt: str = Field(..., description="The prompt to send to the agent")
    agents: List[AgentConfig] = Field(
        default=[AgentConfig()],
        description="List of agent configurations to use in sequence"
    )
    default_agent_index: Optional[int] = Field(
        default=0, 
        description="Index of the default agent to use if not otherwise specified"
    )

class AgentResponse(BaseModel):
    response: str = Field(..., description="The response from the agent")
    input_list: Optional[List[Dict[str, Any]]] = Field(default=None, description="Input list generated from the result")