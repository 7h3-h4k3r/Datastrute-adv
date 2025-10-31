from LinkedList.singelLinkedList import Lists
from queue import Queue
class Graphs:


    class Vertex:

        def __init__(self,key):
            self.id = key 
            self.adj_list = Lists()

        def onEdge(self,who):
            return self.adj_list.search(who) is not None
        
        def inEdge(self,data):
            if self.onEdge(data):
                self.adj_list.insert(data) 
        
        def delVertex(self):
            pass 




    def __init__(self):
        self.adj = {}


    def insert(self,vertex):
        
        if vertex in self.adj:
            raise ValueError('Error [*] Duplicate Err occured')
        self.adj[vertex] = Graphs.Vertex(vertex)
    
    def get_vertax(self,vertex):

        if vertex not in self.adj:
            raise ValueError('Error [*] Duplicate Err occured')
        return self.adj[vertex]
    
    def connEdge(self,v1,v2):
        vertex_one = self.get_vertax(v1)
        vertex_two = self.get_vertax(v2)
        vertex_one.inEdge(vertex_two)


    def bsTraverse(self,start):
        visited = {start}
        output = []
        q = Queue()
        q.enqueue(start)
        while not q.empty():
            u = q.dequeue()
            output.append(u)

            for child in self.adj[u].adj_list:
                if child.id not in visited:
                    visited.add(child.id)
                    q.enqueue(child.id)
        return output 

    def dfs(self,start,visit):
        if start not in visit:
            visit.append(start)
        for child in self.adj[start].adj_list:
            self.dfs(child.id,visit)
        return visit

    def vertex(self):
        return self.adj


    def _debug(self):
        for key, v in self.adj.items():
            print(f"{key}: {[n.id for n in v.adj_list]}")

gra = Graphs()
gra.insert(1)
gra.insert(2)
gra.insert(3)
gra.insert(4)
gra.insert(5)
gra.insert(6)
gra.connEdge(1,2)
gra.connEdge(2,3)
gra.connEdge(5,6)
gra._debug()
li = [1,2,3,4,5,6]
output = []
i = 0
while i < len(li):
    d = gra.dfs(li[i],[])
    if len(d) == 0:
       i+=1
       output.append(1)
    else:
        output.append(len(d))
    i+= len(d)
print(output)