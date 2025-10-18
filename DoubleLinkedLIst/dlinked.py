from lib import node

class DynamicLinkedList:

        def __init__(self):
            self.head = None 
            self.tail = None
        def append_front(self,data):
            nodes = node.node(data)
            if self.head is None:
                self.tail = self.head = nodes
                return 
            nodes.next = self.head 
            self.head.prev = nodes 
            self.head = nodes
           
            
        def append_back(self,data):
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
        
        def insert(self,data,insertdata,exchange=False):
            current = self.head 
            if exchange:
                while current.data:
                    if current.data == data:
                        current.data = insertdata
                        return
                    current = current.next
                raise 'Value Error data not in The List'
            new_node = node.node(insertdata)
            while current.next is not None:
                if current.data == data:
                    new_node.prev = current
                    new_node.next = current.next
                    current.next.prev = new_node 
                    current.next = new_node
                    return 
                current = current.next
            
        def traverse_back(self):
            current = self.tail 
            while current.prev is not None:
                print("{}".format(current.data))
                current = current.prev
            print(current.data)

data = DynamicLinkedList()
data.append_back(10)
data.append_back(40)
data.append_back(60)
data.append_back(80)
data.insert(40,50)
data.insert(30,90)
data.insert(10,30)
data.insert(80,78,True)
data.traverse()
print("=======================")
# data.deleted(80)
# data.deleted(40)
data.traverse_back()
