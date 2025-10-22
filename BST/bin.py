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

    def __postorder__(self,current):
        if current:
            self.__postorder__(current.left)
            self.__postorder__(current.right)
            print(current.value,end=' ')

    def __inOrder__(self,current):
        if current:
            self.__inOrder__(current.left)
            print(current.value,end=' ')
            self.__inOrder__(current.right)
    def __preorder__(self,current):
        if current:
            print(current.value,end=' ')
            self.__preorder__(current.left)
            self.__preorder__(current.right)

    def __findone__(self,target,root):
        if root is None:
            return None 
        if root.value == target:
            return True 
        elif root.value < target:
            self.__findone__(target ,root.right)
        else:
            self.__findone__(target,root.left)
        

        return False
    def search(self,target):
        result = self.__findone__(target,self.root)
        if result:
            print("Target founded on the BinaryTres")
        else:
            print("Target Not found in this BinaryTree")

    def iterate(self,order=None):
        if order is None:
            print('Pre-Order')
            self.__preorder__(self.root)
            print('\n')
        elif order  == True:
            print('Post-Order')
            self.__postorder__(self.root)
            print('\n')
        else:
            print('In-Order')
            self.__inOrder__(self.root)
            print('\n')
data = bin()
data.insert(10)
data.insert(9)
data.insert(5)
data.insert(4)
data.insert(3)
data.insert(7)
data.insert(342)
data.insert(34)
data.iterate()
data.iterate(False)
data.iterate(True)
data.search(443)