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


def Play(StartGame, board, boardSize, history):
    isPlaying = True
    turn = 0
    while isPlaying:
        playerTurnCheck = Players(StartGame)
        if playerTurnCheck == 202:
            toPrint(ErrorCodes.get(202))
            return
        print("")
        if playerTurnCheck[turn][0] == "C":
            toPrint("Computer's Turn")
            print("")
            ComputerTurn(board, boardSize, history)
            os.system("cls||clear")
            displayBoard(board)

        else:
            toPrint(f"Player Turn - {playerTurnCheck[turn][0]}")
            print("")
            check = PlayerTurn(playerTurnCheck, turn, board, history, boardSize)
            if check == "next":
                os.system("cls||clear")
                displayBoard(board)
            elif check == "quit":
                toPrint("Player " + playerTurnCheck[turn][0] + " left")
                isPlaying = False
                break

        win = (
            CheckWinner(board)or CheckWinnerColumn(board)
        )
        if win == True:
            if playerTurnCheck[turn][0] == "C":
                toPrint("Computer won")
            else:
                toPrint("Player " + playerTurnCheck[turn][0] + " won")
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
                UndoMove(StartGame, history, board, turn)
        if playerTurnCheck[turn][0] != "C" and isUndo == "n":
            if turn < len(playerTurnCheck) - 1:
                turn = turn + 1
            else:
                turn = 0
        else:
            if turn < len(playerTurnCheck) - 1:
                turn = turn + 1
            else:
                turn = 0
