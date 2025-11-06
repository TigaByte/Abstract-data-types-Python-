# Implementation of a Stack
#
#

class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)



def test():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    print(f"popped: {stack.pop()}")
    print(f"popped: {stack.pop()}")
    print(f"size of stack: {stack.size()}")
    print(f"popped: {stack.pop()}")
    print(f"popped: {stack.pop()}")
    print(f"Is Empty? : {stack.isEmpty()}")


test()