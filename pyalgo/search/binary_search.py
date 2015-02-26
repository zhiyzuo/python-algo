def binary_search(l, x, recursive=False):
    """Binary search for list/array
       Require the input to be sorted
       If x is not in l, return False
       Else, return the index
    """

    if recursive:
        return binary_search_recurrsive(l, x, 0, len(l)-1)

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

def binary_search_recurrsive(l, x, start, end):
    """Recurrsive binary search for list/array"""

    if start > end:
        return False
    mid = (start + end) //2
    if x == l[mid]:
        return mid
    elif x > l[mid]:
        return binary_search_recurrsive(l, x, mid+1, end)    
    else:
        return binary_search_recurrsive(l, x, start, mid-1)    
