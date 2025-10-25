from decimal import Decimal
from math import floor , sqrt
from libs.SingleLinkedList import SingleLinkedList as sl
class HashTable:
    __A__ = Decimal((sqrt(5)-1) / 2) #golden Ratio Value
    def __init__(self,bucket_size):
        self.sizeof  = bucket_size
        self.buckets = [sl() for _ in range(self.sizeof)]
    def _hash(self,key):
        return floor(self.sizeof*((Decimal(key) * HashTable.__A__)%1))
    def insertData(self,value):
        index = self._hash(hash(value))
        self.buckets[index].insert(value)
    def searchData(self,value):
        index = self._hash(hash(value))
        result = self.buckets[index].search(value)
        if result:
            print('in the HashTable')
        else:
            print('not in the HashTable')
    def deleteData(self,value):
        try:
            index = self._hash(hash(value))
            self.buckets[index].deleted(value)
        except:
            print('deleted Opration Failed -- // --')
Da = HashTable(5)
Da.insertData(23)
Da.insertData(4)
Da.searchData(4)
Da.deleteData(4)
Da.deleteData(4)
Da.searchData(4)