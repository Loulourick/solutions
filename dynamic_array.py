class DynamicArray:
    def __init__(self):
        self.size = 0
        self._capacity = 4
        self.data = [None] * self._capacity

    @property
    def capacity(self): return self._capacity

    def append(self, item):
        if self.size == self._capacity:
            up = [None] * (2 * self._capacity)
            for i in range(self.size):
                up[i] = self.data[i]
            self.data = up
        self.data[self.size] = item
        self.size += 1

    def pop(self):
        if self.size == 0: raise IndexError

        self.size -= 1
        item = self.data[self.size]
        self.data[self.size] = None
        return item

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __len__(self): return self.size

if __name__ == "__main__":
    a = DynamicArray()
    a.capacity        # 4
    for x in range(5):
        a.append(x * 10)
    len(a)            # 5
    a.capacity        # 8 - пятому элементу не хватило места
    a[4]              # 40
    a[1] = 99
    a[1]              # 99
    a.pop()           # 40
    len(a)            # 4
    a.capacity        # 8
    a[4]              # IndexError - ячейка есть, но элемента в ней нет