class BinaryHeap:
    def __init__(self, inputlist=None):
        self._list = [0]
        self._size = 0
        if inputlist:
            self.build_heap(inputlist)

    def insert(self, value):
        self._list.append(value)
        self._size += 1
        self._perc_up(self._size)

    def _perc_up(self, i):
        parent_i = i // 2
        while parent_i > 0:
            if self._list[i] < self._list[parent_i]:
                self._list[i], self._list[parent_i] = (
                    self._list[parent_i], self._list[i])
            i = parent_i
            parent_i = i // 2

    def _perc_down(self, i):
        first_child_index = i * 2
        while first_child_index <= self._size:
            min_child_i = self._min_child(i)
            if self._list[i] > self._list[min_child_i]:
                self._list[min_child_i], self._list[i] = (
                    self._list[i], self._list[min_child_i])
            else:
                break
            i = min_child_i
            first_child_index = i * 2

    def _min_child(self, parent_i):
        first_child_i = parent_i * 2
        second_child_i = first_child_i + 1
        if second_child_i > self._size:
            return first_child_i
        else:
            if self._list[second_child_i] < self._list[first_child_i]:
                return second_child_i
            else:
                return first_child_i

    def get(self):
        min_value = self._list[1]
        self._list[1] = self._list.pop()
        self._size -= 1
        self._perc_down(1)
        return min_value

    def build_heap(self, values):
        new_values = list(values)
        self._size = len(new_values)
        i = self._size // 2
        self._list = [0] + new_values
        while i > 0:
            self._perc_down(i)
            i -= 1

    def __str__(self):
        index = 1
        count = 2
        retval = ''
        while index <= self._size:
            retval += (str(self._list[index:count]) + '\n')
            index = count
            count = index * 2
        return retval


if __name__ == '__main__':
    heap = BinaryHeap()
    #for i in [1,6,3,10,323,32,3,2,55,1200,15]:
    #    heap.insert(i)
    heap.build_heap([2, 30, 1, 4])
    print(heap._list)
    print(heap)
