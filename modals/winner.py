def CheckDiagonalWinner(diagonal):
    if len(set(diagonal)) == 1 and diagonal[0] != ' ':
        return True

def CheckRowWinner(board, coordinates):
    posI = coordinates["IndexI"]
    if len(set(board[posI])) == 1 and board[posI][0] != ' ':
        return True
    
def CheckColumnWinner(coordinates, columnArr):
    posJ = coordinates["IndexJ"]
    if len(set(columnArr[posJ])) == 1 and columnArr[posJ][0] != ' ':
        return True
    
def CheckAntiDiagonalWinner(antiDiagonalArr):
    if len(set(antiDiagonalArr)) == 1 and antiDiagonalArr[0] != ' ':
        return True
