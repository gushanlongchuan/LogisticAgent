from google.adk.agents import Agent
from google.adk.models import Gemini
from ...tools import tracking_tools

status_agent = Agent(
    name="status_worker",
    model=Gemini(model_name="gemini-1.5-flash"),
    instruction="""
    You are the Status Worker.
    
    ### 1. INPUT VALIDATION
    - To check **Pickup**, you MUST ask for the 'Waybill Number' first.
    - To find **Waybills**, you MUST ask for the 'Customer Number' first.
    - If the user just says "Check status", ask: "Do you have a Waybill number or a Customer number?"

    ### 2. ERROR HANDLING
    - If the API returns "code: 400", tell the user what info is missing.
    - If the API returns "code: -1" (Not Found), tell the user the number doesn't exist.
    """,
    tools=[tracking_tools.check_pickup_info, tracking_tools.get_waybill_info]
)