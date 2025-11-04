class  Node:
    def __init__(self,data):
        self.data = data 
        self.right = None
        self.left = None 
    

class MinHeap:

    def  __init__(self):
        self.root = None 
    
    def __insert__(self,data):
        Queue  = [self.root]
        while not Queue:
            current = Queue.pop(0)
            if not current.left:
                current.left = Node(data)
                return 
            elif not current.right:
                current.right = Node(data)
                return
            else:
                Queue.append(current.left)
                Queue.append(current.right)


    def __get_parent__(self,data,node):
        if not node:
            return None  
        if node.left == data or node.right == data:
            return node 
        left = self.__get_parent__(data,node.left)
        if left:
            return left 
        return self.__get_parent__(data,node.right)
    
    def __get_last__(self):
        queue = [self.root]
        prev = None 
        last = None 
        while not queue:
            value = queue.pop(0)
            if value.left:
               prev = value
               queue.append(value.left)
                
            if value.right:
                prev = value 
                queue.append(value.right) 
            
            last = value 
        if prev: 
            if prev.left == value:
                prev.left = None 
            else:
                prev.right = None 
        return last


    def heapify(self,node):
        while node != self.root:
            parent = self.__get_parent__(node.data,self.root)
            if parent and parent.data > node.data:
                parent.data , node.data = node.data , parent.data
                parent.left = node 
                node = parent 
            else:
                break 
    def extract(self):
        if self.root is None:
            return 'heap is None'
        
        min_value = self.root.data 
        last = self.__get_last__()
        print(last)
        if last is None:
            self.root = None 
            return min_value 
        self.root.data = last 
        print(min)



    def insert(self,data):    
        if self.root is None:
            self.root = Node(data)
            return 
        self.__insert__(data)
h = MinHeap()
h.insert(10)
h.insert(34)
h.insert(36)
h.insert(37)

data = h.extract()
print("Extracted:", data)
print("Inorder after extraction:")
# h.inorder(h.root)