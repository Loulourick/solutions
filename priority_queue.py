class PriorityQueue:
    def __init__(self):
        self._items = []
        self._order = 0

    def push(self, item, priority):
        self._items.append((priority, self._order, item))
        self._order += 1

    def _best_index(self):
        if self.is_empty():
            raise IndexError
        best = 0
        for i in range(1, len(self._items)):
            if self._items[i][0:2] < self._items[best][0:2]:
                best = i
        return best

    def pop(self):
        index = self._best_index()
        return self._items.pop(index)[2]

    def peek(self):
        return self._items[self._best_index()][2]

    def __len__(self):
        return len(self._items)

    def is_empty(self):
        return len(self._items) == 0

if __name__ == "__main__":
    er = PriorityQueue()
    er.push("порез пальца", 3)
    er.push("перелом", 2)
    er.push("остановка сердца", 1)
    er.push("ушиб", 3)
    er.peek()  # 'остановка сердца'
    er.pop()  # 'остановка сердца'
    er.pop()  # 'перелом'
    er.pop()  # 'порез пальца' - пришёл раньше ушиба
    len(er)  # 1