# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import time
import sys
sys.path.append("..")
from pyalgo.sort.insertion_sort import *
from pyalgo.sort.merge_sort import *
from pyalgo.sort.selection_sort import *
from pyalgo.sort.sort import *

if __name__ == "__main__":
    n = range(1, 1001, 20)
    loopIndex = range(0, 10)
    
    # insertion sort
    timeArray_insertion = []
    for i in n:
        testArray = range(i)
        np.random.shuffle(testArray)
        time0_insertion = time.clock()
        for j in loopIndex:
            insertion_sort(testArray)
        time1_insertion = time.clock()
        timeArray_insertion.append((time1_insertion - time0_insertion)/len(loopIndex))

    # merge sort
    timeArray_merge = []
    for i in n:
        testArray = range(i)
        np.random.shuffle(testArray)
        time0_merge = time.clock()
        for k in loopIndex:
            merge_sort(testArray)
        time1_merge = time.clock()
        timeArray_merge.append((time1_merge - time0_merge)/len(loopIndex))

    # selection sort
    timeArray_selection = []
    for i in n:
        testArray = range(i)
        np.random.shuffle(testArray)        
        time0_selection = time.clock()
        for l in loopIndex:
            selection_sort(testArray)
        time1_selection = time.clock()
        timeArray_selection.append((time1_selection - time0_selection)/len(loopIndex))

    # quick sort
    timeArray_quick = []
    for i in n:
        testArray = range(i)
        np.random.shuffle(testArray)
        time0_quick = time.clock()
        for m in loopIndex:
            quick_sort(testArray)
        time1_quick = time.clock()
        timeArray_quick.append((time1_quick - time0_quick)/len(loopIndex))
    

    plt.figure()
    plt.plot(n, timeArray_insertion, '-r', label='insertion sort')
    plt.plot(n, timeArray_merge, '-b', label='merge sort')
    plt.plot(n, timeArray_selection, '-k', label='selection sort')
    plt.plot(n, timeArray_quick, '-g', label='quick sort')
    plt.legend(loc='upper center')
    plt.title('sort algorithms time-complexity'), plt.xlabel('n'), plt.ylabel('time')
    plt.savefig('sort algorithms time-complexity', dpi=200)
    plt.show()
