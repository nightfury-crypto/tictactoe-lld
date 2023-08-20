def createBoard(board, boardSize):
    for i in range(0, boardSize):
        board.append([])
        for j in range(0, boardSize):
            board[i].append(" ")