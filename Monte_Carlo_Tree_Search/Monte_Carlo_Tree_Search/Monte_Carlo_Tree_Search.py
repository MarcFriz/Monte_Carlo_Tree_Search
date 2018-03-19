import random as rnd
import copy

print("Start")

class Board(object):
    
    def __init__(self):
        self.board = [".",".", ".",".",".", ".",".",".", "."]
        self.player = "X"

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
        for i in range(0,9):
            if self.board[i] == ".":
                moves.append(i)
        return moves

    def make_move(self, pos):
        if pos in self.list_moves():
            self.board[pos] = self.player
            self.player_change()
            self.last_move = pos

    def three_in_a_row(self):
        
        if (self.board[3] == "X" and self.board[4] == "X" and self.board[5] == "X") or (self.board[1] == "X" and self.board[4] == "X" and self.board[7] == "X") or (self.board[0] == "X" and self.board[1] == "X" and self.board[2] == "X") or ((self.board[6] == "X" and self.board[7] == "X" and self.board[8] == "X")) or ((self.board[0] == "X" and self.board[3] == "X" and self.board[6] == "X")) or (self.board[2] == "X" and self.board[5] == "X" and self.board[8] == "X") or (self.board[0] == "X" and self.board[4] == "X" and self.board[8] == "X") or (self.board[2] == "X" and self.board[4] == "X" and self.board[6] == "X"):
            return 1
        elif (self.board[3] == "O" and self.board[4] == "O" and self.board[5] == "O") or (self.board[1] == "O" and self.board[4] == "O" and self.board[7] == "O") or (self.board[0] == "O" and self.board[1] == "O" and self.board[2] == "O") or ((self.board[6] == "O" and self.board[7] == "O" and self.board[8] == "O")) or ((self.board[0] == "O" and self.board[3] == "O" and self.board[6] == "O")) or (self.board[2] == "O" and self.board[5] == "O" and self.board[8] == "O") or (self.board[0] == "O" and self.board[4] == "O" and self.board[8] == "O") or (self.board[2] == "O" and self.board[4] == "O" and self.board[6] == "O"):
            return -1
        else:
            return 0

    def undo_move(self):
        self.board[self.last_move] = "."
        self.player_change()

    pass


def play_randomly(board):
    value = board.three_in_a_row()
    while value == 0:
        moves = board.list_moves()
        #print("moves = ", moves)
        if moves ==[]: return 0        
        random_Nr = rnd.randint(0, len(moves)-1)
        random_move = moves[random_Nr]
        #print("move is ", random_move)
        board.make_move(random_move)
        #print(board)
        value = board.three_in_a_row()
    return value

def simulate_plays(board, number=100):
    assert number >= 1
    count = [0,0,0]
    while number > 0:
        b = copy.deepcopy(board)
        count[play_randomly(b)+1] += 1
        number -= 1
    return count

def evaluate_moves(board, number=100):
    assert number >=1
    moves = board.list_moves()
    values = []
    for move in moves:
        board.make_move(move)
        values += [simulate_plays(board, number)]
        board.undo_move()
    return values

def choose_best_move(board, number=100):
    assert number >= 1 and board.list_moves() != []
    moves = board.list_moves()

    board_value = evaluate_moves(board, number)
    print(board_value)        

    values = [x for o,p,x in board_value]
    valuesO = [o for o,p,x in board_value]

    max_val = max(values)
    max_idx = values.index(max_val)

    #max_valO = max(valuesO)
    #max_idxO = valuesO.index(max_valO)

    if board.player == "X":
        return moves[max_idx]
    #if board.player == "O":
    #    return moves[max_idxO]

    return moves[max_idx]








b = Board()
print(b)
#print(b.list_moves())
#play_randomly(b)
#print(simulate_plays(Board(), 1000))
#print(evaluate_moves(Board()))
#print(choose_best_move(Board(), 100))

#best = choose_best_move(b, 100)
#print(best)
#b.make_move(best)
#print(b)

value = 0
while value == 0:
    value = b.three_in_a_row()
    best = choose_best_move(b, 1000)
    print(best)
    b.make_move(best)
    print(b)
    value = b.three_in_a_row()


#print(choose_best_move(Board(), 100))
#print(choose_best_move(Board(), 100))
#print(choose_best_move(Board(), 100))
#print(choose_best_move(Board(), 100))
#print(choose_best_move(Board(), 100))
#print(choose_best_move(Board(), 100))
#print(choose_best_move(Board(), 100))
#print(choose_best_move(Board(), 100))