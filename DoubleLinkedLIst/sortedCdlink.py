from lib.node import node 

class sortedCricularList:

    def __init__(self):
        self.head = None 
    
    def __insertFront(self,nodes):
       last = self.head.prev
       nodes.next =  self.head
       nodes.prev = last
       last.next = nodes 
       self.head.prev = nodes
       self.head = nodes
    
    def __insertAnywhere(self,nodes,head):
        nodes.prev = head 
        nodes.next = head.next
        head.next.prev = nodes 
        head.next = nodes 

    def __insertBack(self,nodes):
        last = self.head.prev 
        nodes.next = self.head 
        nodes.prev = last
        last.next = nodes
        self.head.prev = nodes
    def insert(self,data):
        new_node = node(data)

        if self.head is None:
            self.head = new_node 
            self.head.prev = self.head.next = new_node 
            return 
        current = self.head 
        if current.data >= data:
            self.__insertFront(new_node)
            return 
        current = self.head
        while (current.next != self.head and current.next.data < data):
            current = current.next

        new_node.next = current.next
        new_node.prev = current
        current.next.prev = new_node
        current.next = new_node 

    def treverse(self):
        current = self.head 
        while current.next is not None:
            input_from_usr = input("go backward [back] or foreward [front] : ")
            if input_from_usr == "back" :
                current = current.prev
            elif input_from_usr == "front":
                current = current.next
            else:
                print("[*] Invalidate Opration")
                return 
            print(current.data)
        

data = sortedCricularList()
data.insert(10)

data.insert(3)
data.insert(5)
data.insert(20)
data.treverse()