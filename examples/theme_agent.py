"""Use an AI agent to set the PyVista theme."""

# !pip install nest_asyncio
from __future__ import annotations

import asyncio
from typing import ClassVar

import nest_asyncio
from pydantic_ai import Agent  # Replaced AIModel with Agent
import pyvista as pv

nest_asyncio.apply()


class PyVistaThemeModel:
    """Model to store PyVista theme settings."""

    background_color: str = "white"
    font_size: int = 12
    show_axes: bool = True  # Now handled directly in plotter
    show_grid: bool = True
    grid_opacity: float = 0.1
    lighting: bool = False
    edge_color: str = "black"
    color_map: str = "viridis"

    description_translations: ClassVar[dict[str, str]] = {
        "Set background to black": "background_color=black",
        "Increase font size": "font_size=16",
        "Hide axes": "show_axes=False",
        "Disable grid": "show_grid=False",
        "Enable lighting": "lighting=True",
        "Set edge color to red": "edge_color=red",
        "Use plasma colormap": "color_map=plasma",
    }

    @classmethod
    def add_translation(cls, description: str, setting: str) -> None:
        """Add a translation from a description to a setting."""
        cls.description_translations[description] = setting

    def apply_theme(self) -> None:
        """Apply the theme settings to the global PyVista theme."""
        theme = pv.themes.Theme()
        theme.background = self.background_color
        theme.font.size = self.font_size
        theme.lighting = self.lighting
        theme.edge_color = self.edge_color
        theme.cmap = self.color_map
        pv.global_theme.load_theme(theme)


async def main() -> None:
    """Run the agent to set the PyVista theme."""
    PyVistaThemeModel.add_translation("Set background to blue", "background_color=blue")
    PyVistaThemeModel.add_translation("Decrease font size", "font_size=8")

    prompt = "Set background to blue and decrease font size."
    agent = Agent(model="google-gla:gemini-1.5-flash")
    response = await agent.run(prompt)

    model = PyVistaThemeModel()

    response_text = str(response)  # Extract response as a string
    print(response_text)

    if "background_color=blue" in response_text:
        model.background_color = "blue"
    if "font_size=8" in response_text:
        model.font_size = 8
    if "show_axes=False" in response_text:
        model.show_axes = False

    model.apply_theme()

    plotter = pv.Plotter()
    plotter.show_axes = model.show_axes  # Axes visibility is handled here
    if model.show_grid:
        plotter.show_grid()
    plotter.add_mesh(pv.Sphere(), color="red")
    plotter.show()


if __name__ == "__main__":
    asyncio.run(main())
