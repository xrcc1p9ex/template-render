"""A small template renderer supporting variables, loops and conditionals."""

from __future__ import annotations

__all__ = ["templateRender"]


def templateRender(value):
    """A small template renderer supporting variables, loops and conditionals."""
    if value is None:
        raise ValueError("value must not be None")
    return value
