def _find_median_index(l):
    """ Helper function for quick sort.
        Find out the index of the middle value
    """

    # use the mid-value of the first, last and middle point of the input as pivot
    p = _find_median_index([l[0], l[-1], l[len(l)//2]]) 
    l = l[:p] + l[p+1:] + [l[p]]

    sortedL = sorted(l)
    return l.index(sortedL[len(l)//2])

def _partition(l):
    """ Helper function for quick sort.
        Partition the given input according to the pivot
    """
    i = 0 # the index of the first element which is to the right of the pivot
    j = 0 # the index of the first element which is not rearranged yet
    while j < len(l) - 1:
        if l[j] < l[-1]:
            l[j], l[i] = l[i], l[j]
            i = i + 1
        j = j + 1

    l[-1], l[i] = l[i], l[-1]

    return i

def quick_sort(l):
    """ Quick sort for list/array
        Return a new list that is sorted
    """

    if len(l) < 2:
        return l
    
    i = _partition(l)
    left = quick_sort(l[:i])
    right = quick_sort(l[i+1:])

    return left + [l[i]] + right
