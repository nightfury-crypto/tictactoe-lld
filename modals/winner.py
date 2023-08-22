def CheckWinnerColumn(board):
    # Check for vertical win
    boardLen = len(board)
    i = 0
    colArr = []
    while i<boardLen:
        j = 0
        while j<boardLen:
            colArr.append(board[j][i])
            j = j + 1
        if len(set(colArr)) == 1 and colArr[0] != ' ':
            return True
        colArr = []
        i = i + 1
    return False

# checkWinner row and diagonal
def CheckWinner(board):
    boardLen = len(board)
    diagonal = set()
    antidiagonal = set()
    
    for i in range(boardLen):
        # for rows
        if len(set(board[i])) == 1 and board[i][0] != ' ':
            return True
        
        # for diagonal
        if board[i][i] not in diagonal:
            diagonal.add(board[i][i])
        
        # for antidiagonal
        if board[i][boardLen - i - 1] not in antidiagonal:
            antidiagonal.add(board[i][boardLen - i - 1])
    
    if len(diagonal) == 1 and ' ' not in diagonal:
        return True

    if len(antidiagonal) == 1 and ' ' not in antidiagonal:
        return True
    
    return False

