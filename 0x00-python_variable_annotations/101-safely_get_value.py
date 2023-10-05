#!/usr/bin/env python3
from typing import TypeVar, Mapping, Any, Union


T = TypeVar('T')

def safely_get_value(dct: Mapping[str, Any], key: Any, default: Union[T, None] = None) -> Union[Any, T]:
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
