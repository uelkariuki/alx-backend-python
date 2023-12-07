#!/usr/bin/env python3

"""
type-annotated function to_kv that takes a string k and an int OR float v as
arguments and returns a tuple
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Type-annotated function to_kv that returns a tuple"""
    return k, (v*v)
