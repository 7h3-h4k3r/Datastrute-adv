from LinkedList.singelLinkedList import Lists

class Queue:

    def __init__(self):
        self.head = Lists()

    def enqueue(self,data):
        self.head.enqueue(data)

    def dequeue(self):
        return self.head.dequeue()

    def empty(self):
        return self.head.isEmpty()
    def walkTheQueu(self):
        self.head.traverse()

