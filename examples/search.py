# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import time
import sys
sys.path.append("..")
from pyalgo.search.linear_search import *
from pyalgo.search.binary_search import *

if __name__ == "__main__":
    n = range(0, 1001, 20)
    loopIndex = range(0, 20)
 
    # linear search
    timeArray_linear = []
    for i in n:
        testArray = range(i)
        x = 100000

        time0_linear = time.clock()
        for j in loopIndex:
            linear_search(testArray, x)
        time1_linear = time.clock()
        timeArray_linear.append((time1_linear - time0_linear)/len(loopIndex))

    # binary search
    timeArray_binary = []
    for i in n:
        testArray = range(i)
        x = 100000
        time0_binary = time.clock()
        for j in loopIndex:
            binary_search(testArray, x)
        time1_binary = time.clock()
        timeArray_binary.append((time1_binary - time0_binary)/len(loopIndex))
        
    # recursive binary search
    timeArray_recursive = []
    for i in n:
        testArray = range(i)
        x = 100000
        time0_recursive = time.clock()
        for j in loopIndex:
            binary_search(testArray, x, True)
        time1_recursive = time.clock()
        timeArray_recursive.append((time1_recursive - time0_recursive)/len(loopIndex))
        
    plt.figure()
    plt.title('search time-complexity')
    plt.plot(n, timeArray_linear, '-r', label='linear search')
    plt.plot(n, timeArray_binary, '-b', label='binary search')
    plt.plot(n, timeArray_recursive, '-k', label='recursive binary search')
    plt.legend(loc='upper center')
    plt.title('search algorithms time-complexity'), plt.xlabel('n'), plt.ylabel('time')
    plt.savefig('search algorithms time-complexity.png', dpi=200)
    plt.show()
    
