#!/usr/bin/env python3
"""Augment the following code with the correct duck-typed annotations:
"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Safely retrieve the first element of a sequence."""
    if lst:
        return lst[0]
    else:
        return None