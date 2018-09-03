class Board(object):

    def __init__(self):
        self.board = [".", ".", ".", ".", ".", ".", ".", ".", "."]
        self.player = "O"

    def __str__(self):
        output = str(self.board[0]) + "  " + str(self.board[1]) + "  " + str(self.board[2]) + "\n"
        output = output + str(self.board[3]) + "  " + str(self.board[4]) + "  " + str(self.board[5]) + "\n"
        output = output + str(self.board[6]) + "  " + str(self.board[7]) + "  " + str(self.board[8]) + "\n"
        return output

    def player_change(self):
        if self.player == "X":
            self.player = "O"
        else:
            self.player = "X"

    def list_moves(self):
        moves = []
        for i in range(0, 9):
            if self.board[i] == ".":
                moves.append(i)
        return moves

    def make_move(self, pos):
        if pos in self.list_moves():
            self.board[pos] = self.player
            self.player_change()
            self.last_move = pos

    def three_in_a_row(self):

        if (self.board[3] == "X" and self.board[4] == "X" and self.board[5] == "X") or \
                (self.board[1] == "X" and self.board[4] == "X" and self.board[7] == "X") \
                or (self.board[0] == "X" and self.board[1] == "X" and self.board[2] == "X") \
                or ((self.board[6] == "X" and self.board[7] == "X" and self.board[8] == "X")) \
                or ((self.board[0] == "X" and self.board[3] == "X" and self.board[6] == "X")) \
                or (self.board[2] == "X" and self.board[5] == "X" and self.board[8] == "X") \
                or (self.board[0] == "X" and self.board[4] == "X" and self.board[8] == "X") \
                or (self.board[2] == "X" and self.board[4] == "X" and self.board[6] == "X"):
            return 1
        elif (self.board[3] == "O" and self.board[4] == "O" and self.board[5] == "O") \
                or (self.board[1] == "O" and self.board[4] == "O" and self.board[7] == "O") \
                or (self.board[0] == "O" and self.board[1] == "O" and self.board[2] == "O") \
                or ((self.board[6] == "O" and self.board[7] == "O" and self.board[8] == "O")) \
                or ((self.board[0] == "O" and self.board[3] == "O" and self.board[6] == "O")) \
                or (self.board[2] == "O" and self.board[5] == "O" and self.board[8] == "O") \
                or (self.board[0] == "O" and self.board[4] == "O" and self.board[8] == "O") \
                or (self.board[2] == "O" and self.board[4] == "O" and self.board[6] == "O"):
            return -1
        else:
            return 0

    def undo_move(self):
        self.board[self.last_move] = "."
        self.player_change()