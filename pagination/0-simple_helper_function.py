#!/usr/bin/env python3
"""Module to learn the pagination"""

def index_range(page: int, page_size: int) -> tuple[int, int]:
    """ returns the start and end index based on pagination choice"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)
