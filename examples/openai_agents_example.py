"""
Example: Using Asqav with OpenAI Agents SDK

This example shows how to sign and audit agent actions when using
the OpenAI Agents SDK. All actions are cryptographically signed with
ML-DSA for non-repudiation.

Requirements:
    pip install asqav-sdk openai-agents
"""

import asqav
from agents import Agent, Runner

# Initialize asqav
asqav.init()

# Create an asqav agent for audit trail
audit_agent = asqav.Agent.create("openai-agents-example")

# Define your OpenAI agent
research_agent = Agent(
    name="Research Assistant",
    instructions="Help users research topics accurately.",
)


@asqav.secure
async def run_research(query: str) -> str:
    """Run research with cryptographic audit trail."""
    result = await Runner.run(research_agent, query)
    return result.final_output


# Usage:
# import asyncio
# response = asyncio.run(run_research("What is quantum computing?"))
# print(response)
