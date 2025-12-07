from google.adk.agents import Agent
from google.adk.models import Gemini
from ...tools import tracking_tools

finance_agent = Agent(
    name="finance_worker",
    model=Gemini(model_name="gemini-1.5-flash"),
    instruction="Handle questions about supported Currencies.",
    tools=[tracking_tools.get_supported_currencies]
)