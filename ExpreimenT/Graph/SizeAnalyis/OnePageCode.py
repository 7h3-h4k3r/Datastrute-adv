import sys

class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
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
        


class Queue:

    def __init__(self):
        self.head = Lists()

    def enqueue(self,data):
        self.head.enqueue(data)

    def dequeue(self):
        return self.head.dequeue()

    def empty(self):
        return self.head.isEmpty()
    def walkTheQueu(self):
        self.head.traverse()




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

# gra = Graphs()
# gra.insert(1)
# gra.insert(2)
# gra.insert(3)
# gra.insert(4)
# gra.insert(5)
# gra.insert(6)
# gra.connEdge(1,2)
# gra.connEdge(2,3)
# gra.connEdge(5,6)
# gra._debug()
# li = [1,2,3,4,5,6]
# output = []
# i = 0
# while i < len(li):
#     d = gra.dfs(li[i],[])
#     if len(d) == 0:
#       i+=1
#       output.append(1)
#     else:
#         output.append(len(d))
#     i+= len(d)
# print(output)
def returnGraphData(args):
    datas = list(map(int,args))
    vertex = [i for i in range(1,datas[0]+1)]
    Edges_data = datas[2:]
    Edges = [(Edges_data[i-1],Edges_data[i])for i in range(1,len(Edges_data),2)]
    
    return vertex,Edges
def sizeAnalysis(args):
    vertex , Edges = returnGraphData(args)
    
    '''
        add vertex to the Graph 
    '''
    g = Graphs()
    
    for vertex_ in vertex:
        g.insert(vertex_)
    '''
        connected  a vertex Edges
        
    '''
    for v1 ,v2 in Edges:
        g.connEdge(v1,v2)
    
    output = []
    i = 0
    while i < len(vertex):
        d = g.dfs(vertex[i],[])
        if len(d) == 0:
          i+=1
          output.append(1)
        else:
            output.append(len(d))
        i+= len(d)
    output = sorted(output)
    print(output)
    
    
    
if __name__ == "__main__":
    if len(sys.argv) > 1:
       sizeAnalysis(sys.argv[1:])
    else:
        print("No arguments provided.")
