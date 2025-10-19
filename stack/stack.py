from libs import singleLinkedList

class stack:

    def __init__(self):
        self.data = singleLinkedList.singleLinkedList()

    
    def insertData(self,data):
        self.data.insert(data)

    def isEmpty(self):
        return self.data.is_empty()
    
    def popData(self):
        try:
            self.data.pop()
        except Exception as e:
            raise e 
    
    def peekData(self):
        try:
            return self.data.peek()
        except Exception as e:
            raise e 
    def Traveres(self):
        self.data._traverse()
    def indexData(self,data):
        return self.data.index(data)
