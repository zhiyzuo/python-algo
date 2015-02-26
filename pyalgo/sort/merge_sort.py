# -*- coding: utf-8 -*-

def _merge(left, right):
    ''' Helper function for merge sort
        Merge two lists according to the value of elements
        Both inputs should be sorted
    ''' 

    i = 0
    j = 0
    mergedList = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            mergedList.append(left[i])
            i = i + 1
        else:
            mergedList.append(right[j])
            j = j + 1

    if i == len(left):
        mergedList.extend(right[j:])
    else:
        mergedList.extend(left[i:])

    return mergedList

def merge_sort(l):
    """ Selection sort for list/array
        Return a new list that is sorted
    """

    if len(l) < 2:
        return l

    mid = len(l)//2
    left = l[:mid]
    right = l[mid:]
    
    leftSort = merge_sort(left)
    rightSort = merge_sort(right)
    mergedList = _merge(leftSort, rightSort)

    return mergedList
