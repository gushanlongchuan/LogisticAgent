from google.api_core.retry import Retry

# Global Retry Configuration
# Used by all Gemini models to handle network blips or rate limits
retry_config = Retry(
    initial=1.0,      # Wait 1 second before first retry
    maximum=10.0,     # Max wait time between retries
    multiplier=2.0,   # Double the wait time each failure
    deadline=60.0     # Stop trying after 60 seconds total
)