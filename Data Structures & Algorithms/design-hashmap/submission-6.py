import math
class MyHashMap:

    def __init__(self):
        self.size=1000
        self.array=[-1]*self.size

    def put(self, key: int, value: int) -> None:
        idx=self.hash_fn(key)
        self.array[idx]=value

    def get(self, key: int) -> int:
        idx=self.hash_fn(key)
        return self.array[idx]

    def remove(self, key: int) -> None:
        idx=self.hash_fn(key)
        self.array[idx]=-1
    def hash_fn(self,key):
        return int(abs(math.cos(key)*(self.size//2)))


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)