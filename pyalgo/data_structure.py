import numpy as np
from utils.exceptions import *

class Stack:
# {{{ Stack class
    def __init__(self, items=[]):
        try:
            self.top = -1
            self.length = 0
            if type(items) in [int, float, str]:
                self.items = np.array([items])
            elif type(items) in [np.ndarray, list]:
                self.items = np.asarray(items)
            else:
                raise TypeError('Please check the input!')
        except TypeError:
            raise

    def push(self, item):
        self.items = np.append(self.items,item)
        self.top = self.top + 1

    def pop(self):
        try:
            if self.is_empty():
                raise StackEmptyError
            self.top = self.top - 1
            _pop_item = self.items[-1]
            self.items = np.delete(self.items, -1)
            return _pop_item
        except:
            raise

    def get_top(self):
        return self.top

    def is_empty(self):
        return self.items.size == 0

    def get_size(self):
        return self.items.size

    def __repr__(self):
        return "Stack:\n{}".format(self.items)

    def __str__(self):
        return repr(self)
# }}}

# # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Queue:
# {{{ Queue class
    def __init__(self, items=[]):
        try:
            self.top = -1
            self.length = 0
            if type(items) in [int, float, str]:
                self.items = np.array([items])
            elif type(items) in [np.ndarray, list]:
                self.items = np.asarray(items)
            else:
                raise TypeError('Please check the input!')
        except TypeError:
            raise

    def enqueue(self, item):
        self.items.append(item)
        self.top = self.top + 1

    def dequeue(self):
        try:
            if self.is_empty():
                raise QueueEmptyError
            self.top = self.top - 1
            _dequeue_item = self.items[-1]
            self.items = np.delete(self.items, -1)
            return _dequeue_item

        except QueueEmptyError:
            raise

    def get_top(self):
        return self.top

    def is_empty(self):
        return self.items.size == 0

    def get_size(self):
        return self.items.size

    def __repr__(self):
        return "Queue:\n{}".format(self.items)

    def __str__(self):
        return repr(self)
# }}}
