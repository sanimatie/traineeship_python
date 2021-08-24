from tictactoe import EMPTY_BOARD, play, play_best_move

board = EMPTY_BOARD #clear the tictactoe board
winner = None #set the winner to None

def twee_spelers(board, winner):
    board, winner = play(board, 'X', 1, 1) # winner == None
    board, winner = play(board, 'O', 0, 0) # winner == None
    board, winner = play(board, 'X', 1, 0) # winner == None
    board, winner = play(board, 'O', 0, 2) # winner == None
    board, winner = play(board, 'X', 1, 2) # winner == X
    return winner

def speel_tegen_computer(board, winner):
    board, winner = play(board, 'X', 1, 1) # take middle position
    board, winner = play_best_move(board, 'O') # computer sets somewhere

    if board[6] == None:
        board, winner = play(board, 'X', 0, 2) # take bottom left
    else:
        board, winner = play(board, 'X', 2, 2) # take top right
    return winner
    # complete rest of gameplay here