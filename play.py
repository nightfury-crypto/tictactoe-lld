import os
from modals.draw import CheckDraw
from modals.playerturn import PlayerTurn
from modals.computerturn import ComputerTurn
from modals.displayboard import displayBoard
from modals.defineplayers import Players
from modals.winner import *
from modals.undo import UndoMove
from modals.errorcodes import ErrorCodes
from modals.printStatement import toPrint


def Play(StartGame, board, boardSize, history, columnArr, diagonalArr, antiDiagonalArr):
    isPlaying = True
    turn = 0
    while isPlaying:
        playerTurnCheck = Players(StartGame)
        if playerTurnCheck == 202:
            toPrint(ErrorCodes.get(202))
            return
        print("")
        if playerTurnCheck[turn][0] == "C":
            os.system("cls || clear")
            toPrint("Computer's Turn")
            print("")
            coordinates = ComputerTurn(board, boardSize, history, columnArr, diagonalArr, antiDiagonalArr)
            displayBoard(board)

        else:
            toPrint(f"Player Turn - {playerTurnCheck[turn][0]}")
            print("")
            coordinates = PlayerTurn(
                playerTurnCheck, turn, board, history, boardSize, columnArr, diagonalArr, antiDiagonalArr
            )
            if coordinates == "quit":
                toPrint(f"Player {playerTurnCheck[turn][0]} left")
                isPlaying = False
                break

        os.system("cls || clear")
        displayBoard(board)
        win = CheckRowWinner(board, coordinates) or CheckColumnWinner(coordinates, columnArr) or CheckDiagonalWinner(diagonalArr) or CheckAntiDiagonalWinner(antiDiagonalArr)
        if win == True:
            if playerTurnCheck[turn][0] == "C":
                toPrint(f'Computer - {coordinates["Symbol"]} won')
            else:
                toPrint(f'Player {playerTurnCheck[turn][0]} - {coordinates["Symbol"]} won')
            isPlaying = False
            break
        if CheckDraw(history, boardSize) == True:
            toPrint("It's a Draw. No one won")
            isPlaying = False
            break
        if playerTurnCheck[turn][0] != "C":
            isUndo = input("Whether u want to undo the move? (y/n) : ")
            while isUndo != "y" and isUndo != "n":
                toPrint("Enter valid input")
                isUndo = input("Whether u want to undo the move? (y/n) : ")
            if isUndo == "y":
                toPrint("Undoing the move")
                checkUndo = UndoMove(StartGame, history, board, turn, columnArr, diagonalArr, antiDiagonalArr)
                if checkUndo != "None":
                    os.system("cls || clear")
                    displayBoard(board)
        os.system("cls || clear")
        displayBoard(board)
        if playerTurnCheck[turn][0] == "C" or isUndo == "n":
            if turn < len(playerTurnCheck) - 1:
                turn = turn + 1
            else:
                turn = 0
