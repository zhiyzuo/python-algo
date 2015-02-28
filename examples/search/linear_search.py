# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import time
import sys
sys.path.append("..\..")
from pyalgo.search.linear_search import *

if __name__ == "__main__":
    n = range(0, 10001, 100)
    loopIndex = range(0, 10)
    timeArray = []
    for i in n:
        testArray = range(i)
        x = 100000
        
        time1 = time.clock()
        for j in loopIndex:
            linear_search(testArray, x)
        time2 = time.clock()
        timeArray.append((time2 - time1)/len(loopIndex))

    plt.figure()
    plt.plot(n, timeArray, '-r')
    plt.title('linear search time-complexity'), plt.xlabel('n'), plt.ylabel('time')
    plt.savefig('linear search time-complexity', dpi=200)
    plt.show()
