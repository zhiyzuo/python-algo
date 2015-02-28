# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import time
import sys
sys.path.append("..\..")
from pyalgo.sort.merge_sort import *

if __name__ == "__main__":
    n = range(0, 1001, 20)
    loopIndex = range(0, 10)
    timeArray = []
    for i in n:
        testArray = range(i)
        np.random.shuffle(testArray)

        time0 = time.clock()
        for j in loopIndex:
            merge_sort(testArray)
        time1 = time.clock()
        timeArray.append((time1 - time0)/len(loopIndex))

    plt.figure()
    plt.plot(n, timeArray, '-r')
    plt.title('merge sort time-complexity'), plt.xlabel('n'), plt.ylabel('time')
    plt.savefig('merge sort time-complexity', dpi=200)
    plt.show()
