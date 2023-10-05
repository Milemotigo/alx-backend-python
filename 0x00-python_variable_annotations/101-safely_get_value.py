#!/usr/bin/env python3
"""
11. Safely get a value from a dictionary using a specified key.
"""
from typing import TypeVar, Mapping, Any, Union


T = TypeVar('T')

def safely_get_value(dct: Mapping[str, Any], key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """Safely get a value from a dictionary using a specified key."""
    if key in dct:
        return dct[key]
    else:
        return default
