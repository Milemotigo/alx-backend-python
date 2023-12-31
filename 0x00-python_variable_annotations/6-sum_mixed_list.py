#!/usr/bin/env python3
'''Write a type-annotated function sum_mixed_list which takes a list mxd_lst of integers
and floats and returns their sum as a float.'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a list containing a mixture of ints and floats.

    Args:
        mxd_lst (List[Union[int, float]]): The list containing a mixture of ints and floats.

    Returns:
        float: The sum of the elements in the input list.
    """
    return sum(mxd_lst)