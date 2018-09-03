import Classes.Board as Board
import Classes.Monte_Carlo_Tree_Search as MCTS


def play(board):
    value = 0
    while value == 0:
        if board.three_in_a_row() == 1:
            print("KI Win!")
            return
        elif board.three_in_a_row() == 2:
            print("You Win!")
            return

        # KI turn
        best = MCTS.choose_best_move(board, 1000)
        print(best)
        board.make_move(best)
        print(board)

        if board.three_in_a_row() == 1:
            print("KI Win!")
            return
        elif board.three_in_a_row() == 2:
            print("You Win!")
            return

        # Player turn
        x = int(input("Ihr Zug: "))
        board.make_move(x)
        print(board)

        if board.three_in_a_row() == 1:
            print("KI Win!")
            return
        elif board.three_in_a_row() == 2:
            print("You Win!")
            return


print("Start")

board = Board.Board()
print(board)

play(board)


