class Node:

    def __init__(self,data,parent=None):
        '''
            It's Store a Current child and his Parendt 

        '''
        self.data = data 
        self.parent = parent
        self.right = None 
        self.left = None 


class MaxHeapSorted:

    def __init__(self):
        self.root = None 

    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
            return
        self.__insert__(data)

    

    def __insert__(self,data):
        Queue = [self.root]
        new_node = Node(data)
        while Queue:
            node = Queue.pop(0)
            if not node.left:
                new_node.parent = node
                node.left = new_node 
                self.__heapify__(new_node)
                return 
            if not node.right:
                new_node.parent = node 
                node.right = new_node 
                self.__heapify__(new_node)
                return 
            Queue.append(node.left)
            Queue.append(node.right)
    
                
    def __heapify__(self,node):
         
        while node.parent is not None:
            parent = node.parent 
            if parent and parent.data < node.data:
                parent.data , node.data = node.data , parent.data 
                node = parent
            else:
                break 
    def __get_last__(self):
        Queue = [self.root]
        last = None
        while Queue:
            node = Queue.pop(0)
            if node.left is not None:
                last = node
                Queue.append(node.left)
            if node.right is not None:
                last = node  
                Queue.append(node.right) 
            
            if node.right is None and node.right is None:
                last = node

        if last:
            return last
        
    def __heapdown__(self):
        node = self.root 
        while node:
            largest = node
            if node.left and node.left.data > largest.data:
                largest = node.left
            if node.right and node.right.data > largest.data:
                largest = node.right
            if largest != node:
                # Swap values
                node.data, largest.data = largest.data, node.data
                node = largest
            else:
                break
    def extract(self):
        max_value = self.root.data
        last = self.__get_last__()
        if not last:
            self.root = None 
            return max_value
        self.root.data = last.data 
        last.parent = None
        self.__heapdown__()
        return max_value
    def bfserach(self):
        Q = [self.root]
        nodes = []
        while Q:
            u = Q.pop(0)
            nodes.append(u.data)
            if u.left:
                Q.append(u.left)
            if u.right:
                Q.append(u.right)
        print(nodes)

sorted  = MaxHeapSorted()
sorted.insert(10)
sorted.insert(50)
sorted.insert(30)
sorted.insert(90)
sorted.insert(60)
sorted.insert(20)
sorted.bfserach()
sorted_list = []
for i in range(6):
    sorted_list.append(sorted.extract())
print(sorted_list)