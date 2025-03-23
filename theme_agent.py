"""Demonstrates how to use the theme agent to determine if the user wants to show edges or not."""

from __future__ import annotations

from pydantic_ai import Agent

theme_agent = Agent(
    model="google-gla:gemini-1.5-flash",
    result_type=bool,
    system_prompt="Answer true if user want to show edges and answer false if user do not want to show edges.",
)
result = theme_agent.run_sync("I want to show edges.")
print(result.data)  # noqa: T201
result = theme_agent.run_sync("I do not want to show edges.")
print(result.data)  # noqa: T201
