def handleColArr(colArr, board):
    boardLen = len(board)
    for i in range(boardLen):
        colArr.append([])
        for j in range(boardLen):
            colArr[i].append(" ")
    return colArr

def handlecross(cross, board):
    boardLen = len(board)
    for i in range(boardLen):
        cross.append(" ")
    return cross