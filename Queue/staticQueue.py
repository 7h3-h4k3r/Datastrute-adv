
class Queue:
    
    def __init__(self,Max_size):
        self.MaxSize = Max_size 
        self.array = [None] * self.MaxSize
        self.front = 0 
        self.rear= 0 
        self.size = 0
    def enqueue(self,data):
        if self.size == self.MaxSize:
            print("List of Array hase been Fulled")
            return 
        self.array[self.front] = data 
        self.front = (self.front+1) % self.MaxSize
        self.size +=1 
    
    def dequeue(self):
        if self.size == 0:
            print("List is empty no Rear opration occur")
            return 
        self.array[self.rear] = None
        self.rear = (self.rear+1)%self.MaxSize 
        self.size-=1 
    def isEmpty(self):
        return self.size == 0
    def isFull(self):
        return self.size == self.MaxSize 
    def display(self):
        print(self.array)
que = Queue(5)
que.enqueue(10)
que.enqueue(20)
que.display()
que.dequeue()
que.display()
que.enqueue(30)
que.enqueue(40)
que.enqueue(60)
que.display()
que.enqueue(80)
que.display()
que.dequeue()
que.enqueue(3)
que.display()
que.dequeue()
que.dequeue()
que.dequeue()
que.dequeue()
que.dequeue()
que.display()
que.dequeue()
