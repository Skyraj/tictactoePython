board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

def drawBoard():
    print("\n " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " ")
    print("---+---+---")
    print(" " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " ")
    print("---+---+---")
    print(" " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " \n")

def checkVictory():
    if all(s == 'X' for s in board[0]) or all(s == 'O' for s in board[0]):
        return True
    elif all(s == 'X' for s in board[1]) or all(s == 'O' for s in board[1]):
        return True
    elif all(s == 'X' for s in board[2]) or all(s == 'O' for s in board[2]):
        return True
    elif board[0][0] == board[1][0] == board[2][0] == 'X' or board[0][0] == board[1][0] == board[2][0] == 'O':
        return True
    elif board[0][1] == board[1][1] == board[2][1] == 'X' or board[0][1] == board[1][1] == board[2][1] == 'O':
        return True
    elif board[0][2] == board[1][2] == board[2][2] == 'X' or board[0][2] == board[1][2] == board[2][2] == 'O':
        return True
    elif board[0][0] == board[1][1] == board[2][2] == 'X' or board[0][0] == board[1][1] == board[2][2] == 'O':
        return True
    elif board[0][2] == board[1][1] == board[2][0] == 'X' or board[0][2] == board[1][1] == board[2][0] == 'O':
        return True
    else:
        return False

def ttt():
    turn_count = 1
    turn = 'X'

    while (turn_count < 10):
        print("Turn {}: Player {}'s turn".format(turn_count, turn))
        while True:
            try:
                x, y = input("Enter index: ").split()
                x, y = int(x), int(y)
                
                if board[x][y] == ' ':
                    board[x][y] = turn
                else:
                    raise Exception()
            except ValueError:
                print("2 integer inputs separated by a space is required!")
                continue
            except:
                print("Index taken!")
                turn = 'O'
                continue
            else:
                break

        drawBoard()
        if checkVictory():
            break
        
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

        turn_count += 1
    
    if turn_count == 10:
        print("Tie!")
    elif turn_count % 2 == 0:
        print("Player O Wins!")
    else:
        print("Player X Wins!")


# Terminal Version of Tic Tac Toe
print("Let's Play Tic Tac Toe!")
drawBoard()
ttt()