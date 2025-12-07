from google.adk.agents import Agent
from google.adk.models import Gemini
from .specialists.tracking_manager import tracking_manager
from .specialists.order_specialist import order_specialist
from .specialists.shipping_specialist import shipping_specialist
from .callbacks import before_model_callback, after_model_callback
from .config import retry_config

root_agent = Agent(
    name="logistics_root",
    model=Gemini(model_name="gemini-1.5-pro", retry=retry_config),
    instruction="""
    You are the Logistics System. Route to:
    1. TRACKING/STATUS/INFO -> 'tracking_manager'
    2. ORDERS/LABELS/DELETE -> 'order_specialist'
    3. SHIPPING/PRICES -> 'shipping_specialist'
    """,
    sub_agents=[tracking_manager, order_specialist, shipping_specialist],
    before_model_callback=[before_model_callback],
    after_model_callback=[after_model_callback]
)