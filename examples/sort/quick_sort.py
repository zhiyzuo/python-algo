# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import time
import sys
sys.path.append("..\..")
from pyalgo.sort.sort import *

if __name__ == "__main__":
    n = range(0, 10001, 200)
    timeArray = []
    for i in n:
        testArray = range(i)
        np.random.shuffle(testArray)

        time0 = time.clock()
        quick_sort(testArray)
        time1 = time.clock()
        timeArray.append(time1 - time0)

    plt.figure()
    plt.plot(n, timeArray, '-r')
    plt.title('quick sort time-complexity'), plt.xlabel('n'), plt.ylabel('time')
    plt.savefig('quick sort time-complexity', dpi=200)
    plt.show()
