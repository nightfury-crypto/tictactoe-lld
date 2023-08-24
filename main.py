from modals.createboard import createBoard
from modals.displayboard import displayBoard
from modals.defineplayers import Players
from modals.errorcodes import ErrorCodes
from play import Play
import os
from modals.printStatement import toPrint
from modals.maintainArray import *

if __name__ == "__main__":
    os.system("cls||clear")
    while True:
        StartGame = input('''Total_Players playerID Symbol boardSize:
    eg. 2 u1 O u2 X 3 : ''').strip().split(" ")
        if StartGame[0].isdigit() and StartGame[len(StartGame) - 1].isdigit():
            break
        else:
            toPrint("Number of players and boardSize should be integer")
            continue
    validatePlayers = Players(StartGame)
    if type(validatePlayers) != type([]):
        if ErrorCodes.get(validatePlayers) != None:
            toPrint(ErrorCodes.get(validatePlayers))
            exit()
    else:
        if len(validatePlayers) != int(StartGame[0]):
            toPrint("Number of players and Number of playerID's are not matching")
            exit()
    boardSize = int(StartGame[len(StartGame) - 1])
    board = []
    history = []
    columnArr = []
    diagonalArr = []
    antiDiagonalArr = []
    
    createBoard(board, boardSize)
    handleColArr(columnArr, board)
    handlecross(diagonalArr, board)
    handlecross(antiDiagonalArr, board)
    displayBoard(board)
    Play(StartGame, board, boardSize, history, columnArr, diagonalArr, antiDiagonalArr)
