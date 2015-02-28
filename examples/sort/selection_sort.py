# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import time
import sys
sys.path.append("..\..")
from pyalgo.sort.selection_sort import *

if __name__ == "__main__":
    n = range(0, 1001, 20)
    timeArray = []
    for i in n:
        testArray = range(i)
        np.random.shuffle(testArray)

        time0 = time.clock()
        selection_sort(testArray)
        time1 = time.clock()
        timeArray.append(time1 - time0)

    plt.figure()
    plt.plot(n, timeArray, '-r')
    plt.title('selection sort time-complexity'), plt.xlabel('n'), plt.ylabel('time')
    plt.savefig('selection sort time-complexity', dpi=200)
    plt.show()
