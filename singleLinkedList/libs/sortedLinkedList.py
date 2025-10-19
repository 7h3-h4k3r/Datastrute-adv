from nodes import node


class sortedLinkedList:

    def __init__(self):
        self.head =  None 

    def len(self):
        lenof  =  1 
        current = self.head     
        while current.next is not None:
            current = current.next 
            lenof +=1 
        return lenof
    

    def __insert_front(self,data):
        current = self.head 
        self.head = node.Node(data)
        self.head.next = current

    def insert(self,data,index_value):
        if index_value <= 0 or self.len()-1 < index_value:
            self.__insert_front(data)
            return
        index = 0
        current = self.head 
        prevaios = None 
        while current.next is not None:
            prevaios = current
            if index == index_value-1:
                current = current.next
                break 
            current = current.next 
            index+=1 
        prevaios.next = node.Node(data)
        prevaios = prevaios.next
        prevaios.next = current


    def search(self,target):
        curr  = self.head 
        while curr.next is not None:
            if curr.data == target:
                return True
            curr = curr.next 
        return None
        
    def compair(self,data):
        if self.head.data >= data:
            if self.head.data >= data:
                older_head = self.head 
                self.head = node.Node(data)
                self.head.next = older_head
                return True 
            return False
        

    def add(self,data):
        current = self.head
        previous = 0
        index = 0
        if current is None:
            self.head = node.Node(data)
            return
        
        if self.len() == 1:
            return self.compair(data)
        
        while current.next is not None:
            if previous <= data:
                if data <= current.data:
                    self.insert(data,index)
                    return
            previous = current.data 
            current = current.next
            index+=1 
        current.next  = node.Node(data)
    
    def traverse(self):
        current = self.head 
        while current.next is not None:
            print(current.data)
            current = current.next 
        print(current.data) 


data = sortedLinkedList()
data.add(10)
data.add(6)
data.add(5)
data.add(3)
data.add(1)
data.add(70)
if data.search(6):
    print("FOund it")
else:
    print("Not found")
data.traverse()