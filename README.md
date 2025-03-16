# pyvista-ai
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-3-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

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
import asyncio
import pyvista as pv
from pyvista_ai import PlotterAgent

agent = PlotterAgent(model="gemini:pro")

async def main() -> None:
    plotter = await agent.run("Enhance realistic shading and display in widescreen mode")
    return plotter.show()

asyncio.run(main())
```

## Required Environment Variables
To use `pyvista-ai`, you need to set the GEMINI API key as an environment variable.

```bash
export GEMINI_API_KEY="your-api-key-here"
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

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/tkoyama010"><img src="https://avatars.githubusercontent.com/u/7513610?v=4?s=100" width="100px;" alt="Tetsuo Koyama"/><br /><sub><b>Tetsuo Koyama</b></sub></a><br /><a href="https://github.com/pyvista/pyvista-ai/commits?author=tkoyama010" title="Documentation">📖</a> <a href="#maintenance-tkoyama010" title="Maintenance">🚧</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://allcontributors.org"><img src="https://avatars.githubusercontent.com/u/46410174?v=4?s=100" width="100px;" alt="All Contributors"/><br /><sub><b>All Contributors</b></sub></a><br /><a href="https://github.com/pyvista/pyvista-ai/commits?author=all-contributors" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/apps/pre-commit-ci"><img src="https://avatars.githubusercontent.com/in/68672?v=4?s=100" width="100px;" alt="pre-commit-ci[bot]"/><br /><sub><b>pre-commit-ci[bot]</b></sub></a><br /><a href="#maintenance-pre-commit-ci[bot]" title="Maintenance">🚧</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
