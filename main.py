from modals.createboard import createBoard
from modals.displayboard import displayBoard
from modals.defineplayers import Players
from modals.errorcodes import ErrorCodes
from play import Play
import os

if __name__ == "__main__":
    os.system("cls||clear")
    while True:
        StartGame = input('''Total_Players playerID Symbol boardSize:
    eg. 2 u1 O u2 X 3 : ''').strip().split(" ")
        if StartGame[0].isdigit() and StartGame[len(StartGame) - 1].isdigit():
            break
        else:
            print("=========================================================")
            print("Number of players and boardSize should be integer")
            print("=========================================================")
            continue
    validatePlayers = Players(StartGame)
    if type(validatePlayers) != type([]):
        if ErrorCodes.get(validatePlayers) != None:
            print("=========================================================")
            print(ErrorCodes.get(validatePlayers))
            print("=========================================================")
            exit()
    else:
        if len(validatePlayers) != int(StartGame[0]):
            print("=========================================================")
            print("Number of players and Number of playerID's are not matching")
            print("=========================================================")
            exit()
    boardSize = int(StartGame[len(StartGame) - 1])
    board = []
    history = []
    createBoard(board, boardSize)
    displayBoard(board)
    Play(StartGame, board, boardSize, history)
