from lib.node import node

class cirDoubleList:

    def __init__(self):
        self.head = None
        

    def append_back(self,data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node 
            self.head.prev = self.head.next = new_node
            return 
        last = self.head.prev
        new_node.next = self.head 
        new_node.prev = last
        last.next = new_node 
        self.head.prev = new_node



    def travers(self):
        current = self.head
        if self.head is None:
            print('none')
            return
        
        while current.next is not None:
            input_from_usr = input("go backward [back] or foreward [front] : ")
            if input_from_usr == "back":
                current = current.prev
            elif input_from_usr == "front":
                current = current.next
            else:
                print("[*] Invalidate Opration")
                return 
            print(current.data)
    

data = cirDoubleList()
data.append_back(10)
data.append_back(43)
data.append_back(75643)
data.travers()
