def findMinIndex(l):
    ''' Helper function for selection sort
        To find out the index of the minimun value in the given input
    '''
    minIndex = 0
    for i in range(1, len(l)):
        if l[i] < l[minIndex]:
            minIndex = i
    return minIndex

def selectionSort(l):
    """ Selection sort for list/array
        Modify the original input to sorted
    """
    for i in range(len(l)):
        minInSubArray = findMinIndex(l[i:])
        l[i], l[minInSubArray+i] = l[minInSubArray+i], l[i]

def insertionSort(l):
    """ Insertion sort for list/array
        Modify the original input to sorted
    """
    for i in range(1, len(l)):
        j = i - 1
        while j >= 0:
            if l[i] < l[j]:
                l[i], l[j] = l[j], l[i]
                i = j
            j = j - 1


def merge(left, right):
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

def mergeSort(l):
    """ Selection sort for list/array
        Return a new list that is sorted
    """

    if len(l) < 2:
        return l

    mid = len(l)//2
    left = l[:mid]
    right = l[mid:]
    
    leftSort = mergeSort(left)
    rightSort = mergeSort(right)
    mergedList = merge(leftSort, rightSort)

    return mergedList

def findMedianIndex(l):
    """ Helper function for quick sort.
        Find out the index of the middle value
    """

    # use the mid-value of the first, last and middle point of the input as pivot
    p = findMedianIndex([l[0], l[-1], l[len(l)//2]]) 
    l = l[:p] + l[p+1:] + [l[p]]

    sortedL = sorted(l)
    return l.index(sortedL[len(l)//2])

def partition(l):
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

def quickSort(l):
    """ Quick sort for list/array
        Return a new list that is sorted
    """

    if len(l) < 2:
        return l
    
    i = partition(l)
    left = quickSort(l[:i])
    right = quickSort(l[i+1:])

    return left + [l[i]] + right

l = [9,7,5,11,12,2,14,3,10,6]
#selectionSort(l)
#insertionSort(l)
#sortedL = mergeSort(l)
sortedL = quickSort(l)
print sortedL
#print l
