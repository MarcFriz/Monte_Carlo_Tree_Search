import random as rnd
import copy


def play_randomly(board):
    value = board.three_in_a_row()
    counter = 0
    while value == 0:
        moves = board.list_moves()
        # print("moves = ", moves)
        if moves ==[]: return 0        
        random_nr = rnd.randint(0, len(moves)-1)
        random_move = moves[random_nr]
        # print("move is ", random_move)
        board.make_move(random_move)
        # print(board)
        value = board.three_in_a_row()
        counter += 1
    return value


def simulate_plays(board, number=100):
    assert number >= 1
    # Wins: Player, equals, KI
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


def evaluate_loss(board, move):
    b = copy.deepcopy(board)
    b.make_move(move)



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
    # if board.player == "O":
    #    return moves[max_idxO]

    return moves[max_idx]
