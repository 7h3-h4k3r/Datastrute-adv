'''

Heap Maximum 

'''
from libs.node import Node

class MaxHeap:

    def __init__(self):
        self.root = None 

    def insert(self,data):
        new_node  = Node(data)
        if self.root is None:
            self.root = new_node
            return 
        Q = [self.root]
        while Q:
            u = Q.pop(0)
            if not u.left:
                new_node.parent = u 
                u.left = new_node 
                self.heapify(new_node)
                return 
            if not u.right:
                new_node.parent = u 
                u.right = new_node
                self.heapify(new_node)
                return 
            Q.append(u.left)
            Q.append(u.right)
    

    def heapify(self,node): 
        while node.parent is not None:
            parent = node.parent
            if node.data > parent.data:
                node.data , node.parent.data = node.parent.data , node.data
                node = parent 
            else:
                break

    def bfs(self):
        visited = []
        Queue = [self.root]
        while Queue:
            u = Queue.pop(0)
            visited.append(u.data)
            if u.left:
                Queue.append(u.left)
            if u.right:
                Queue.append(u.right)
        if not visited:
            return 'List is Empty'
        return visited
h = MaxHeap()
for i in [3, 9, 2, 1, 4, 5]:
    h.insert(i)
print(h.bfs())