# -*- coding: utf-8 -*-

def binary_search(l, x, recursive=False):
    """Binary search for list/array
       Require the input to be sorted
       If x is not in l, return False
       Else, return the index
    """

    if recursive:
        binary_search_recurrsive(l, x)

    else:
        start = 0
        end = len(l) - 1
        while start <= end:
            mid = (start + end) //2
            if x == l[mid]:
                return mid
            elif x > l[mid]:
                start = mid+1
            else:
                end = mid-1
        return False

def binary_search_recurrsive(l, x):
    """Recurrsive binary search for list/array"""

    start = 0
    end = len(l) - 1
    mid = (start + end) //2
    if x == l[mid]:
        return mid
    elif x > l[mid]:
        binary_search_recurrsive(l[mid+1:end+1], x)    
    else:
        binary_search_recurrsive(l[start:mid], x)    
    return False
