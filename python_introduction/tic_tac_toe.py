from os import system
from time import sleep
from random import randint

the_board = {1: ' ', 2: ' ', 3: ' ',
             4: ' ', 5: ' ', 6: ' ',
             7: ' ', 8: ' ', 9: ' '}

players_choices = {'X': '', 'O': ''}  # H or C


def print_board(board):
    print(' ' + str(board[1]) + ' | ' + str(board[2]) + ' | ' + str(board[3])
          + '             ' + str(1) + ' | ' + str(2) + ' | ' + str(3))
    print('---+---+---' + '           ' + '---+---+---')
    print(' ' + str(board[4]) + ' | ' + str(board[5]) + ' | ' + str(board[6])
          + '             ' + str(4) + ' | ' + str(5) + ' | ' + str(6))
    print('---+---+---' + '           ' + '---+---+---')
    print(' ' + str(board[7]) + ' | ' + str(board[8]) + ' | ' + str(board[9])
          + '             ' + str(7) + ' | ' + str(8) + ' | ' + str(9))


def clear_screen():
    system('clear')
    print('\n       >>> TIC-TAC-TOE <<< ')
    print_players = []
    for k, v in players_choices.items():
        if v == 'H':
            print_players.insert(0, '        Human: ' + k + '   ')
        elif v == 'C':
            print_players.append('CPU: ' + k)
    for player in print_players:
        print(player, end='')
    print('\n')


def is_winner(move, turn):
    if move == 1:  # check to the right and low and diagonal low
        if the_board[2] == turn and the_board[3] == turn:  # right
            return True
        elif the_board[4] == turn and the_board[7] == turn:  # low
            return True
        elif the_board[5] == turn and the_board[9] == turn:  # diagonal
            return True
    elif move == 2:  # check to the right and low and diagonal low
        if the_board[1] == turn and the_board[3] == turn:  # right
            return True
        elif the_board[5] == turn and the_board[8] == turn:  # low
            return True
    elif move == 3:  # check to the right and low and diagonal low
        if the_board[2] == turn and the_board[1] == turn:  # right
            return True
        elif the_board[6] == turn and the_board[9] == turn:  # low
            return True
        elif the_board[5] == turn and the_board[7] == turn:  # diagonal
            return True

    if move == 4:  # check to the right and low and diagonal low
        if the_board[1] == turn and the_board[7] == turn:  # up and down
            return True
        elif the_board[5] == turn and the_board[6] == turn:  # right in the middle
            return True
    elif move == 5:  # check to the right and low and diagonal low
        if the_board[2] == turn and the_board[8] == turn:  # up and down in the middle
            return True
        elif the_board[4] == turn and the_board[6] == turn:  # left and right in the middle
            return True
        elif the_board[1] == turn and the_board[9] == turn:  # diagonal left-to-right
            return True
        elif the_board[3] == turn and the_board[7] == turn:  # diagonal right-to-left
            return True
    elif move == 6:  # check to the right and low and diagonal low
        if the_board[3] == turn and the_board[9] == turn:  # up and down in the right
            return True
        elif the_board[5] == turn and the_board[4] == turn:  # left in the middle
            return True

    if move == 7:  # check to the right and low and diagonal low
        if the_board[4] == turn and the_board[1] == turn:  # up left
            return True
        elif the_board[5] == turn and the_board[3] == turn:  # right diagonal
            return True
        elif the_board[8] == turn and the_board[9] == turn:  # right
            return True
    elif move == 8:  # check to the right and low and diagonal low
        if the_board[5] == turn and the_board[2] == turn:  # up in the middle
            return True
        elif the_board[7] == turn and the_board[9] == turn:  # left and right
            return True
    elif move == 9:  # check to the right and low and diagonal low
        if the_board[6] == turn and the_board[3] == turn:  # up right
            return True
        elif the_board[8] == turn and the_board[7] == turn:  # left low
            return True
        elif the_board[5] == turn and the_board[1] == turn:  # diagonal left
            return True

    return False


def move_cpu():
    enemy_positions = []
    this_positions = []

    # Get positions for the enemy and this player
    for position, figure in the_board.items():
        if figure == ' ':
            continue
        if players_choices[figure] == 'C':
            this_positions.append(position)
        elif players_choices[figure] == 'H':
            enemy_positions.append(position)
    
    move = None
    # 2. Go for this player positions and check for possible win moves
    not_empty_positions = enemy_positions + this_positions
    empty_positions = []
    for i in range(1, 10):
        if i not in not_empty_positions:
            empty_positions.append(i)

    # print('this_positions ' + str(this_positions))
    # print('empty_positions ' + str(empty_positions))
    # Check for two positions only and make it a winner
    if 1 in this_positions and 2 in this_positions and 3 in empty_positions:
        move = 3
    elif 1 in this_positions and 3 in this_positions and 2 in empty_positions:
        move = 2
    elif 1 in this_positions and 5 in this_positions and 9 in empty_positions:
        move = 9
    elif 1 in this_positions and 9 in this_positions and 5 in empty_positions:
        move = 5
    elif 1 in this_positions and 4 in this_positions and 7 in empty_positions:
        move = 7
    elif 1 in this_positions and 7 in this_positions and 4 in empty_positions:
        move = 4
        
    elif 2 in this_positions and 3 in this_positions and 1 in empty_positions:
        move = 1
    elif 2 in this_positions and 5 in this_positions and 8 in empty_positions:
        move = 8

    elif 3 in this_positions and 5 in this_positions and 7 in empty_positions:
        move = 7
    elif 3 in this_positions and 7 in this_positions and 5 in empty_positions:
        move = 5
    elif 3 in this_positions and 6 in this_positions and 9 in empty_positions:
        move = 9
    elif 3 in this_positions and 9 in this_positions and 6 in empty_positions:
        move = 6

    elif 4 in this_positions and 7 in this_positions and 1 in empty_positions:
        move = 1
    elif 4 in this_positions and 5 in this_positions and 6 in empty_positions:
        move = 6
    elif 4 in this_positions and 6 in this_positions and 5 in empty_positions:
        move = 5
        
    elif 5 in this_positions and 8 in this_positions and 2 in empty_positions:
        move = 2
    elif 5 in this_positions and 6 in this_positions and 4 in empty_positions:
        move = 4
    elif 5 in this_positions and 9 in this_positions and 1 in empty_positions:
        move = 1
    elif 5 in this_positions and 7 in this_positions and 3 in empty_positions:
        move = 3

    elif 6 in this_positions and 9 in this_positions and 3 in empty_positions:
        move = 3

    elif 7 in this_positions and 8 in this_positions and 9 in empty_positions:
        move = 9
    elif 7 in this_positions and 9 in this_positions and 8 in empty_positions:
        move = 8
        # 8 and 9 are already included in the other conditions

    # print('after cpu 2 - move: ' + str(move))
    # print('enemy_positions: ' + str(enemy_positions))
    # 1. Go through enemy positions and return position to block possible win moves
    if move == None and len(enemy_positions) >= 2:
        if 1 in enemy_positions:
            if 4 in enemy_positions:
                move = 7
            elif 7 in enemy_positions:
                move = 4
            elif 5 in enemy_positions:
                move = 9
            elif 9 in enemy_positions:
                move = 5
            elif 2 in enemy_positions:
                move = 3
            elif 3 in enemy_positions:
                move = 2
        elif 2 in enemy_positions:
            if 1 in enemy_positions:
                move = 3
            elif 3 in enemy_positions:
                move = 1
            elif 5 in enemy_positions:
                move = 8
        elif 3 in enemy_positions:
            if 1 in enemy_positions:
                move = 2
            elif 2 in enemy_positions:
                move = 1
            elif 5 in enemy_positions:
                move = 8
            elif 9 in enemy_positions:
                move = 6
            elif 6 in enemy_positions:
                move = 9
            elif 5 in enemy_positions:
                move = 7
            elif 7 in enemy_positions:
                move = 5
        elif 4 in enemy_positions:
            if 1 in enemy_positions:
                move = 7
            elif 7 in enemy_positions:
                move = 1
            elif 5 in enemy_positions:
                move = 6
            elif 6 in enemy_positions:
                move = 5
        elif 5 in enemy_positions:
            if 2 in enemy_positions:
                move = 8
            elif 8 in enemy_positions:
                move = 2
            elif 4 in enemy_positions:
                move = 6
            elif 6 in enemy_positions:
                move = 4
            elif 1 in enemy_positions:
                move = 9
            elif 9 in enemy_positions:
                move = 1
            elif 3 in enemy_positions:
                move = 7
            elif 7 in enemy_positions:
                move = 3
        elif 6 in enemy_positions:
            if 3 in enemy_positions:
                move = 9
            elif 9 in enemy_positions:
                move = 3
            elif 5 in enemy_positions:
                move = 4
            elif 4 in enemy_positions:
                move = 5
        elif 7 in enemy_positions:
            if 1 in enemy_positions:
                move = 4
            elif 4 in enemy_positions:
                move = 1
            elif 5 in enemy_positions:
                move = 3
            elif 3 in enemy_positions:
                move = 5
            elif 8 in enemy_positions:
                move = 9
            elif 9 in enemy_positions:
                move = 8
        elif 8 in enemy_positions:
            if 5 in enemy_positions:
                move = 2
            elif 2 in enemy_positions:
                move = 5
            elif 7 in enemy_positions:
                move = 9
            elif 9 in enemy_positions:
                move = 7
        elif 9 in enemy_positions:
            if 3 in enemy_positions:
                move = 6
            elif 6 in enemy_positions:
                move = 3
            elif 7 in enemy_positions:
                move = 8
            elif 8 in enemy_positions:
                move = 7
            elif 1 in enemy_positions:
                move = 5
            elif 5 in enemy_positions:
                move = 1
    # print('after enemy - move: ' + str(move))
    
    # if. position a move if there's one (enemy) or 0 (means the cpu goes first) positions
    if move == None and move not in this_positions: # not this_positions = empty list
        best_moves = [1, 7, 5, 3, 9]
        move = best_moves[randint(0, len(best_moves) - 1)]
        if the_board[move] != ' ':
            best_moves.remove(move)
            move = best_moves[randint(0, len(best_moves) - 1)]
    # print('first cpu move, best moves - move: ' + str(move))
    
    # check for empty positions and map it againts this_positions, then decide which spot 
    if move == None:
        # Check for one position only
        if 1 in this_positions and 8 not in empty_positions:
            move = 8
        elif 2 in this_positions and 9 not in empty_positions:
            move = 9
        elif 3 in this_positions and 8 not in empty_positions:
            move = 8
        elif 4 in this_positions and 3 not in empty_positions:
            move = 3
        elif 5 in this_positions and 6 not in empty_positions:
            move = 6
        elif 6 in this_positions and 1 not in empty_positions:
            move = 1
        elif 7 in this_positions and 3 not in empty_positions:
            move = 3
        elif 8 in this_positions and 1 not in empty_positions:
            move = 1
        elif 9 in this_positions and 2 not in empty_positions:
            move = 2        
    # print('after cpu simple - move: ' + str(move))      
    # At the end Check if move is only in an empty position, 
    # if not get empty positions (!= not_empty_positions) and set move to one of those empty positions
    # check possible wins after enemy positions are not dangerous, for example: 
    # this_positions [4, 5] and enemy_positions[1, 6, 7] and empty_postions[2, 3, 8, 9], pick the best which is 2 or 5; 
    # not random from empty positions.
    if move in not_empty_positions or move == None:
        move = empty_positions[randint(0, len(empty_positions) - 1)]
    """
    {1: ' ', 2: ' ', 3: 'X',
     4: ' ', 5: 'O', 6: ' ',
     7: ' ', 8: 'X', 9: ' '}  
    """
    
    return move

    
def validate_number_input():
    while True:
        try:
            move = int(input())
            while move < 1 or move > 9:
                print("Not a valid number, pick anumber between 1-9.")
                move = int(input())
        except ValueError:
            print('Not a valid number. Try again!')
            continue
        else:
            while the_board[move] != ' ':
                print('***> Position is not empty. Choose another position: ')
                move = validate_number_input()
            return move


def set_space(selection):
    print('Turn for ' + selection + '. Move on which space?')
    move = 1
    if players_choices[selection] == 'H':
        move = validate_number_input()
    elif players_choices[selection] == 'C':
        sleep(2)
        move = move_cpu()  # TODO check adversary spaces and if it's about to win, pick that place
        print(move)
        sleep(2)
    
    the_board[move] = selection
    return move


def select_player_turns():
    
    print('===> Picking first player... ')
    sleep(2)
    cpu_turn = randint(0,9) > 4
    if cpu_turn: # CPU
        selection = 'X' if randint(0,9) > 4 else 'O'
        for key in players_choices.keys():
            players_choices[key] = 'C' if key == selection else 'H'
        print('>>> CPU picks: ' + selection)
        sleep(2)
    else: # Human
        print('>>> Human picks!')
        print('===> Select Letter (X or O - not ZERO -)')
        selection = input().upper()
        while selection not in  ['X', 'O']:
            print('***> SELECT correct LETTER (X - O)')
            selection = input().upper()
        for key in players_choices.keys():
            players_choices[key] = 'H' if key == selection else 'C'
    
    return selection


def empty_spaces():
    empty_positions = []
    for position in the_board:
        if the_board[position] == ' ':
            empty_positions.append(position)
    return empty_positions


def play_again():
    print('Want to play again: (Y - N) ', end='')
    continue_playing = input().upper()
    while continue_playing not in ['Y', 'N']:
        print('Invalid choice, play again? (Y - N) ', end='')
        continue_playing = input().upper()
            
    if continue_playing == 'Y':
        for position in the_board:
            the_board[position] = ' '
        return True
    else:
        return False


def welcome():
    clear_screen()
    print('*************************************')
    print('**** Welcome to TIC-TAC-TOE game ****')
    print('*************************************\n')


def game_on():
    welcome()
    # Select Player vs CPU. Who will go first?
    selection = select_player_turns()

    keep_playing = True

    while keep_playing:
        clear_screen()
        print_board(the_board)

        if empty_spaces():
            # set the position
            move = set_space(selection)
        else:
            sleep(1)
            print('\n>>>>> There is a TIE! <<<<<' )
            keep_playing = play_again()

        # Check winner
        if is_winner(move, selection):
            clear_screen()
            print_board(the_board)
            print('\n******* The winner is ' + selection + ' *******')
            keep_playing = play_again()

        # Change selection
        selection = 'O' if selection == 'X' else 'X'


game_on()
