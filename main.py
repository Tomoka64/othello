from IPython.display import clear_output
import random
import sys, signal

def main():
    try: 
        __main__()
    except KeyboardInterrupt:
        signal.signal(signal.SIGINT, signal_handler)

def __main__():
    board = [' '] * 10  
    available = [str(num) for num in range(0,10)] 
    players = [0,'X','O']
    while True:
        game_mode_controller(board, available,players)

        board = [' '] * 10
        available = [str(num) for num in range(0,10)]

        if not replay():
            break 

def game_mode_controller(board, available,players):
    ans = input("Choose game preference\nplay with friend: 1\nplay with robot: 2\n")
    if ans == '1':
        friends_mode(board, available,players)
    elif ans == '2':
        robot_mode(board, available,players)
    else:
        return game_mode_controller(board, available,players)


def friends_mode(board, available,players):
    clear_output()
    
    first_player = random_player()
    player = players[first_player]
    print('For this round, Player %s will go first!' %(player))
    
    isGameOn = True
    while isGameOn:
        display_board(available,board)
        position = player_choice(board,player)
        place_marker(available,board,player,position)

        if hasWon(board, player):
            display_board(available,board)
            print('Congratulations! Player '+player+' wins!')
            isGameOn = False
        else:
            if isFull(board):
                display_board(available,board)
                print('The game is a draw!')
                break
            else:
                first_player *= -1
                player = players[first_player]
                clear_output()

def robot_mode(board, available,players):
    clear_output()
    
    first_player = random_player()
    player = players[first_player]
    print('For this round, Player %s will go first!' %(player))
    
    isGameOn = True
    if first_player == -1:
        isRobot = False
    else: 
        isRobot = True

    while isGameOn:
        display_board(available,board)
        if isRobot:
            position = robot_choice(board)
            isRobot = False
        else:
            position = player_choice(board,player)
            isRobot = True
        place_marker(available,board,player,position)

        if hasWon(board, player):
            display_board(available,board)
            print('Congratulations! Player '+player+' wins!')
            isGameOn = False
        else:
            if isFull(board):
                display_board(available,board)
                print('The game is a draw!')
                break
            else:
                first_player *= -1
                player = players[first_player]
                clear_output()


def display_board(a,b):
    print(f'Available \n  moves\n\n  {a[7]}|{a[8]}|{a[9]}        {b[7]}|{b[8]}|{b[9]}\n  -----        -----\n  {a[4]}|{a[5]}|{a[6]}        {b[4]}|{b[5]}|{b[6]}\n  -----        -----\n  {a[1]}|{a[2]}|{a[3]}        {b[1]}|{b[2]}|{b[3]}\n')

def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(available,board,marker,position):
    board[position] = marker
    available[position] = ' '


def hasWon(board,mark):
    return ((board[7] ==  board[8] ==  board[9] == mark) or 
    (board[4] ==  board[5] ==  board[6] == mark) or 
    (board[1] ==  board[2] ==  board[3] == mark) or 
    (board[7] ==  board[4] ==  board[1] == mark) or 
    (board[8] ==  board[5] ==  board[2] == mark) or 
    (board[9] ==  board[6] ==  board[3] == mark) or 
    (board[7] ==  board[5] ==  board[3] == mark) or 
    (board[9] ==  board[5] ==  board[1] == mark)) 

def random_player():
    return random.choice((-1, 1))
    
def isvalid(board,position):
    return board[position] == ' '

def isFull(board):
    return ' ' not in board[1:]

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def player_choice(board,player):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not isvalid(board, position):
        try:
            position = int(input('Player %s, choose your next position: (1-9) '%(player)))
        except:
            print("the input was invalid.\nchoose your next position: (1-9)")
    return position

def robot_choice(board):
    inp = random.randint(1, 10) 
    position = 0
    if inp not in [1,2,3,4,5,6,7,8,9] or not isvalid(board, position):
        return inp
    return robot_choice(board)

def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y') == 'y'


def signal_handler(signal, frame):
    print("\nprogram exiting gracefully")
    sys.exit(0)

main()
