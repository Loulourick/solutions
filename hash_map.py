class HashMap:
    def __init__(self, size=10):
        if not isinstance(size, int) or size <= 0:
            raise ValueError
        self.size = size
        self.buckets = [[] for _ in range(size)]
        self._length = 0

    def _index(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        bucket = self.buckets[self._index(key)]
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return
        bucket.append([key, value])
        self._length += 1

    def get(self, key):
        bucket = self.buckets[self._index(key)]
        for stored_key, value in bucket:
            if stored_key == key:
                return value
        raise KeyError(key)

    def remove(self, key):
        bucket = self.buckets[self._index(key)]
        for index, pair in enumerate(bucket):
            if pair[0] == key:
                del bucket[index]
                self._length -= 1
                return
        raise KeyError(key)

    def contains(self, key):
        bucket = self.buckets[self._index(key)]
        return any(stored_key == key for stored_key, _ in bucket)

    def __len__(self):
        return self._length

if __name__ == "__main__":
    m = HashMap()
    m.put("яблоко", 50)
    m.put("груша", 70)
    m.put("яблоко", 55)  # ключ уже есть - значение заменяется
    len(m)  # 2
    m.get("яблоко")  # 55
    m.contains("слива")  # False
    m.remove("груша")
    m.get("груша")  # KeyError
    m.put("пусто", None)
    m.contains("пусто")  # True - значение None, но ключ есть