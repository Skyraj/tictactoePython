board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

def drawBoard():
    print("Let's Play Tic Tac Toe!\n")
    print(" " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " ")
    print("---+---+---")
    print(" " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " ")
    print("---+---+---")
    print(" " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " \n")

def checkVictory():
    if board[0][0] == board[0][1] == board[0][2]:
        return True
    elif board[1][0] == board[1][1] == board[1][2]:
        return True
    elif board[2][0] == board[2][1] == board[2][2]:
        return True
    elif board[0][0] == board[1][0] == board[2][0]:
        return True
    elif board[0][1] == board[1][1] == board[2][1]:
        return True
    elif board[0][2] == board[1][2] == board[2][2]:
        return True
    elif board[0][0] == board[1][1] == board[2][2]:
        return True
    elif board[0][2] == board[1][1] == board[2][0]:
        return True
    else:
        return False

def ttt():
    turn_count = 0
    turn = 'X'
    print("Player {} goes first!".format(turn))

    while (turn_count <= 9):
        x, y = input("Input Position: ").split()
        if board[x][y] == ' ':
            board[x][y] = turn
        # Need to elaborate on error case to ask for input again
        else:
            print("Position taken!")
        
        if checkVictory():
            break
        
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

        turn_count += 1
        drawBoard()
    
    if turn_count % 2 == 0:
        print("Player X Wins!")
    else:
        print("Player O Wins!")

drawBoard()
ttt()