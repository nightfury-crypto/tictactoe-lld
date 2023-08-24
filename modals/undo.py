from modals.displayboard import displayBoard
import os

def UndoMove(StartGame, history, board, turn, columnArr, diagonalArr, antiDiagonalArr):
    ptemp = StartGame[1 : len(StartGame) - 1]

    index_i = history[len(history)-1][0]
    index_j = history[len(history)-1][1]
    if index_i == index_j:
        diagonalArr[index_i] = " "
    if index_i + index_j == len(board) - 1:
        antiDiagonalArr[len(board) - 1 - index_i] = " "
    columnArr[index_j][index_i] = " "
    board[index_i][index_j] = " "
    history.pop()
    if turn == 0:
        turn = len(ptemp)-1
    else:
        turn = turn - 1
    return turn
