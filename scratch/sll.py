class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return repr(self.value)


class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def __repr__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(repr(current))
            current = current.next
        return '[' + ', '.join(nodes) + ']'

    def append(self, value):
        if not self.head:
            # empty list, set value to head
            self.head = Node(value)
            return

        current = self.head
        while current.next:
            # go to end of the list
            current = current.next
        # set value to new end
        current.next = Node(value)

    def prepend(self, value):
        # if list is empty, next will be None
        new_head = Node(value, self.head)
        self.head = new_head

    def remove(self, value):
        if not self.head:
            return

        if self.head.value == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next


sll = SinglyLinkedList()

sll.append(5)
sll.append(56)
sll.append(3)
sll.append(84)
sll.append(20)

print(sll)
sll.prepend(45)
print(sll)
sll.remove(3)
print(sll)
