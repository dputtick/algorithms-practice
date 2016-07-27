### Object oriented, recursive


class Board():
    def __init__(self, biggest_piece):
        self.n = biggest_piece
        range_max = self.n + 1
        self.solution_list = list(reversed(range(1, range_max)))
        self.a = list(self.solution_list)
        self.b = []
        self.c = []


    def move_piece(self, n):
        a, b, c = self.a, self.b, self.c
        if n % 2 == 0:
            moves = {1: (a, b): (a, c), (b, c)]
            #even solution
            while c != self.solution_list:
                if check_legal_move(a, b):
                    move_piece(a, b)
                if check_legal_move(a, c):
                    move_piece(a, c)
                if check_legal_move(b, c):
                    move_piece(b, c)
        elif n % 2 == 1:
            #odd solution
            pass


    def printer(self):
        print("A:", self.a)
        print("B:", self.b)
        print("C:", self.c)
        print("-" * 20)



def main():
    biggest_piece = 4
    board = Board(biggest_piece)
    board.printer()
    board.move_piece(board.n)
    board.printer()


def check_legal_move(list_1, list_2):
    if list_1:
        if not list_2:
            return True
        if list_1[-1] < list_2[-1]:
            return True
        else:
            return False

def move_piece(list_1, list_2):
    list_2.append(list_1.pop())


if __name__ == '__main__':
    main()