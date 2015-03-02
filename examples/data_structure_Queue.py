# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
from pyalgo.data_structure import *

def test_print():
    print "\tQueue is empty:" , myQueue.is_empty()
    print "\tQueue top:", myQueue.get_top()
    print "\tQueue size:", myQueue.get_size()
    print "\tQueue __repr__:", myQueue.__repr__()
    print "\tQueue __str__:", myQueue.__str__()

if __name__ == "__main__": 
    # test Queue class
    myQueue = Queue()
    print "Step 1: dequeue when Queue is empty"
    test_print()
    # myQueue.dequeue()


    print "\nStep 2: enqueue single item to Queue"
    print "  enqueue one item to Queue"
    myQueue.enqueue(0)
    print "\tThe first item in Queue:", myQueue.items[0], type(myQueue.items[0])
    test_print()
    print "  dequeue one item out of Queue"
    myQueue.dequeue()
    test_print()

    print "  enqueue one item to Queue"
    myQueue.enqueue('test')
    print "\tThe first item in Queue:", myQueue.items[0], type(myQueue.items[0])
    test_print()
    print "  dequeue one item out of Queue"
    myQueue.dequeue()
    test_print()


    print "  enqueue one item to Queue"
    myQueue.enqueue(['my','Queue','test'])
    print "\tThe first item in Queue:", myQueue.items[0], type(myQueue.items[0])
    print "\tThe last item in Queue:", myQueue.items[myQueue.get_size()-1], type(myQueue.items[myQueue.get_size()-1])
    test_print()
    print "  dequeue one item out of Queue"
    myQueue.dequeue()
    print "\tThe first item in Queue:", myQueue.items[0], type(myQueue.items[0])
    print "\tThe last item in Queue:", myQueue.items[myQueue.get_size()-1], type(myQueue.items[myQueue.get_size()-1])
    test_print()
    print "  dequeue one item out of Queue"
    myQueue.dequeue()
    print "\tThe first item in Queue:", myQueue.items[0], type(myQueue.items[0])
    print "\tThe last item in Queue:", myQueue.items[myQueue.get_size()-1], type(myQueue.items[myQueue.get_size()-1])
    test_print()
    print "  enqueue one item to Queue"
    myQueue.enqueue('test0')
    print "\tThe first item in Queue:", myQueue.items[0], type(myQueue.items[0])
    print "\tThe last item in Queue:", myQueue.items[myQueue.get_size()-1], type(myQueue.items[myQueue.get_size()-1])
    test_print()
    print "  dequeue one item out of Queue"
    myQueue.dequeue()
    test_print()
    print "  dequeue one item out of Queue"
    myQueue.dequeue()
    test_print()


    print "\nStep 3: continuously enqueue to Queue"
    print "  enqueue 0-9999 to Queue"
    for i in range(1,10001):
        myQueue.enqueue(i-1)
    print "\tThe first item in Queue:", myQueue.items[0], type(myQueue.items[0])
    print "\tThe Last item in Queue:", myQueue.items[myQueue.get_size()-1], type(myQueue.items[myQueue.get_size()-1])
    test_print()
    print "  dequeue out of Queue"
    for i in range(1,1001):
        myQueue.dequeue()
    print "\tThe first item in Queue:", myQueue.items[0], type(myQueue.items[0])
    print "\tThe Last item in Queue:", myQueue.items[myQueue.get_size()-1], type(myQueue.items[myQueue.get_size()-1])
    test_print()
    print "  enqueue one item to Queue"
    myQueue.enqueue(['my','Queue','test'])
    print "\tThe first item in Queue:", myQueue.items[0], type(myQueue.items[0])
    print "\tThe Last item in Queue:", myQueue.items[myQueue.get_size()-1], type(myQueue.items[myQueue.get_size()-1])
    test_print()
    print "  dequeue all out of Queue"
    for i in range(1,myQueue.get_size()+1):
        myQueue.dequeue()
    test_print()
    print "  dequeue when Queue is empty"
    myQueue.dequeue()

