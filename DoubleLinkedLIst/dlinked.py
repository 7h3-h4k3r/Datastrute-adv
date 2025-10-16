from lib import node

class DynamicLinkedList:

        def __init__(self):
            self.head = None 
            self.tail = None
        def insert_front(self,data):
            nodes = node.node(data)
            if self.head is None:
                self.tail = self.head = nodes
                return 
            nodes.next = self.head 
            self.head.prev = nodes 
            self.head = nodes
           
            
        def insert_back(self,data):
            nodes = node.node(data)
            if self.tail is None:
                self.head = self.tail = nodes
                return
            self.tail.next = nodes 
            nodes.prev = self.tail 
            self.tail = nodes
            
            

    
            

        def traverse(self):
            current = self.head
            while current.next is not None:
                print("{}".format(current.data))
                current = current.next 
            print(current.data)
        
        def traverse_back(self):
            current = self.tail 
            while current.prev is not None:
                print("{}".format(current.data))
                current = current.prev
            print(current.data)

data = DynamicLinkedList()
data.insert_back(10)
data.insert_back(30)
data.insert_back(70)
data.traverse()
data.traverse_back()