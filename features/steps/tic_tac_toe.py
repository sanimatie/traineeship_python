from behave import *
from tictactoe import EMPTY_BOARD, play, play_best_move
import logging

def convert_column_row(col, row):
    col = col -1
    row = row -1
    return col, row

@given(u'we have an empty tic-tac-toe board')
def step_impl(context):
    context.board = EMPTY_BOARD
    context.winner = None

@when(u'I play X on column {col} and row {row} on the board')
def step_impl(context, col, row):
    col_new, row_new = convert_column_row(int(col), int(row))
    context.board, context.winner = play(context.board, 'X', col_new, row_new)

@when(u'I ask the computer to do its best move for O')
def step_impl(context):
    context.board, context.winner = play_best_move(context.board, 'O')

@then(u'the board has a O in column 1 and row 1 on the board')
def step_impl(context):
    col_new, row_new = convert_column_row(1, 1)
    position_on_board = row_new * 3 + col_new 
    assert context.board[position_on_board] == 'O'

@then(u'the game will {uitkomst}')
def step_impl(context, uitkomst):
    if uitkomst == 'end with O as the winner':
        assert context.winner == 'O'
    elif uitkomst == 'end in a tie':
        assert context.winner == 'T'
    elif uitkomst == 'end with X as the winner':
        assert context.winner == 'X'
    elif uitkomst == 'continue':
        assert context.winner == None

