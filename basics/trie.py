class Trie():
    def __init__(self):
        self.root = Node(None)


    def add(self, data):
        if type(data) is not str:
            raise TypeError("Strings only!")
        current_node = self.root
        for char in data:
            next_node = next((node for node in current_node.children 
                                if node.value is char), None)
            if next_node is None:
                new_node = Node(char)
                current_node.children.add(new_node)
                current_node = new_node
            else:
                current_node = next_node


    def is_in_trie(self, data):
        current_node = self.root
        for char in data:
            current_node = next((node for node in current_node.children
                                    if node.value is char), None)
            if current_node is None:
                return False
        return True


class Node():
    def __init__(self, value):
        self.value = value
        self.children = set()


    def __iter__(self):
        for node in self.children:
            yield node.value


if __name__ == '__main__':
    trie = Trie()
    trie.add("Hello")
    print(trie.is_in_trie("Hello"))
    print(trie.is_in_trie("World"))   