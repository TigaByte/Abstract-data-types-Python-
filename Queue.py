# Phython Implementation of a Queue
#
#


class Queue():

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            raise IndexError("Queue is empty")

    def front(self):
        if not self.isEmpty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
