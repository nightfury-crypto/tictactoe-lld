from modals.printStatement import toPrint

def PlayerTurn(playerTurnCheck, turn, board, history, boardSize, columnArr, diagonalArr, antiDiagonalArr):
    while True:
        pos = input(f'''Enter block i,j : 
i - (0-{int(boardSize)-1})
j - (0-{int(boardSize)-1})
or "q" to quit. : ''').split(",")
        # break the loop if player wants to quit
        if pos[0] == "q" and len(pos) == 1:
            return "quit"
        # check for valid input
        if (len(pos) == 2 and pos[0].isdigit() and pos[1].isdigit()):
            if ((int(pos[0]) < boardSize) and (int(pos[0]) >= 0)) and ((int(pos[1]) < boardSize) and (int(pos[1]) >= 0)):
                i,j = int(pos[0]), int(pos[1])
                if(board[i][j] == " "):
                    board[i][j] = playerTurnCheck[turn][1]
                    history.append([i,j])
                    columnArr[j][i] = playerTurnCheck[turn][1]
                    if(i == j):
                        diagonalArr[i] = playerTurnCheck[turn][1]
                    if (i+j == boardSize-1):
                        antiDiagonalArr[boardSize-1-i] = playerTurnCheck[turn][1]
                    return {"IndexI": i, "IndexJ": j, "Symbol": playerTurnCheck[turn][1]}
                else:
                    toPrint("Already filled. Try other coorinates")
            else:
                toPrint("i,j are out of range. Enter valid input")
                continue
        else:
            toPrint("Enter valid input")
            continue