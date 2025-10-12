
from libs import node
class UnsortedLinkedList:
    def __init__(self):
        self.head = None

    def __insert_front(self,data):
        current = self.head 
        self.head = node.Node(data)
        self.head.next = current

    def remove(self,data):
        current = self.head 
        previous =  None
        try:
            while current.next is not None:
                if current.data == data:
                    previous.next = current.next
                    return
                previous = current
                current = current.next
        except:
            self.head = current.next
        
        
    def len(self):
        lenof = 0
        current = self.head 
        while current.next is not None:
            lenof+=1 
            current = current.next
        return lenof+1
    
    def indexInsert(self,data,index_value,remove=False):
        if index_value <= 0:
            raise 'Value Error (you call a wrong function for this opration)'
        elif remove:
            self.remove(data,index_value)
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
        
    def insert(self,data,index=False):
        current = self.head
        if current is None:
            self.head = node.Node(data)
            return 
        if index:
            self.__insert_front(data)
            return
        while current.next is not None:
            current = current.next 
       
        current.next = node.Node(data)
    
    def traverse(self):
        current = self.head
        index = 0
        if current is None:
            raise 'Value Error ( LinkedList is Empty )'
        while current.next is not  None:
            print('[{}-{}]->'.format(index,current.data),end='')
            current = current.next 
            index+=1
        print('[{}-{}]-> None'.format(index,current.data))    
Link = UnsortedLinkedList()
Link.insert(10)
Link.insert(20)
Link.insert(30)
Link.insert(40,True)
Link.traverse()
Link.indexInsert(60,2)
Link.traverse()
Link.indexInsert(70,1)
Link.traverse()
Link.remove(70)
Link.traverse()
Link.remove(40)
Link.traverse()
Link.insert(34)
Link.indexInsert(89,3)
Link.traverse()
print(Link.len())