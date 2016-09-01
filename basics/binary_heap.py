class BinaryHeap:
    def __init__(self, inputlist=None):
        self.heap_list = [0]
        self.current_size = 0
        if inputlist:
            self.build_heap(inputlist)

    def insert(self, value):
        self.heap_list.append(value)
        self.current_size += 1
        self._perc_up(self.current_size)

    def _perc_up(self, curr_index):
        parent_index = curr_index // 2
        while parent_index > 0:
            if self.heap_list[curr_index] < self.heap_list[parent_index]:
                self.heap_list[curr_index], self.heap_list[parent_index] = (
                    self.heap_list[parent_index], self.heap_list[curr_index])
            curr_index = parent_index
            parent_index = curr_index // 2

    def _perc_down(self, curr_index):
        first_child_index = curr_index * 2
        while first_child_index <= self.current_size:
            i_of_min_child = self._min_child(curr_index)
            if self.heap_list[curr_index] > self.heap_list[i_of_min_child]:
                self.heap_list[i_of_min_child], self.heap_list[curr_index] = (
                self.heap_list[curr_index], self.heap_list[i_of_min_child])
            else:
                break
            curr_index = i_of_min_child
            first_child_index = curr_index * 2

    def _min_child(self, parent_i):
        first_child_i = parent_i * 2
        second_child_i = first_child_i + 1
        if second_child_i > self.current_size:
            return first_child_i
        else:
            if self.heap_list[second_child_i] < self.heap_list[first_child_i]:
                return second_child_i
            else:
                return first_child_i

    def get(self):
        min_value = self.heap_list[1]
        self.heap_list[1] = self.heap_list.pop()
        self.current_size -= 1
        self._perc_down(1)
        return min_value

    def build_heap(self, values):
        new_values = list(values)
        self.current_size = len(new_values)
        curr_index = self.current_size // 2
        self.heap_list = [0] + new_values
        while curr_index > 0:
            self._perc_down(curr_index)
            curr_index -= 1

    def __str__(self):
        index = 1
        count = 2
        retval = ''
        while index <= self.current_size:
            retval += (str(self.heap_list[index:count]) + '\n')
            index = count
            count = index * 2
        return retval


if __name__ == '__main__':
    heap = BinaryHeap()
    #for i in [1,6,3,10,323,32,3,2,55,1200,15]:
    #    heap.insert(i)
    heap.build_heap([2, 30, 1, 4])
    print(heap.heap_list)
    print(heap)
