class Deque:
    def __init__(self):
        self._capacity = 4
        self._buffer = [None] * self._capacity
        self._head = 0
        self._size = 0

    @property
    def capacity(self):
        return self._capacity

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _grow(self):
        new_capacity = self._capacity * 2
        new_buffer = [None] * new_capacity
        for i in range(self._size):
            new_buffer[i] = self._buffer[(self._head + i) % self._capacity]
        self._buffer = new_buffer
        self._capacity = new_capacity
        self._head = 0

    def push_back(self, item):
        if self._size == self._capacity:
            self._grow()
        tail = (self._head + self._size) % self._capacity
        self._buffer[tail] = item
        self._size += 1

    def push_front(self, item):
        if self._size == self._capacity:
            self._grow()
        self._head = (self._head - 1) % self._capacity
        self._buffer[self._head] = item
        self._size += 1

    def pop_back(self):
        if self.is_empty():
            raise IndexError
        tail = (self._head + self._size - 1) % self._capacity
        item = self._buffer[tail]
        self._buffer[tail] = None
        self._size -= 1
        return item

    def pop_front(self):
        if self.is_empty():
            raise IndexError
        item = self._buffer[self._head]
        self._buffer[self._head] = None
        self._head = (self._head + 1) % self._capacity
        self._size -= 1
        if self._size == 0:
            self._head = 0
        return item

    def back(self):
        if self.is_empty():
            raise IndexError
        tail = (self._head + self._size - 1) % self._capacity
        return self._buffer[tail]

    def front(self):
        if self.is_empty():
            raise IndexError
        return self._buffer[self._head]

if __name__ == "__main__":
    d = Deque()
    d.push_back(1)
    d.push_back(2)
    d.push_front(0)  # head уходит из ячейки 0 в ячейку 3
    d.front()  # 0
    d.back()  # 2
    d.pop_back()  # 2
    d.pop_front()  # 0
    len(d)  # 1
    for x in range(10):
        d.push_back(x)
    len(d)  # 11
    d.capacity  # 16