"""A pydantic model for a pyvista theme."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel
import pyvista as pv


class PyVistaTheme(BaseModel):
    """A pydantic model for a pyvista theme."""

    config: dict[str, Any]

    @classmethod
    def from_theme(cls, theme: pv.themes.DocumentTheme) -> PyVistaTheme:
        """Create a PyVistaTheme instance from a pyvista theme."""
        return cls(config=theme.__dict__)

    def to_theme(self) -> pv.themes.DocumentTheme:
        """Create a pyvista theme from a PyVistaTheme instance."""
        theme = pv.themes.DocumentTheme()
        for k, v in self.config.items():
            setattr(theme, k, v)
        return theme


if __name__ == "__main__":
    original_theme = pv.global_theme

    pydantic_theme = PyVistaTheme.from_theme(original_theme)

    restored_theme = pydantic_theme.to_theme()
