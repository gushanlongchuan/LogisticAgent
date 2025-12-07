from google.adk.agents import Agent
from google.adk.models import Gemini
from .tracking_team.status_agent import status_agent
from .tracking_team.finance_agent import finance_agent
from .tracking_team.carrier_agent import carrier_agent 

tracking_manager = Agent(
    name="tracking_manager",
    model=Gemini(model_name="gemini-1.5-pro"),
    instruction="""
    You are the Head of Tracking. Delegate tasks:
    1. STATUS/PICKUP -> 'status_worker'
    2. CARRIERS/CHANNELS -> 'carrier_worker' 
    3. CURRENCY -> 'finance_worker'
    """,
    sub_agents=[status_agent, carrier_agent, finance_agent]
)