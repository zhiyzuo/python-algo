# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import time
import sys
sys.path.append("..\..")
from pyalgo.search.binary_search import *

if __name__ == "__main__":
    n = range(0, 10001, 200)
    loopIndex = range(0, 20)
    timeArray1 = []
    timeArray2 = []
    for i in n:
        testArray = range(i)
        x = 100000

        # binary search
        time0 = time.clock()
        for j in loopIndex:
            binary_search(testArray, x)
        time1 = time.clock()
        timeArray1.append((time1 - time0)/len(loopIndex))
        
        # Recursive binary search
        time2 = time.clock()
        for j in loopIndex:
            binary_search(testArray, x, True)
        time3 = time.clock()
        timeArray2.append((time3 - time2)/len(loopIndex))
        
    plt.figure()
    plt.title('binary search time-complexity')
    plt.subplot(211)
    plt.plot(n, timeArray1, '-r')
    plt.title('binary search'), plt.xlabel('n'), plt.ylabel('time')
    plt.subplot(212)
    plt.plot(n, timeArray2, '-r')
    plt.title('recurrsive binary search'), plt.xlabel('n'), plt.ylabel('time')
    plt.savefig('binary search time-complexity.png', dpi=200)
    plt.show()
    
