def CheckWinnerRow(board):
    # Check for horizontal win
    boardLen = len(board)
    arr = []
    i = 0
    while i<boardLen:
        if len(set(board[i])) == 1 and board[i][0] != ' ':
            return True
        i = i + 1
    return False

def CheckWinnerColumn(board):
    # Check for vertical win
    boardLen = len(board)
    colArr = []
    i = 0
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

def CheckWinnerDiagonal(board):
    # Check for diagonal win
    boardLen = len(board)
    diagonal = set()
    antidiagonal = set()
    i = 0
    while i<boardLen:
        if board[i][i] not in diagonal:
            diagonal.add(board[i][i])
        
    # antidiagonal
        if board[i][boardLen - i - 1] not in antidiagonal:
            antidiagonal.add(board[i][boardLen - i - 1])
        
        i = i + 1
    if len(diagonal) == 1 and  diagonal.issuperset(" ") == False:
        return True

    if len(antidiagonal) == 1 and  antidiagonal.issuperset(" ") == False:
        return True

    return False