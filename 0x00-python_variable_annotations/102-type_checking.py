#!/usr/bin/env python3

"""
Use mypy to validate the following piece of code and apply
any necessary changes
"""

from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Correctly type-annotated function
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(tuple(array))

zoom_3x = zoom_array(tuple(array), 3)
