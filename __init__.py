import os
from dotenv import load_dotenv

# 1. Load environment variables from the .env file
load_dotenv()

if not os.getenv("GOOGLE_CLOUD_PROJECT"):
    print("WARNING: GOOGLE_CLOUD_PROJECT not found. Did you create the .env file?")

from .agent import root_agent as agent