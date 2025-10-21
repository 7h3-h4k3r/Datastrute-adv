from lib.node import node

class bin:

    def __init__(self):
        self.root = None

    def insert(self,value):
        if self.root is None:
            self.root = node(value)
            return 
        self.__insert__(self.root,value)
    
    def __insert__(self,current, value):

        if current.value < value:
            if current.right is None:
                current.right = node(value)
            else:
                self.__insert__(current.right,value)
        else:
            if current.left is None:
                current.left = node(value)
            else:
                self.__insert__(current.left,value)
        

    def display(self):
        self._display_recursive(self.root)

    def _display_recursive(self, current):
        if current:
            self._display_recursive(current.left)
            print(current.value, end=' ')
            self._display_recursive(current.right)
data = bin()
data.insert(10)
data.insert(4)
data.insert(342)
data.insert(34)
data.insert(2)
data.display()