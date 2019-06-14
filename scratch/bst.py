class BinarySearchTree:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert(self, value):
        if value <= self.data:
            if self.left == None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    def contains(self, value):
        if self.data == value:
            return True
        elif value < self.data:
            if self.left == None:
                return False
            else:
                return self.left.contains(value)

        else:
            if self.right == None:
                return False
            else:
                return self.right.contains(value)

    def print_in_order(self):
        # left -> root -> right
        if self.left:
            self.left.print_in_order()

        print(self.data)

        if self.right:
            self.right.print_in_order()


bst = BinarySearchTree(5)

bst.insert(56)
bst.insert(34)
bst.insert(3)
bst.insert(87)
bst.insert(20)

print(bst.contains(3))

bst.print_in_order()
