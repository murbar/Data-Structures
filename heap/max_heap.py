class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)

    def delete(self):
        pass

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        pass

    def _sift_down(self, index):
        pass

    def get_parent_index(self, index):
        p = (index - 1) // 2
        return p if p >= 0 else None

    def get_left_index(self, index):
        l = (index * 2) + 1
        return l if l < self.get_size else None

    def get_right_index(self, index):
        r = (index * 2) + 2
        return r if r < self.get_size else None

    def swap(self, index1, index2):
        self.storage[index1], self.storage[index2] = self.storage[index2], self.storage[index1]
