
from libs.nodes import node


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
    
    def delt(self,index):
        current = self.head 
        i = 0
        previous = None

        if self.len()-1 == index:
            raise 'Value Error : invalidate Syntax out of Range'
        try:
            while current.next is not None:
                if i == index:
                    previous.next = current.next
                    return
                i+=1
                previous = current
                current = current.next
        except:
            self.head = current.next
    def pop(self):
        if self.head is None:
            raise 'Value Error : InValidate syntax \'0\'' 
        current = self.head 
        lenof = self.len() -1
        i = 1
        while current.next is not None:
            if i == lenof:
                current.next = None
                return
            current = current.next
            i+=1 

        self.head = current  
    def len(self):
        lenof = 0
        current = self.head 
        while current.next is not None:
            lenof+=1 
            current = current.next
        return lenof+1
    
    def insert(self,data,index_value):
        if index_value <= 0 or self.len()-1 < index_value:
            raise 'Value Error (you call a wrong function for this opration)'
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
        
    def append(self,data,index=False):
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
