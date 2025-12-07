from google.adk.agents import Agent
from google.adk.models import Gemini
from .specialists.tracking_manager import tracking_manager
from .specialists.order_specialist import order_specialist
from .specialists.shipping_specialist import shipping_specialist

root_agent = Agent(
    name="logistics_root",
    model=Gemini(model_name="gemini-1.5-pro"),
    instruction="""
    You are the Logistics System. Route to:
    1. TRACKING/STATUS/INFO -> 'tracking_manager'
    2. ORDERS/LABELS/DELETE -> 'order_specialist'
    3. SHIPPING/PRICES -> 'shipping_specialist'
    """,
    tools=[tracking_manager, order_specialist, shipping_specialist]
)