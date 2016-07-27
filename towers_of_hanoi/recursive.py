### Object oriented, recursive


class Board():
    def __init__(self, biggest_piece):
        self.n = biggest_piece
        range_max = self.n + 1
        self.a = list(reversed(range(1, range_max)))
        self.b = []
        self.c = []


    def move_piece(self, n, source, target, aux):
        if n == 0:
            return
        else:
            self.move_piece(n - 1, source, aux, target)
            target.append(source.pop())
            self.move_piece(n - 1, aux, target, source)


    def printer(self):
        print("A:", self.a)
        print("B:", self.b)
        print("C:", self.c)
        print("-" * 20)



def main():
    biggest_piece = 4
    board = Board(biggest_piece)
    board.printer()
    board.move_piece(board.n, board.a, board.b, board.c)
    board.printer()



if __name__ == '__main__':
    main()