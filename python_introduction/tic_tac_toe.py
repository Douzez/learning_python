from os import system
from time import sleep
from random import randint

the_board = {1: ' ', 2: ' ', 3: ' ',
             4: ' ', 5: ' ', 6: ' ',
             7: ' ', 8: ' ', 9: ' '}

turns = {'X': '', 'O': ''}  # H or C


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
    print('\n>>> TIC-TAC-TOE. > ', end='')
    for k, v in turns.items():
        if v == 'H':
            print(k + ': Human', end=' ')
        elif v == 'C':
            print(k + ': CPU', end=' ')
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


def ok_turn(turn):
    if turn == 'X' or turn == 'O':
        return False
    else:
        return True


def get_move(turn):
    move = ''
    if turns[turn] == 'H':
        move = int(input())
        while the_board[move] != ' ' or the_board[move] != ' ':
            print('***> Position is not empty. Choose another position: ')
            move = int(input())
    elif turns[turn] == 'C':
        # TODO 1st check empty spaces and randomly pick an empty space
        # TODO 2nd check adversary spaces and if it's about to win, pick that place
        empty_spaces = []
        for space, move in the_board.items():
            if move == ' ':
                empty_spaces.append(space)
        move = empty_spaces[randint(0, len(empty_spaces) - 1)]
        empty_spaces.clear()
        print(move)
        sleep(2)

    return move


def get_turn():
    print('>>> Picking who goes first!')
    sleep(2)
    if randint(0, 9) >= 5:
        print('CPU picks letter')
        if randint(0, 1) == 0:
            turn = 'X'
            turns[turn] = 'C'
            turns['O'] = 'H'
        else:
            turn = 'O'
            turns[turn] = 'C'
            turns['X'] = 'H'
        print('CPU picked ' + turn)
        sleep(4)
    else:
        print('>>> Human picks!')
        print('===> Select Letter (X or O -non zero-)')
        turn = input()
        while ok_turn(turn):
            print('***> Select correct LETTER X-O')
            turn = input()
        if turn == 'X':
            turns[turn] = 'H'
            turns['O'] = 'C'
        elif turn == 'O':
            turns[turn] = 'H'
            turns['X'] = 'C'
    return turn


def start():
    clear_screen()
    print('*************************************')
    print('**** Welcome to TIC-TAC-TOE game ****')
    print('*************************************\n')

    # Select Player vs CPU. Who will go first?
    turn = get_turn()

    for i in range(9):
        clear_screen()
        print_board(the_board)
        print('Turn for ' + turn + '. Move on which space?')

        # set the position
        move = get_move(turn)
        the_board[move] = turn

        # Check winner
        if is_winner(move, turn):
            clear_screen()
            print_board(the_board)
            print('\n******* The winner is ' + turn + ' *******')
            break

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'


start()
