class heap:

    def __init__(self):
        self.heap_list=[]

    def insert(self,data):
        self.heap_list.append(data)
        self.heapify(len(self.heap_list)-1)

    def swap(self,parent,index):
        self.heap_list[parent],self.heap_list[index] = self.heap_list[index],self.heap_list[parent]

    def heapify(self,index):
        parent = (index -1)//2 
        if index > 0 and self.heap_list[index] > self.heap_list[parent]:
            self.swap(parent=parent,index=index)
            self.heapify(parent)
    def _len(self):
        return len(self.heap_list)
    def extract_Max(self):
        last = self.heap_list.pop()
        self.heap_list[0] = last 
        self.heapify(len(self.heap_list)-1)
    def heapidown(self,index=0):
        larger = index 
        left  = 2*index +1 
        right = 2*index +2
        lenof = self._len()
        if left < lenof and self.heap_list[larger] < self.heap_list[left]:
            larger = left 
        if right <lenof and self.heap_list[larger] < self.heap_list[right]:
            larger = right 

        if larger != index:
            self.heap_list[index], self.heap_list[larger] = self.heap_list[larger], self.heap_list[index]
            self.heapidown(larger) 
    
    def display(self):
        print(self.heap_list)

Data = heap()
data = [9, 7, 8, 6, 5, 1, 2, 3, 4]
for i in data:
    Data.insert(i)
Data.display()
Data.extract_Max()
Data.display()