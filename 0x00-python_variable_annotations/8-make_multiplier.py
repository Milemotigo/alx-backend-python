#!/usr/bin/env python3
'''Write a type-annotated function make_multiplier that takes a float multiplier as argument'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
        Create and return a function that multiplies a float by the specified multiplier.
    """
    def make_multiplier(a: float) -> float:
        return a * multiplier

    return make_multiplier
