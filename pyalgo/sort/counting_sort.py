# -*- coding: utf-8 -*-

def counting_sort(l, keyRange=None):
    """ Counting sort for list/array (discrete&finite sorting keys)
        Return a new list that is sorted
    """

    if keyRange == None:
        keyRange = max(l) + 1
    countList = [0]*keyRange
    accumulateList = [0]*keyRange

    for key in l:
        countList[key] = countList[key] + 1
    for i in range(1, keyRange):
        accumulateList[i] = countList[i-1] + accumulateList[i-1]

    sorted_l = [None]*len(l)
    for j in range(len(l)):
        key = l[j]
        index = accumulateList[key]
        sorted_l[index] = key
        accumulateList[key] = accumulateList[key] + 1

    return sorted_l

