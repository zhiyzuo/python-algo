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

