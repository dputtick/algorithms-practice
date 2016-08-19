class LinkedList():
    def __init__(self):
        self.head = None
        self.length = 0


    def prepend_node(self, data):
        if not self.head:
            self.head = Node(data)
        elif self.head:
            old_head = self.head
            self.head = Node(data)
            self.head.next = old_head
        self.length += 1


    def append_node(self, data):
        if not self.head:
            self.head = Node(data)
            self.length += 1
        elif self.head:
            current = self.head
            for _ in range(self.length):
                if current.next == None:
                    current.next = Node(data)
                    self.length += 1
                    break
                else:
                    current = current.next
            

    def left_pop(self):
        if self.head:
            old_head = self.head
            self.head = old_head.next
            self.length -= 1
            return old_head
        else:
            return None


    def right_pop(self):
        if self.head:
            current = self.head
            next_node = current.next
            for _ in range(self.length):
                if next_node.next == None:
                    current.next = None
                    return next_node
                    self.length -= 1


# FUN EXTRA STUFF

    def search(self, data):
        index = 0
        if self.head:
            current = self.head
            while True:
                if current.data == data:
                    return current
                else:
                    if current.next:
                        current = current.next
                    else:
                        return None


    def __str__(self):
        s = "["
        for node in self:
            s += node.data
            if node.next is not None:
                s += ", "
        s += "]"
        return s


    def __iter__(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None




if __name__ == '__main__':
    mylist = LinkedList()
    for x in mylist:
        print(x)
    mylist.prepend_node("World")
    mylist.prepend_node("Hello")
    mylist.append_node(("!"))
    for x in mylist:
        print(x.data)
    print(mylist)