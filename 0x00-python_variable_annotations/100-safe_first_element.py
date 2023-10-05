#!/usr/bin/env python3
from typing import Sequence, Union, Any

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Safely retrieve the first element of a sequence.

    Args:
        lst (Sequence[Any]): A sequence (e.g., list, tuple) of any type.

    Returns:
        Union[Any, None]: The first element of the sequence if it is not empty.
                          None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
    
print(safe_first_element.__annotations__)