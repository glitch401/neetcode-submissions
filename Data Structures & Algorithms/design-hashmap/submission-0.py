class MyHashMap:

    def __init__(self, base=769):
        self.base = base
        self.buckets = [[] for _ in range(self.base)]

    def _hash(self, key:int)->int:
        return key%self.base

    def put(self, key: int, value: int) -> None:
        idx = self._hash(key)
        bucket = self.buckets[idx]
        for pair in bucket:
            if pair[0]==key:
                pair[1]=value
                return
        bucket.append([key, value])

    def get(self, key: int) -> int:
        idx = self._hash(key)
        bucket = self.buckets[idx]

        # Return value if key is found
        for pair in bucket:
            if pair[0] == key:
                return pair[1]

        return -1

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        bucket = self.buckets[idx]

        # Find and remove the pair if it exists
        for i, pair in enumerate(bucket):
            if pair[0] == key:
                del bucket[i]
                return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)