class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return len(self._items) == 0

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError
        return self._items[-1]

    def size(self):
        return len(self._items)

if __name__ == "__main__":
    s = Stack()
    s.is_empty()  # True
    s.push(1)
    s.push(2)
    s.push(3)
    s.size()  # 3
    s.peek()  # 3
    s.pop()  # 3
    s.pop()  # 2
    s.is_empty()  # False
