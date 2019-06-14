class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        last_index = self.get_size() - 1
        self._bubble_up(last_index)

    def delete(self):
        size = self.get_size()

        if not size:
            return None

        if size == 1:
            return self.storage.pop()

        last_index = self.get_size() - 1
        self.swap(0, last_index)
        priority = self.storage.pop()
        self._sift_down(0)
        return priority

    def get_max(self):
        return self.storage[0] if self.get_size() > 0 else None

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        parent_index = self.get_parent_index(index)
        while parent_index is not None and (self.storage[parent_index] < self.storage[index]):
            self.swap(parent_index, index)
            parent_index = self.get_parent_index(parent_index)

    def _sift_down(self, index):
        left_index = self.get_left_index(index)
        while left_index:
            right_index = self.get_right_index(index)
            larger_child_index = left_index
            if right_index and self.storage[right_index] > self.storage[left_index]:
                larger_child_index = right_index

            if self.storage[larger_child_index] > self.storage[index]:
                self.swap(index, larger_child_index)
                left_index = self.get_left_index(larger_child_index)
            else:
                break

            # if not self.storage[larger_child_index] > self.storage[index]:
            #     break
            # else:
            #     self.swap(index, larger_child_index)

            # left_index = self.get_left_index(larger_child_index)

    def get_parent_index(self, index):
        p = (index - 1) // 2
        return p if p >= 0 else None

    def get_left_index(self, index):
        l = (index * 2) + 1
        return l if l < self.get_size() else None

    def get_right_index(self, index):
        r = (index * 2) + 2
        return r if r < self.get_size() else None

    def swap(self, index1, index2):
        self.storage[index1], self.storage[index2] = self.storage[index2], self.storage[index1]
