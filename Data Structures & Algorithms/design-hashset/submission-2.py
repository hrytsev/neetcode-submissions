class MyHashSet:

    def __init__(self):
        self.storage={}

    def add(self, key: int) -> None:
        self.storage[key]=True
    def remove(self, key: int) -> None:
        if self.contains(key):
            del self.storage[key]

    def contains(self, key: int) -> bool:
        return self.storage.get(key,False)


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)