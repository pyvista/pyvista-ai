"""
Demonstrates how to create a custom agent for handling banking support queries.
The agent uses a simulated customer database to fetch customer details and provide support.
The agent also assesses the risk level of the query and decides whether to block the customer's card.
"""

from __future__ import annotations

import asyncio
from dataclasses import dataclass

from pydantic import BaseModel
from pydantic import Field
from pydantic_ai import Agent
from pydantic_ai import RunContext

# Simulated customer database
CUSTOMER_DATABASE = {
    123: {"name": "John Doe", "balance": 123.45},
    456: {"name": "Alice Smith", "balance": 789.00},
}


@dataclass
class SupportDependencies:
    """Dependency container for SupportAgent"""

    customer_id: int  # Customer ID to identify the user


class SupportResult(BaseModel):
    """Model for the agent's response"""

    support_advice: str = Field(description="Advice returned to the customer")
    block_card: bool = Field(description="Whether to block the customer's card")
    risk: int = Field(description="Risk level of query", ge=0, le=10)


class SupportAgent(Agent[SupportDependencies, SupportResult]):
    """Custom agent for handling banking support queries"""

    def __init__(self, model: str = "gemini:pro") -> None:
        """Initialize the SupportAgent with a default system prompt"""
        super().__init__(
            model,
            deps_type=SupportDependencies,
            result_type=SupportResult,
            system_prompt=self.default_system_prompt(),
        )
        self.system_prompt(self.add_customer_name)

    @staticmethod
    def default_system_prompt() -> str:
        """Return the default system prompt for the agent"""
        return "You are a support agent in our bank, providing assistance to customers and assessing the risk level of their queries."

    @staticmethod
    async def add_customer_name(ctx: RunContext[SupportDependencies]) -> str:
        """Fetch customer name from the simulated database and add it to the prompt"""
        customer = CUSTOMER_DATABASE.get(ctx.deps.customer_id, {"name": "Unknown"})
        return f"The customer's name is {customer['name']!r}"

    @staticmethod
    @Agent.tool
    async def customer_balance(ctx: RunContext[SupportDependencies]) -> float:
        """Return the customer's current account balance"""
        customer = CUSTOMER_DATABASE.get(ctx.deps.customer_id, {"balance": 0.0})
        return customer["balance"]


# Create an instance of SupportAgent using Gemini
support_agent = SupportAgent(model="google-gla:gemini-1.5-flash")


async def main() -> None:
    """Test the SupportAgent with different queries"""
    deps = SupportDependencies(customer_id=123)
    result = await support_agent.run("What is my balance?", deps=deps)
    print(result.data)
    """
    support_advice='Hello John Doe, your current account balance is $123.45.' block_card=False risk=1
    """

    result = await support_agent.run("I just lost my card!", deps=deps)
    print(result.data)
    """
    support_advice="I'm sorry to hear that, John Doe.
    We are temporarily blocking your card to prevent unauthorized transactions." block_card=True risk=8
    """


# Run the main function if needed
asyncio.run(main())  # Uncomment this line to run in an async environment
