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
            return self.items.pop(0)
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



def testQueue():
    Q = Queue()
    print(f" enqueue: {Q.enqueue(1)}")
    print(f" enqueue: {Q.enqueue(2)}")
    print(f" size: {Q.size()}")
    print(f" isEmpty: {Q.isEmpty()}")
    print(f" front: {Q.front()}")
    print(f" dequeue: {Q.dequeue()}")
    print(f" dequeue: {Q.dequeue()}")
    print(f" isEmpty: {Q.isEmpty()}")



testQueue()