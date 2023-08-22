def displayBoard(board):
    print("")
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if j == len(board[i]) - 1:
                print(board[i][j], end="")
            else:
                print(board[i][j], end=" |")
        print("")
        if i != len(board) - 1:
            print(len(board[i]) * "⎯⎯ ")
    print("")
