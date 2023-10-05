#!/usr/bin/env python3
from typing import List, Iterable, Sequence, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of each element in the input list and return a list of tuples.
    
    Args:
        lst (Iterable[Sequence]): The input list of sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple contains a sequence from the input list and its corresponding length.
    """
    return [(i, len(i)) for i in lst]

