# pyvista-ai

`pyvista-ai` is a Python library that leverages AI to automatically adjust PyVista's `Plotter` settings. By entering a prompt, you can easily apply visually optimal plot configurations.

## Features
- **AI-powered automatic configuration**: Optimizes `pyvista.Plotter` settings based on user prompts
- **Customizable**: Automatically adjusts background color, window size, lighting settings, and more
- **Simple API**: Intuitive operations for adjusting 3D visualizations

## Installation

```bash
pip install pyvista-ai
```

## Usage

### Basic Example
```python
import pyvista as pv
from pyvista_ai import AIPlotter, PlotterConfig

# Initial configuration
config = PlotterConfig()
plotter = AIPlotter(config)

# Modify settings using AI
plotter.configure_from_ai("Enhance realistic shading and display in widescreen mode")

# Add a mesh and display it
mesh = pv.Sphere()
plotter.add_mesh(mesh, color="blue")
plotter.show()
```

## Required Environment Variables
To use `pyvista-ai`, you need to set the OpenAI API key as an environment variable.

```bash
export OPENAI_API_KEY="your-api-key-here"
```

## Future Plans
- **Support for offline AI models**: Integration with `Hugging Face Transformers` for local AI model support
- **GUI Integration**: Compatibility with `PyQt` and `Streamlit`
- **Additional Features**: AI-assisted optimal camera angles and automatic mesh color selection

## License
MIT License

## Contribution
Bug reports and feature suggestions are welcome via GitHub Issues.
Pull requests are also highly encouraged!
