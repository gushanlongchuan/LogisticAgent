from google.adk.agents import Agent
from google.adk.models import Gemini
from ..tools import shipping_tools
from ..config import retry_config

shipping_specialist = Agent(
    name="shipping_specialist",
    model=Gemini(model_name="gemini-1.5-flash", retry=retry_config),
    instruction="""
    You are the Shipping Specialist.

    ### 1. INPUT VALIDATION
    - **Before** checking price or creating shipments, you MUST have: 'Origin', 'Destination', and 'Weight'.
    - If missing, ask the user specifically for the missing piece.
      - Example: "I can check the price, but where are you shipping to?" or "How heavy is the package?"

    ### 2. ERROR HANDLING
    - If the tool returns a 400 error (Missing Info), apologize and ask the user for that info again.
    """,
    tools=[shipping_tools.check_shipping_price, shipping_tools.create_shipment]
)