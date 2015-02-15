# -*- coding: utf-8 -*-
import sys
sys.path.append("..\..")
from pyalgo.data_structure import *

def test_print():
    print "\tStack is empty:" , myStack.is_empty()
    print "\tStack top:", myStack.get_top()
    print "\tStack size:", myStack.get_size()
    print "\tStack __repr__:", myStack.__repr__()
    print "\tStack __str__:", myStack.__str__()

if __name__ == "__main__": 
    # test Stack class
    myStack = Stack()
    print "Step 1: pop when stack is empty"
    test_print()
    # myStack.pop()

    print "\nStep 2: push single item to stack"
    print "  push one item to stack"
    myStack.push(0)
    print "\tThe first item in Stack:", myStack.items[0], type(myStack.items[0])
    test_print()
    print "  pop one item out of stack"
    myStack.pop()
    test_print()

    print "  push one item to stack"
    myStack.push('test')
    print "\tThe first item in Stack:", myStack.items[0], type(myStack.items[0])
    test_print()
    print "  pop one item out of stack"
    myStack.pop()
    test_print()

    print "  push one item to stack"
    myStack.push(['my','Stack','test'])
    print "\tThe first item in Stack:", myStack.items[0], type(myStack.items[0])
    print "\tThe last item in Stack:", myStack.items[myStack.get_size()-1], type(myStack.items[myStack.get_size()-1])
    test_print()
    print "  pop one item out of stack"
    myStack.pop()
    test_print()
    print "  pop one item out of stack"
    myStack.pop()
    test_print()
    print "  push one item to stack"
    myStack.push('test')
    print "\tThe first item in Stack:", myStack.items[0], type(myStack.items[0])
    test_print()
    print "  pop one item out of stack"
    myStack.pop()
    test_print()
    print "  pop one item out of stack"
    myStack.pop()
    test_print()

    print "\nStep 3: continuously push to stack"
    print "  push 0-9999 to Stack"
    for i in range(1,10001):
        myStack.push(i-1)
    print "\tThe first item in Stack:", myStack.items[0], type(myStack.items[0])
    print "\tThe Last item in Stack:", myStack.items[myStack.get_size()-1], type(myStack.items[myStack.get_size()-1])
    test_print()
    print "  pop out of Stack"
    for i in range(1,1001):
        myStack.pop()
    print "\tThe first item in Stack:", myStack.items[0], type(myStack.items[0])
    print "\tThe Last item in Stack:", myStack.items[myStack.get_size()-1], type(myStack.items[myStack.get_size()-1])
    test_print()
    print "  push one item to stack"
    myStack.push(['my','Stack','test'])
    print "\tThe Last item in Stack:", myStack.items[myStack.get_size()-1], type(myStack.items[myStack.get_size()-1])
    test_print()
    print "  pop all out of Stack"
    for i in range(1,myStack.get_size()+1):
        myStack.pop()
    test_print()
    print "  pop when Stack is empty"
    myStack.pop()
