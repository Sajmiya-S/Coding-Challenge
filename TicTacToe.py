# Write a Python program to build a Tic Tac Toe game that allows two players to play against each other on the same computer .

print('\n  Welcome to Tic Tac Toe Game ')

board = [' ' for _ in range(1,11)]

def display_board(board):
    print()
    print(f'{board[1]} | {board[2]} |{board[3]}')
    print('--+---+--')
    print(f'{board[4]} | {board[5]} |{board[6]}')
    print('--+---+--')
    print(f'{board[7]} | {board[8]} |{board[9]}')
    print()

def check_win(player):
    wins =  [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    for win in wins:
        if board[win[0]] == board[win[1]] == board[win [2]] == player:
            return True
    return False

def check_draw():
    return ' ' not in board[1:]

player = 'X'
display_board(board)

while True:
    try:
        move = int(input(f'\nPlayer {player},Enter your move(1-9):' ))
        if move < 1 or move > 9:
            print('\nInvalid move.. Please enter a number between 1 to 9')
            continue
        if board[move] != ' ':
            print('\nSpot already taken.. Try again')
            continue
    except ValueError:
        print('\nEnter a valid number')
        continue

    board[move] = player
    display_board(board)

    if check_win(player):
        print(f'\nPlayer {player} wins!!!')
        break

    if check_draw():
        print('\nIts a draw!!!')
        break
    player = 'O' if player == 'X' else 'X'  












