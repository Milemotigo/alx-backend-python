#!/usr/bin/env python3
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create and return a function that multiplies a float by the specified multiplier.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: A function that takes a float and returns the result of multiplying it by the multiplier.
    """
    def make_multiplier(a: float) -> float:
        return a * multiplier

    return make_multiplier
