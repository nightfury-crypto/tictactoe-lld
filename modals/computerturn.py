import random


def ComputerTurn(board, boardSize, history, columnArr, diagonalArr, antiDiagonalArr):
    while True:
        rani, ranj = random.randint(0, boardSize - 1), random.randint(0, boardSize - 1)
        if board[rani][ranj] == " ":
            board[rani][ranj] = "C"
            history.append([rani, ranj])
            if (rani == ranj):
                diagonalArr[rani] = "C"
            if (rani + ranj == boardSize - 1):
                antiDiagonalArr[boardSize-1-rani] = "C"
            columnArr[ranj][rani] = "C"
            return {"IndexI": rani, "IndexJ": ranj, "Symbol": "C"}
