"""
Demonstrates a custom Pydantic AI agent for managing PyVista Plotter configurations.
The agent can configure the background color and window size of the PyVista Plotter.
"""

from __future__ import annotations

import asyncio
from dataclasses import dataclass

from pydantic import BaseModel
from pydantic import Field
from pydantic_ai import Agent
from pydantic_ai import RunContext
import pyvista as pv


@dataclass
class PlotterDependencies:
    """Dependency container for PlotterAgent"""

    background_color: str = "white"  # Default background color
    window_size: tuple[int, int] = (800, 600)  # Default window size


class PlotterResult(BaseModel):
    """Model for the agent's response"""

    message: str = Field(description="Response message from the Plotter Agent")
    success: bool = Field(description="Indicates if the plotter operation was successful")


class PlotterAgent(Agent[PlotterDependencies, PlotterResult]):
    """Custom agent for handling PyVista Plotter configurations"""

    def __init__(self, model: str = "gemini:pro") -> None:
        """Initialize the PlotterAgent with a default system prompt"""
        super().__init__(
            model,
            deps_type=PlotterDependencies,
            result_type=PlotterResult,
            system_prompt=self.default_system_prompt(),
        )
        self.system_prompt(self.describe_plotter)
        self.tool(self.create_plotter)
        self.plotter = pv.Plotter()

    @staticmethod
    def default_system_prompt() -> str:
        """Return the default system prompt for the agent"""
        return "You are an AI agent managing PyVista Plotter configurations for scientific visualization."

    @staticmethod
    async def describe_plotter(ctx: RunContext[PlotterDependencies]) -> str:
        """Describe the plotter configuration in the system prompt"""
        return f"The plotter has a background color of {ctx.deps.background_color} and a window size of {ctx.deps.window_size}."

    @staticmethod
    async def create_plotter(ctx: RunContext[PlotterDependencies]) -> PlotterResult:
        """Create a PyVista Plotter instance with specified configurations"""
        try:
            plotter = pv.Plotter()
            plotter.background_color = ctx.deps.background_color
            plotter.window_size = ctx.deps.window_size
            message = "Plotter configured successfully."
            success = True
        except Exception as e:  # noqa: BLE001
            message = f"Failed to configure Plotter: {e!s}"
            success = False

        return PlotterResult(message=message, success=success)

    @property
    def plotter(self) -> pv.Plotter:
        """Get the PyVista Plotter instance"""
        return self._plotter

    @plotter.setter
    def plotter(self, value: pv.Plotter) -> None:
        """Set the PyVista Plotter instance"""
        self._plotter = value


# Create an instance of PlotterAgent
plotter_agent = PlotterAgent(model="google-gla:gemini-1.5-flash")


async def main() -> None:
    """Test the PlotterAgent with different configurations"""
    deps = PlotterDependencies(background_color="black", window_size=(1024, 768))
    result = await plotter_agent.run("Configure PyVista Plotter", deps=deps)
    print(result.data)
    plotter_agent.plotter.show()


# Run the main function if needed
asyncio.run(main())  # Uncomment this line to run in an async environment
