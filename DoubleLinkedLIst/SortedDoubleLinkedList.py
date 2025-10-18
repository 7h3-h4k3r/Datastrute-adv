from lib.node import node
class SortedDoubleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __insertBack(self,nodes): 
        self.tail.next = nodes
        nodes.prev = self.tail
        self.tail = nodes

    def __insertFront(self,nodes):
        nodes.next = self.head 
        self.head.prev = nodes 
        self.head = nodes
    def insert(self,data):
        new_node =  node(data)
        if self.head is None:
            self.head = self.tail = new_node
            return 
        current = self.head 

        if current.prev is None and current.data >= data:
            self.__insertFront(new_node)
        
        elif current.next is None and current.data <= data:
            self.__insertBack(new_node)
        
        else:
            while current.next is not None:
                if current.data <= data and data  <= current.next.data:
                    # print(current.data ,"<=", data ,"and" ,data, "<=", current.next.data)
                    new_node.prev = current
                    new_node.next = current.next
                    current.next.prev = new_node
                    current.next = new_node 
                    return
                current = current.next
            if current.next is None:
                self.__insertBack(new_node)

    def traverse(self):
        current = self.head
        while current.next is not None:
            print(current.data)
            current = current.next 
        print(current.data)
    def traverseBack(self):
        current = self.tail
        while current.prev is not None:
            print(current.data)
            current = current.prev 
        print(current.data)
data = SortedDoubleLinkedList()
data.insert(10)
data.insert(50)
data.insert(30)
data.insert(40)
data.insert(70)
data.insert(20)
data.traverse()
data.traverseBack()

        