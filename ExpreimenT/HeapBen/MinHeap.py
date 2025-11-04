from libs.node import Node 
'''

Challenge : MinHeap 

Beginner Level — Core Understanding

Build a Min Heap

Input: [4, 10, 3, 5, 1]

Output: [1, 4, 3, 10, 5]

'''
class MinHeap:

    def __init__(self):
        self.root = None 
    
    def insert(self,value):
        if self.root is None:
            self.root = Node(value)
            return 
        q = [self.root]
        while q:
            node = q.pop(0)
            if not node.left:
                node.left = Node(value)
                self.heapify(node.left)
                return 
            elif not node.right:
                node.right = Node(value)
                self.heapify(node.right)
                return 
            else:
                q.append(node.left)
                q.append(node.right)
    def bsf(self):
        visited = []
        q = [self.root]
        while q:
            u = q.pop(0)
            visited.append(u.data)
            if u.right:
                q.append(u.right)
            if u.left:
                q.append(u.left)
           
        
        return visited
            
    def heapify(self,node):
        while node.data < self.root.data:
            parent = self._getParent(node,self.root)
            if parent and parent.data > node.data:
                parent.data , node.data = node.data, parent.data
                node = parent
            else:
                break 

    
    def _getParent(self,child,root):
        if root is None:
            return None  
        if root.left == child or root.right == child:
            return root 
        left = self._getParent(child,root.left)
        if left:
            return left 
        right = self._getParent(child,root.right)
        if right:
            return right 
        return None
    
    
h = MinHeap()
h.insert(4)
h.insert(10)
h.insert(3)
h.insert(5)
h.insert(1)
print(h.bsf())