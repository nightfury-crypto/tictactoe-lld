import random


def ComputerTurn(board, boardSize, history):
    while True:
        rani, ranj = random.randint(0, boardSize - 1), random.randint(0, boardSize - 1)
        if board[rani][ranj] == " ":
            board[rani][ranj] = "C"
            history.append([rani, ranj])
            break
