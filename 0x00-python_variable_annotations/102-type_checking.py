#!/usr/bin/env python3
"""
102. Type Checking
"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zoom in on an array by repeating its elements.

    Args:
        lst (List[int]): The input list of integers to be zoomed in on.
        factor (int, optional): The zoom factor. Default is 2.

    Returns:
    List[int]: A list containing elements of the input list, repeated according to the zoom factor.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
