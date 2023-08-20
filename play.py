import os
from draw import CheckDraw
from playerturn import PlayerTurn
from computerturn import ComputerTurn
from displayboard import displayBoard
from defineplayers import Players
from winner import *
from undo import UndoMove


def Play(StartGame, board, boardSize, history):
    isPlaying = True
    turn = 0
    while isPlaying:
        playerTurnCheck = Players(StartGame)
        if playerTurnCheck == "No 2 Computers allowed":
            print("==================================")
            print(playerTurnCheck)
            print("==================================")
            return
        print("")
        if playerTurnCheck[turn][0] == "C":
            print("==================================")
            print("Computer's Turn")
            print("==================================")
            print("")
            ComputerTurn(board, boardSize, history)
            os.system("cls||clear")
            displayBoard(board)

        else:
            print("==================================")
            print(f"Player Turn - {playerTurnCheck[turn][0]}")
            print("==================================")
            print("")
            check = PlayerTurn(playerTurnCheck, turn, board, history, boardSize)
            if check == "next":
                os.system("cls||clear")
                displayBoard(board)
            elif check == "quit":
                print("==================================")
                print("Player " + playerTurnCheck[turn][0] + " left")
                print("==================================")
                isPlaying = False
                break

        win = (
            CheckWinnerRow(board)
            or CheckWinnerDiagonal(board)
            or CheckWinnerColumn(board)
        )
        if win == True:
            if playerTurnCheck[turn][0] == "C":
                print("==================================")
                print("Computer won")
                print("==================================")
            else:
                print("==================================")
                print("Player " + playerTurnCheck[turn][0] + " won")
                print("==================================")
            isPlaying = False
            break
        if CheckDraw(history, boardSize) == True:
            print("==================================")
            print("It's a Draw. No one won")
            print("==================================")
            isPlaying = False
            break
        if playerTurnCheck[turn][0] != "C":
            isUndo = input("Whether u want to undo the move? (y/n) : ")
            while isUndo != "y" and isUndo != "n":
                print("Enter valid input")
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
