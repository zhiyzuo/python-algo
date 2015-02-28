# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import time
import sys
sys.path.append("..\..")
from pyalgo.sort.counting_sort import *

if __name__ == "__main__":
    n = range(1, 10001, 200)
    loopIndex = range(0, 20)
    timeArray = []
    for i in n:
        testArray = range(i)
        np.random.shuffle(testArray)

        time0 = time.clock()
        for j in loopIndex:
            counting_sort(testArray)
        time1 = time.clock()
        timeArray.append((time1 - time0)/len(loopIndex))


    plt.figure()
    plt.plot(n, timeArray, '-r')
    plt.title('counting sort time-complexity'), plt.xlabel('n'), plt.ylabel('time')
    plt.savefig('counting sort time-complexity.png', dpi=200)
    plt.show()
