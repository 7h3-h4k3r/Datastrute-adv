class Node:
    '''
    Balancing Tree is called Heap , Meaning of Heap called Pile 

                  -
                -----
               -------
              ---------
            -------------
    '''
    def __init__(self,data):
        self.data = data 
        self.left = None 
        self.right  = None 


class Heap:

    def __init__(self):
        self.root = None 

    def add(self,data):
        if self.root is None:
            self.root = Node(data)
            return 
        self.__recursive_add__(data,self.root)
    
    def __recursive_add__(self,data,node):

        if node.left is None:
            node.left = Node(data)
            self.heapify(node.left)
        elif node.right is None:
            node.right = Node(data)
            self.heapify(node.right)
        else:
            if self.__get_position__(node.left) <= self.__get_position__(node.right):
                self.__recursive_add__(data,node.left)
            else:
                self.__recursive_add__(data.node.right)


    def __get_position__(self,node):
        if node is None:
            return 0 
        return 1 + self.__get_position__(node.left) + self.__get_position__(node.right) 
    
    def heapify(self,node):
        while node and node != self.root:
            parent = self.__get_parent__(node,self.root)
            if parent.data < node.data:
                parent.data , node.data = node.data,parent.data 
                node = parent 
            else:
                break 

    def __get_parent__(self,node,root):
        if root.left == node or root.right == node:
            return node
        
        if root.left:
            parent = self.__get_parent__(node,root.left)
            if parent is not None:return parent 
        
        if root.right:
            parent = self.__get_parent__(node,root.right)
            if parent is not None:return parent 
        return None
    
    def extreact(self):
        if self.root is None:
            return 'heap list is Empty'
        min = self.root.data 
        last = self.__get_last__(self.root)
        if last is None:
            self.root = None 
            return 
        self.root.data = last.data
        self.heapify_down(self.root)

        return min

    def heapify_down(self,node):
        while node:
            small = node 
            if node.left and node.left.data < small.data:
                small = node.left  
            if node.right and node.right.data < small.data:
                small = node.right 
            if small != node:
                small.data ,node.data = node.data , small.data 
                node =small 
            else:
                return 
    def __get_last__(self,node):
        Queue = [node]
        last_node = None 
        while len(Queue) != 0:
            current = Queue.pop(0)
            if current.left:
                Queue.append(current.left)
            
            if current.right:
                Queue.append(current.right)
            
            if not current.right and not current.left:
                last_node = current 

            if last_node:
                parent = self.__get_parent__(last_node,self.root)
                if parent.left ==last_node:
                    parent.left = None 
                else:
                    parent.right = None 
        return last_node
            
h = Heap()
h.add(10)
h.add(34)
h.add(36)
h.add(37)
data = h.extreact()
print(data)