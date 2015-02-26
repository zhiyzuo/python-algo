# -*- coding: utf-8 -*-

def linear_search(l, x):
    """Linear search for list/array
       If x is not in l, return False
       Else, return the index
    """
    for i in range(len(l)):
        if l[i] == x:
            return i
    return False
