# -*- coding: utf-8 -*-

def _find_min_index(l):
    ''' Helper function for selection sort
        To find out the index of the minimun value in the given input
    '''
    minIndex = 0
    for i in range(1, len(l)):
        if l[i] < l[minIndex]:
            minIndex = i
    return minIndex

def selection_sort(l):
    """ Selection sort for list/array
        Modify the original input to sorted
    """
    for i in range(len(l)):
        minInSubArray = _find_min_index(l[i:])
        l[i], l[minInSubArray+i] = l[minInSubArray+i], l[i]
