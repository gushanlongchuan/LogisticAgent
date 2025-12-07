import os
from dotenv import load_dotenv

# 1. Load environment variables from the .env file
# This reads the file and injects them into os.environ
load_dotenv()

# Optional: Safety check to warn you if it failed
if not os.getenv("GOOGLE_CLOUD_PROJECT"):
    print("WARNING: GOOGLE_CLOUD_PROJECT not found. Did you create the .env file?")

# 2. Now it is safe to import the agent
from .root_agent import root_agent as agent