def linearSearch(l, x):
    """Linear search for list/array
       If x is not in l, return False
       Else, return the index
    """
    for i in range(len(l)):
        if l[i] == x:
            return i
    return False

def binarySearch(l, x, recursive=False):
    """Binary search for list/array
       Require the input to be sorted
       If x is not in l, return False
       Else, return the index
    """

    if recursive:
        binarySearchRecurrsive(l, x)

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

def binarySearchRecurrsive(l, x):
    """Recurrsive binary search for list/array"""

    start = 0
    end = len(l) - 1
    mid = (start + end) //2
    if x == l[mid]:
        return mid
    elif x > l[mid]:
        binarySearchRecurrsive(l[mid+1:end+1], x)    
    else:
        binarySearchRecurrsive(l[start:mid], x)    
    return False
