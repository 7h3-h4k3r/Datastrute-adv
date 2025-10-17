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
            
            

        def _search(self,target):
            current = self.head 
            while current.data != target: 
                current = current.next 
            
            if current.data == target:
                return current 
            return None
        
        def deleted(self,data):
            nodes = self._search(target=data)
            if nodes is None:
                print('Invalidated value Error : Target not in the List')
                return 
            if nodes.prev is None:
                if nodes.next is None:
                    self.head = self.tail = None 
                else:
                    self.head = nodes.next 
            elif nodes.next is None:
                self.tail = nodes.prev 
                self.tail.next =None 
            else:
                middelt = nodes.prev  
                middelt.next = nodes.next
                

        def traverse(self):
            current = self.head
            if self.head is None:
                print('none')
                return
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
data.insert_back(40)
data.insert_back(60)
data.insert_back(80)
data.deleted(80)
data.deleted(40)
data.traverse()
