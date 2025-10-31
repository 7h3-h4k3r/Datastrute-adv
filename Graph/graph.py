from linkedlist.singleLInkedList import singleLinked 
from linkedlist.Queue import Queue
class Graph:

    class vertax:
        
        def __init__(self,key):
            self.id = key 
            self.adj_list = singleLinked()
        def onEdge(self,destination_vertax):
            return self.adj_list._search_(destination_vertax) is not None
        
        def inEdge(self,destination_vertax):
            if self.adj_list._search_(destination_vertax) is not None:
                raise ValueError('Error : vertax not in the Graph')
            self.adj_list._insert_(destination_vertax)
        def delEdge(self,destVertax):
            self.adj_list._del_(destVertax)
    def __init__(self):
        self.adj = {} 
    
    def _insertVertax(self,key):
        if key in self.adj:
            raise ValueError('Error : Key alreay in the Vertax (duplicate Error segamentaion Fault)')
        self.adj[key] = Graph.vertax(key)
    def _getVertax(self,key):
        if key not in self.adj:
             raise ValueError('Error : Key alreay in the Vertax (duplicate Error segamentaion Fault)')
        return self.adj[key]
    def _insertEdge(self,source_key1,destination_key2):
        source = self._getVertax(source_key1)
        destination = self._getVertax(destination_key2)
        source.inEdge(destination)
    def _delVertax(self,key):
        if key not in self.adj:
              raise ValueError('Error : Key alreay in the Vertax (duplicate Error segamentaion Fault)')
        k= self._getVertax(key)
        for u in self.adj.values():
            if u != k and u.onEdge(k):
                u.delEdge(k)
        del self.adj[key]
    def vertex_count(self):
        return len(self.adj)
    '''
A: ['B', 'C']
B: ['C']
C: ['F']
D: []
E: []
F: []
G: []
H: []
'''
    def BfSearch(self,start_vertax):
        visited_lists = [start_vertax]
        q = Queue()
        q._enqueue(start_vertax)
        while not q.isempty():
            u = q._dequeue()

            for child in self.adj[u].adj_list:
                if child.id not in visited_lists:
                    visited_lists.append(child.id)
                    q._enqueue(child.id)
        if len(visited_lists) == 0:
            return None 
        return visited_lists 
    
    def DfSearch(self,start_vertex,visited):
        if start_vertex not in visited:
            visited.append(start_vertex)
             
        for child in self.adj[start_vertex].adj_list:
            self.DfSearch(child.id,visited)
        
        return visited
        
    

    def reconstruct_path(self, pred, target):
        print(pred)
        path = []
        while target:
            path.append(target)
            target = pred[target]
        return path[::-1]

    def _debug(self):
        for key, v in self.adj.items():
            print(f"{key}: {[n.id for n in v.adj_list]}")



opration = Graph()
opration._insertVertax('A')
opration._insertVertax('B')
opration._insertVertax('C')
opration._insertVertax('D')
opration._insertVertax('E')
opration._insertVertax('F')
opration._insertVertax('G')
opration._insertVertax('H')
opration._insertEdge('A','B')
opration._insertEdge('B','C')
opration._insertEdge('A','C')
opration._insertEdge('C','F')
opration._insertEdge('A','D')


bsf_result = opration.BfSearch('A')
dfs_result = opration.DfSearch('A',[])
print(dfs_result)