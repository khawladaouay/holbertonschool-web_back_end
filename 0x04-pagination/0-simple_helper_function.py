#!/usr/bin/env python3
"""
index_range 
"""


def index_range(page, page_size):
    """
    The function should return a tuple of size two containing:
    a start index and an end index corresponding to
    the range of indexes to return in a list
    for those particular pagination parameters.
    """
    previous = (page - 1) * page_size
    return (previous, previous + page_size)
