#!/usr/bin/env python3

"""
Given the parameters and the return values, add type annotations
to the function
"""

from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None)\
      -> Union[Any, T]:
    """
    Typed-annotated function
    """
    if key in dct:
        return dct[key]
    else:
        return default
