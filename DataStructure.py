class Stack:

    def __init__(self, items=[]):
        self.top = -1
        self.length = 0
        if type(items) == int:
            self.items = [items]
        else:
            self.items = items

    def push(self, item):
        self.items.append(item)
        self.top = self.top + 1

    def pop(self):
        if self.isEmpty():
            print "This stack is already empty!"
            return
        self.top = self.top - 1
        return self.items.pop()

    def getTop(self):
        return self.top

    def isEmpty(self):
        return len(self.items) == 0

    def getSize(self):
        return len(self.items)

    def __repr__(self):
        return "Stack: {}".format(self.items)

    def __str__(self):
        return "Stack: {}".format(self.items)

class Queue:

    def __init__(self, items=[]):
        self.top = -1
        self.length = 0
        if type(items) == int:
            self.items = [items]
        else:
            self.items = items

    def enqueue(self, item):
        self.items.append(item)
        self.top = self.top + 1

    def dequeue(self):
        if self.isEmpty():
            print "This queue is already empty!"
            return
        self.top = self.top - 1
        return self.items.pop(0)

    def getTop(self):
        return self.top

    def isEmpty(self):
        return len(self.items) == 0

    def getSize(self):
        return len(self.items)

    def __repr__(self):
        return "Queue: {}".format(self.items)

    def __str__(self):
        return "Queue: {}".format(self.items)
