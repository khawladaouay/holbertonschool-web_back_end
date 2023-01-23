#!/usr/bin/env python3
"""task7"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """return tuple"""
    return (k, float(v**2))
