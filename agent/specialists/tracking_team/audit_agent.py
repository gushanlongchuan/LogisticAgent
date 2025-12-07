from google.adk.agents import Agent
from google.adk.models import Gemini

# Import the workers
from .status_agent import status_agent
from .finance_agent import finance_agent
from .carrier_agent import carrier_agent

# Define the Model (We need a smart model to orchestrate parallel calls)
model = Gemini(model="gemini-1.5-pro")

audit_agent = Agent(
    name="full_audit_team",
    model=model,
    instruction="""
    You are the Audit Team Leader.
    
    Your goal is to provide a complete view of the shipment by gathering data from all your sub-workers SIMULTANEOUSLY.
    
    1. Call 'status_worker' to get the pickup/location status.
    2. Call 'carrier_worker' to get the channel info.
    3. Call 'finance_worker' to get the currency info.
    
    CRITICAL: You must call all three tools in parallel (at the same time) to be efficient. 
    Once you have all results, compile them into a single summary report.
    """,
    # We pass the other AGENTS as TOOLS. 
    # The ADK allows Agents to be tools for other Agents.
    tools=[status_agent, carrier_agent, finance_agent]
)