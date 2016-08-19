class DynamicArray():
    def __init__(self, max_size=32):
        self.max_size = max_size
        self.data = []
        self.cur = 0


    @property
    def length(self):
        return len(self.data)


    @property
    def is_max_length(self):
        return self.length >= self.max_size


    def append(self, data):
        if self.is_max_length:
            self.data[self.cur] = data
        else:
            self.data.append(data)
        self.cur = (self.cur + 1) % self.max_size


    def get(self):
        return self.data[self.cur:] + self.data[:self.cur]
 
    


if __name__ == '__main__':
    array = DynamicArray()
    for i in range(35):
        array.append(i)
    print(array.length)
    print(array.get())
