class MyHashSet:

    def __init__(self, base=769):
        self.base = base
        self.buckets = [[] for _ in range(self.base)]
    def add(self, key: int) -> None:
        idx = key%self.base
        if key not in self.buckets[idx]:
            self.buckets[idx].append(key)

    def remove(self, key: int) -> None:
        idx = key%self.base
        if key in self.buckets[idx]:
            self.buckets[idx].remove(key)

    def contains(self, key: int) -> bool:
        return True if key in self.buckets[key%self.base] else False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)