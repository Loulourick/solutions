class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    def prepend(self, data):
        node = Node(data)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def delete(self, data):
        c = self.head
        while c is not None:
            if c.data == data:
                if c.prev is None:
                    self.head = c.next
                else:
                    c.prev.next = c.next

                if c.next is None:
                    self.tail = c.prev
                else:
                    c.next.prev = c.prev
                return
            c = c.next

    def to_list(self):
        res = []
        c = self.head
        while c is not None:
            res.append(c.data)
            c = c.next
        return res

    def to_list_reverse(self):
        res = []
        c = self.tail
        while c is not None:
            res.append(c.data)
            c = c.prev
        return res


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.prepend(0)
    dll.to_list()  # [0, 1, 2, 3]
    dll.to_list_reverse()  # [3, 2, 1, 0]
    dll.head.data  # 0
    dll.tail.data  # 3
    dll.delete(2)
    dll.to_list()  # [0, 1, 3]
    dll.delete(3)  # удаляем хвост
    dll.tail.data  # 1
    dll.to_list_reverse()  # [1, 0]