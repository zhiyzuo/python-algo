class EmptyError(Exception):

    def __init__(self, message="object"):
        self.message = "Current {} is empty!".format(message)

    def __str__(self):
        return self.msg
    def __repr__(self):
        return self.msg

'''
class DimensionError(Exception):
    msg = "Given input does not match the dimension!"
    def __str__(self):
        return DimensionError.msg
    def __repr__(self):
        return DimensionError.msg
'''
