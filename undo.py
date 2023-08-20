def UndoMove(StartGame, history, board, turn):
    ptemp = StartGame[1 : len(StartGame) - 1]
    if len(history) == 0:
        return "no moves to undo"
    board[history[len(history)-1][0]][history[len(history)-1][1]] = " "
    history.pop()
    if turn == 0:
        turn = len(ptemp)-1
    else:
        turn = turn - 1
    return turn
