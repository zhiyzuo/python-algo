class StackEmptyError(Exception):
    msg = "Current Stack is empty!"
    def __str__(self):
        return StackEmptyError.msg
    def __repr__(self):
        return StackEmptyError.msg

class QueueEmptyError(Exception):
    msg = "Current Queue is empty!"
    def __str__(self):
        return QueueEmptyError.msg
    def __repr__(self):
        return QueueEmptyError.msg

'''
class DimensionError(Exception):
    msg = "Given input does not match the dimension!"
    def __str__(self):
        return DimensionError.msg
    def __repr__(self):
        return DimensionError.msg
'''
