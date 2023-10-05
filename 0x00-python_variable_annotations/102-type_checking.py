#!/usr/bin/env python3

from typing import List, Tuple

def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """
        Zoom in on an array by repeating its elements.

        Args:
            lst (List[int]): The input list of integers to be zoomed in on.
            factor (int, optional): The zoom factor. Default is 2.

        Returns:
            List[int]: A list containing elements of the input list, repeated according to the zoom factor.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in

array = (12, 72, 91)  # changed from list to tuple

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)  # changed from 3.0 to 3
