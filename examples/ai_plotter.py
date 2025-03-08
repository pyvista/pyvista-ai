r"""
PyVista Plotter with AI-based configuration
-------------------------------------------

This example demonstrates how to create a PyVista Plotter with AI-based configuration.

"""

from __future__ import annotations

import json
import os

import google.generativeai as genai
from pydantic import BaseModel
from pydantic import ValidationError
import pyvista as pv

# Set up Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


class PlotterConfig(BaseModel):
    """Configuration settings for the PyVista Plotter"""

    background_color: str = "white"
    window_size: tuple[int, int] = (800, 600)
    lighting: bool = True


class AIPlotter(pv.Plotter):
    """PyVista Plotter class that allows AI-based configuration"""

    def __init__(self, config: PlotterConfig) -> None:
        """Initialize the Plotter with the given configuration"""
        super().__init__()
        self.background_color = config.background_color
        self.window_size = config.window_size
        self.lighting = config.lighting

    def configure_from_ai(self, prompt: str) -> None:
        """Interpret the prompt using an AI model and modify the settings accordingly"""
        model = genai.GenerativeModel("gemini-1.5-pro-latest")

        response = model.generate_content(
            [
                "You are an AI assistant that translates user input into PyVista Plotter settings.",
                "Adjust the PyVista plot settings based on this prompt and return a JSON contents with keys:",
                f"background_color, window_size, and lighting: {prompt}",
            ]
        )

        ai_suggestion = response.text
        print("AI Suggestion:", ai_suggestion)

        # Apply the parsed result (attempting to convert to JSON format)
        try:
            config_dict = json.loads(ai_suggestion)
            print(f"config_dict:{config_dict}")
            config = PlotterConfig(**config_dict)
            self.background_color = config.background_color
            self.window_size = config.window_size
            self.lighting = config.lighting
        except (ValidationError, json.JSONDecodeError) as e:
            print(f"Invalid AI suggestion: {e}")


# Initialize default settings
config = PlotterConfig()

# Create an instance of AIPlotter
plotter = AIPlotter(config)

# Modify settings based on AI-generated prompt
plotter.configure_from_ai("Enhance realistic shading and display in widescreen mode")

# Add a demo mesh
mesh = pv.Sphere()
plotter.add_mesh(mesh, color="blue")
plotter.show()
