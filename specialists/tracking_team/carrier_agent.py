from google.adk.agents import Agent
from google.adk.models import Gemini
from ...tools import tracking_tools
from ...config import retry_config

carrier_agent = Agent(
    name="carrier_worker", 
    model=Gemini(model_name="gemini-1.5-flash", retry=retry_config),
    instruction="""
    You are the Carrier & Network Worker.
    - Your job is to provide information about available shipping channels (Carriers) and services.
    - Use 'get_channel_info' to list supported logistics providers.
    """,
    tools=[tracking_tools.get_channel_info]
)