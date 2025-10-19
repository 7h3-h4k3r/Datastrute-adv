from libs.node import node


class singleLinkedList:

    def __init__(self):
        self.head = None

    def insert(self,data):
        new_node = node(data)

        if self.head is None:
            self.head = new_node 
            return 
        older_header = self.head 
        self.head = new_node 
        new_node.next = older_header 
    
    def peek(self):
        if self.head is None:
            raise ValueError("[*]Error occured : Stack is Empty ")
        return self.head.data 

    def index(self,data):
        current = self.head 
        i  = 0 
        try:
            while current.data != data:
                i+=1
                current = current.next 
            return i
        except:
            return None
         
    def pop(self):
        if self.head is None:
            raise ValueError("[*]Error occured : NO More value on stack  ")
        self.head = self.head.next 
        return None
        

    def _traverse(self):
        current = self.head 
        while current.next is not None:
            print(current.data)
            current = current.next 
        print(current.data)
    def is_empty(self):
        if self.head is None:
            return True 
        return False
