from linkedlist.libs.node import Node

class singleLinked:
    def __init__(self):
        self.head = None 
        self.da = None
    def _insert_(self,data):
        new_node = Node(data)   
        if self.head is None:
            self.head = new_node 
            return
        current = self.head 
        while current.next is not None:
            current = current.next 
        current.next = new_node 
    def _search_(self,target):
        current = self.head 
        while current:
            if current.data == target:
                return True 
            current = current.next 
        return None 
    def _empty_(self):
        if self.head is None:
            return True
        return False
    def _del_(self,target=None,opr=False):
        if opr and target == None:
            self.da = self.head.data
            self.head = self.head.next 
            return self.da
        current = self.head 
        prev = None
        if current.data == target:
            self.head = self.head.next 
            return
        while current:
            if current.data == target:
                if current.next is None:
                    current.next = None 
                    return
                prev.next = current.next 
                return 
            prev = current
            current = current.next 
        return None
    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next