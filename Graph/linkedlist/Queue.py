from linkedlist.singleLInkedList import singleLinked
class Queue:


    def __init__(self):
        self.head = singleLinked()
    def _enqueue(self,data):
        self.head._insert_(data)
    def _dequeue(self):
        return self.head._del_(None,opr=True)
    def isempty(self):
        return self.head._empty_()
