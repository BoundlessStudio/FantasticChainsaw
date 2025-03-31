from agents import Agent, Runner, RunResult
from typing import Dict, Any, List
from app.schemas.agent import AgentConfig

class AgentService:
    def __init__(self):
        pass
    
    async def run_agent_async(self, 
                             prompt: str, 
                             agents: List[AgentConfig] = None,
                             default_agent_index: int = 0) -> Dict[str, Any]:
        """
        Run an OpenAI agent with a prompt and configuration asynchronously
        
        Args:
            prompt: The user's input prompt
            agents: List of agent configurations
            default_agent_index: Index of the default agent to use
            
        Returns:
            A dictionary containing the agent's response and additional information
        """
        # Use default agent if no agents provided
        if not agents or len(agents) == 0:
            agents = [AgentConfig()]
        
        # Validate default_agent_index
        if default_agent_index < 0 or default_agent_index >= len(agents):
            default_agent_index = 0
        
        # Get the selected agent config
        selected_agent = agents[default_agent_index]
        
        # Convert Pydantic model to dict
        agent_params = selected_agent.model_dump(exclude_unset=True)
        
        # Create the agent with the params
        agent = Agent(**agent_params)
        
        # Run the agent and get the result
        result: RunResult = await Runner.run(agent, prompt)
        
        # Create a structured response
        response = {
            "response": result.final_output,
        }
        
        return response