#!/usr/bin/env python3
"""
 101. More involved type annotations
"""
from typing import TypeVar, Union, Any, Mapping

T = TypeVar('T')
V = Union[Any, T]
Df = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Df = None) -> V:
    """Safely get a value from a dictionary using a specified key. """
    if key in dct:
        return dct[key]
    else:
        return default
