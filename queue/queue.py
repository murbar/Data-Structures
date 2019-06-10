class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, node):
        self.next_node = node

    def set_value(self, value):
        self.value = value


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, item):
        node = Node(item)

        if not self.head and not self.tail:
            self.head = node
            self.tail = node
        else:
            self.tail.set_next(node)
            self.tail = node

    def dequeue(self):
        if not self.head and not self.tail:
            return None

        if self.head is self.tail:
            item = self.head.get_value()
            self.head = None
            self.tail = None
            return item

        new_head = self.head.get_next()
        item = self.head.get_value()
        self.head = new_head
        return item

    def len(self):
        if not self.head and not self.tail:
            return 0

        if self.head is self.tail:
            return 1

        n = 1
        element = self.head
        while element.get_next():
            n += 1
            element = element.get_next()
        return n
