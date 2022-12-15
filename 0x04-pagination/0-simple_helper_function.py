#!/usr/bin/env python3
'''
This file contains the basic index range function.
'''


def index_range(page, page_size):
    '''
    Returns a tuple of the size of start of the index and end of the inndex
    pages are 1-indexed.
    '''

    end_of_index = page * page_size
    start_of_index = end_of_index - page_size

    return (start_of_index, end_of_index)
