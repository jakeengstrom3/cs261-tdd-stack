# Stack: A stack.
# Your implementation should pass the tests in stack.py.
# YOUR NAME

class Stack:

    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def pop(self):
        if self.is_empty():
            raise IndexError("Cannon Pop from empty Stack")
        val = self.data[-1]
        del self.data[-1]
        return val
        

    def peek(self):
        if self.is_empty():
            raise IndexError("Cannon Peek an empty Stack")
        return self.data[-1]

    def push(self, val):
        self.data.append(val)
            