"""
Example demonstrates how to create an agent that can be used to determine if a customer has won a game of roulette.
The agent uses a simple function to check if the customer's chosen square matches the winning number.
"""

from __future__ import annotations

from pydantic_ai import Agent
from pydantic_ai import RunContext

roulette_agent = Agent(
    "google-gla:gemini-1.5-flash",
    deps_type=int,
    result_type=bool,
    system_prompt=("Use the `roulette_wheel` function to see if the customer has won based on the number they provide."),
)


@roulette_agent.tool
async def roulette_wheel(ctx: RunContext[int], square: int) -> str:
    """Check if the square is a winner"""
    return "winner" if square == ctx.deps else "loser"


# Run the agent
success_number = 18
result = roulette_agent.run_sync("Put my money on square eighteen", deps=success_number)
print(result.data)
# > True

result = roulette_agent.run_sync("I bet five is the winner", deps=success_number)
print(result.data)
# > False
