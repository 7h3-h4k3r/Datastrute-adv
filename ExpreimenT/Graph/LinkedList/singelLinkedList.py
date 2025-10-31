from node.Node import Node 

class Lists:

    def __init__(self,):
        self.head = None 
       
    def isEmpty(self):
        return self.head is None
    

    def __iter__(self):
        current = self.head
        while current:
            yield current.data   
            current = current.next

    def __insert__stack(self,data):
        '''
        
        stack is Last in First Out or First In Last Out

        FIFO , LIFO

        '''
        if self.head is None:
            self.head  = Node(data)
            return
        current = self.head 
        self.head = Node(data)
        self.head.next = current
        
    
    def __insert__queue(self,data):
        '''
        Queue

        First In first Out : FIFO 

        Last in Last Out : LILO

        '''
        newNode = Node(data)
        current = self.head 
        if self.head is None:
            self.head = newNode 
            return
        
        while current.next is not None:
            current = current.next 
        current.next = newNode 

        

    def __pop__stack(self):
        
        if self.head is None:
            raise ValueError('Error [*] ( stack is empty )')
        current = self.head 
        prev  = None
        while current.next is not None:
            prev = current
            current = current.next 
        pop_data = current.data
        prev.next = None 
        return pop_data
    
    def __de__queue(self):
        if self.head is None:
            raise ValueError('Error [*] ( Queue is empty )')
        dequeue = self.head.data 
        self.head = self.head.next
        return dequeue

    def enqueue(self,data):
        '''
        Enqueue: Adds an element to the rear of a queue.

        '''
        self.__insert__queue(data)


    def push(self,data):
        '''
        Push: Adds an element to the top of a stack.

        '''
        self.__insert__stack(data)

    def pop(self):
        '''
        Pop: Removes an element from the top of a stack.
        
        '''
        return self.__pop__stack()

    def dequeue(self):
        '''
        Dequeue: Removes an element from the front of a queue.

        '''
        return self.__de__queue()

    def insert(self,data):
        
        self.__insert__queue(data)


    def search(self,target):
        curr = self.head 
        while curr:
            if curr.data == target:
                return None
        return True
    def traverse(self):
        current = self.head 
        while current:
            print(current.data,end=' ')
            current = current.next 
        




