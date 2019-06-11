"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        if not self.head:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
            self.length = 1
            return

        self.head.insert_before(value)
        self.head = self.head.prev
        self.length += 1

    def remove_from_head(self):
        if not self.head:
            return None

        if not self.head.next:
            # head is the only element in the list
            value = self.head.value
            self.head = None
            self.tail = None
            self.length = 0
            return value

        head = self.head
        value = head.value
        self.head = head.next
        head.delete()
        self.length -= 1
        return value

    def add_to_tail(self, value):
        if not self.head:
            self.add_to_head(value)
        else:
            self.tail.insert_after(value)
            self.tail = self.tail.next
            self.length += 1

    def remove_from_tail(self):
        if not self.head:
            return None

        if not self.tail.prev:
            # only 1 element in the list
            return self.remove_from_head()

        tail = self.tail
        value = tail.value
        self.tail = tail.prev
        tail.delete()
        self.length -= 1
        return value

    def move_to_front(self, node):
        value = node.value
        self.delete(node)
        self.add_to_head(value)

    def move_to_end(self, node):
        value = node.value
        self.delete(node)
        self.add_to_tail(value)

    def delete(self, node):
        if self.length == 1:
            self.head = None
            self.tail = None
        elif node is self.head:
            self.head = self.head.next
            node.delete()
        elif node is self.tail:
            self.tail = self.tail.prev
            node.delete()
        else:
            node.delete()

        self.length -= 1

    def get_max(self):
        if not self.head:
            return None

        current = self.head
        max = current.value
        while current.next:
            next_value = current.next.value
            if next_value > max:
                max = next_value
            current = current.next

        return max
