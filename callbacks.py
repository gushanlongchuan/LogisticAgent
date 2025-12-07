import logging
import time
from google.adk.agents.callback_context import CallbackContext
from google.adk.models import LlmRequest, LlmResponse
from google.adk.tools.base_tool import BaseTool
from google.adk.tools.tool_context import ToolContext
from typing import Optional
from typing import Dict, Any

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(message)s')
logger = logging.getLogger("Logistic_Agent_Monitor")

"""Centralized hooks for monitoring Agent and Tool activity."""
# 2. before_model_callback: print user input + record start time
def before_model_callback(
    callback_context: CallbackContext,
    llm_request: LlmRequest,
) -> Optional[LlmResponse]:
    """
    Runs right before calling Gemini.
    - Prints the user input text.
    - Stores the current timestamp in callback_context.state for timing.
    """

    # Grab the last user message from llm_request.contents
    user_text = None
    for content in reversed(llm_request.contents):
        if content.role == "user":
            parts_text = []
            for part in content.parts:
                text_val = getattr(part, "text", None)
                if text_val:
                    parts_text.append(text_val)
            user_text = " ".join(parts_text) if parts_text else ""
            break

    logger.info(f"[before_model_callback] Agent: {callback_context.agent_name}")
    if user_text is not None:
        logger.info(f"[before_model_callback] User input: {user_text!r}")
    else:
        logger.info("[before_model_callback] No user message found in llm_request.contents")

    # Record start time in the callback context state
    callback_context.state["model_start_time"] = time.time()

    return None


# 3. after_model_callback: compute & print execution time
def after_model_callback(
    callback_context: CallbackContext,
    llm_response: LlmResponse,
) -> Optional[LlmResponse]:
    """
    Runs right after the model responds.
    - Computes elapsed time using the timestamp stored earlier.
    - Prints the execution time.
    """

    start_time = callback_context.state.get("model_start_time")
    if start_time is not None:
        elapsed = time.time() - start_time
        logger.info(
            f"[after_model_callback] Agent: {callback_context.agent_name} "
            f"model execution time: {elapsed:.3f} seconds"
        )
    else:
        logger.info(
            "[after_model_callback] 'model_start_time' missing in state "
            "(before_model_callback might not have run?)"
        )

    return None

def before_tool_callback(
    tool: BaseTool,
    args: Dict[str, Any],
    tool_context: ToolContext,
) -> Optional[Dict]:
    """
    Runs just before a tool is executed.
    - Prints which tool is called and its args.
    - Stores a start time for tool execution.
    """

    agent_name = tool_context.agent_name
    tool_name = tool.name

    logger.info(f"[before_tool_callback] Agent: {agent_name}, tool: {tool_name}")
    logger.info(f"[before_tool_callback] Args: {args}")

    # Record per-tool start time;
    tool_context.state["tool_start_time"] = time.time()

    # Return None -> allow the tool to run normally
    return None


def after_tool_callback(
    tool: BaseTool,
    args: Dict[str, Any],
    tool_context: ToolContext,
    tool_response: Dict,
) -> Optional[Dict]:
    """
    Runs just after a tool finishes successfully.
    - Prints the tool result.
    - Prints tool execution time.
    """

    agent_name = tool_context.agent_name
    tool_name = tool.name
    logger.info(f"[after_tool_callback] Agent: {agent_name}, tool: {tool_name}")
    logger.info(f"[after_tool_callback] Tool response: {tool_response}")

    start_time = tool_context.state.get("tool_start_time")
    if start_time is not None:
        elapsed = time.time() - start_time
        logger.info(
            f"[after_tool_callback] Tool '{tool_name}' execution time: "
            f"{elapsed:.3f} seconds"
        )
    else:
        logger.info(
            "[after_tool_callback] 'tool_start_time' missing in state "
            "(before_tool_callback might not have run?)"
        )

    return None