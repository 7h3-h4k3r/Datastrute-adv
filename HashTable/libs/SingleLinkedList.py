from libs.node import Node 

class SingleLinkedList:

    def __init__(self):
        self.head = None 
    
    def insert(self,value):
        if self.head is None:
            self.head  = Node(value)
            return
        current = self.head 
        self.head = Node(value)
        self.head.next = current

    def deleted(self,target):
        current = self.head
        prev = None 
        while current:
            if current.value == target:
                if prev is None:
                    self.head = self.head.next 
                elif self.head.next is None:
                    prev.next = None 
                    self.head = prev
                else:
                    prev.next = current.next 
                    self.head = prev 
                return True 
            prev = current 
            current = current.next 
        raise 'Not in List'

    def search(self,value):
        current = self.head 
        while current:
            if current.value == value:
                return True 
            current = current.next 
        return None
    def Traverse(self):
        current = self.head 
        while current:
            print(current.value)
            current = current.next

