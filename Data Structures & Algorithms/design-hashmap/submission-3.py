class MyHashMap:

    def __init__(self):
        self.size=10000000
        self.array=[-1]*self.size

    def put(self, key: int, value: int) -> None:
        idx=key%self.size
        self.array[idx]=value

    def get(self, key: int) -> int:
        idx=key%self.size
        return self.array[idx]

    def remove(self, key: int) -> None:
        idx=key%self.size
        self.array[idx]=-1
  


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)