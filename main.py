from createboard import createBoard
from displayboard import displayBoard
from defineplayers import Players
from errorcodes import ErrorCodes
from play import Play
import os

if __name__ == "__main__":
    os.system("cls||clear")
    StartGame = input('''Total_Players playerID Symbol boardSize:
eg. 2 u1 O u2 X 3 : ''').strip().split(" ")
    validatePlayers = Players(StartGame)
    if type(validatePlayers) != type([]):
        if ErrorCodes.get(validatePlayers) != None:
            print(ErrorCodes.get(validatePlayers))
            exit()
    else:
        if len(validatePlayers) != int(StartGame[0]):
            print("Number of players and Number of playerID's are not matching")
            exit()
    boardSize = int(StartGame[len(StartGame) - 1])
    board = []
    history = []
    createBoard(board, boardSize)
    displayBoard(board)
    Play(StartGame, board, boardSize, history)