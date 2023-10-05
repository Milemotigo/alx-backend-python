#!/usr/bin/env python3
from typing import TypeVar, Dict, Optional

K = TypeVar('K')      # Key type
V = TypeVar('V')      # Value type

def safely_get_value(dct: Dict[K, V], key: K, default: Optional[V] = None) -> V:
    """
    Safely get a value from a dictionary using a specified key.

    Args:
        dct (Dict[K, V]): The dictionary to retrieve the value from.
        key (K): The key to look up in the dictionary.
        default (Optional[V], optional): The default value to return if the key is not found. Defaults to None.

    Returns:
        V: The value associated with the key in the dictionary, or the default value if the key is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default