# Создайте программу для игры в ""Крестики-нолики"".

from random import choice, randint, randrange
from os import system


def print_board(board, value='         '):
    for i in range(3):
        print(
            f'\n{board[0+i*3]+value[0+i*3]}\t{board[1+i*3]+value[1+i*3]}\t{board[2+i*3]+value[2+i*3]}')


def win_check(board, turn):
    return (((board[0] == turn) and (board[1] == turn) and (board[2] == turn)) or
            ((board[3] == turn) and (board[4] == turn) and (board[5] == turn)) or
            ((board[6] == turn) and (board[7] == turn) and (board[8] == turn)) or
            ((board[0] == turn) and (board[4] == turn) and (board[8] == turn)) or
            ((board[6] == turn) and (board[4] == turn) and (board[2] == turn)) or
            ((board[0] == turn) and (board[3] == turn) and (board[6] == turn)) or
            ((board[1] == turn) and (board[4] == turn) and (board[7] == turn)) or
            ((board[2] == turn) and (board[5] == turn) and (board[8] == turn)))


def draw_check(board, turn):
    if not win_check(board, turn) and not ('*' in board):
        return True


def Easy_AI(board):
    n = randint(0, 8)
    while board[n] != '*':
        n = randint(0, 8)
    return n


def first_step(board):
    count = 0
    for i in board:
        if i == '0':
            count += 1
    if count < 1:
        return True
    else:
        return False


def random_turn(board, moves):
    possible_moves = []
    for i in moves:
        if board[i] == '*':
            possible_moves.append(i)

    if len(possible_moves) != 0:
        return choice(possible_moves)
    else:
        return None


def copy_board(board):
    copy = []
    for i in board:
        copy.append(i)
    return copy


def corner_and_center_is_busy(board):
    return (board[0] == '0' or board[2] == '0' or board[6] == '0' or board[8] == '0') and board[4] == '0'


def right_turn(board):
    n = -1
    if corner_and_center_is_busy(board):
        if board[0] == '0':
            if board[1] == '*' and board[2] == '*':
                n = 1
            if board[3] == '*' and board[6] == '*':
                n = 3
        if board[2] == '0':
            if board[1] == '*' and board[0] == '*':
                n = 1
            if board[5] == '*' and board[8] == '*':
                n = 5
        if board[6] == '0':
            if board[3] == '*' and board[0] == '*':
                n = 3
            if board[7] == '*' and board[8] == '*':
                n = 7
        if board[8] == '0':
            if board[5] == '*' and board[2] == '*':
                n = 5
            if board[7] == '*' and board[6] == '*':
                n = 7
        if n != -1:
            return n
        else:
            return None
    else:
        return random_turn(board, [0, 2, 6, 8])


def Smart_AI(board):
    if first_step(board):
        if board[4] == '*':
            n = 4
        else:
            n = randrange(0, 9, 2)
    else:
        n = right_turn(board)
        if n == None:
            n = random_turn(board, [1, 3, 5, 7])
            if n == None:
                n = random_turn(board, [0, 2, 6, 8])
        for i in range(0, 9):
            copy = copy_board(board)
            if copy[i] == '*':
                copy[i] = 'X'
                if win_check(copy, 'X'):
                    n = i
        for i in range(0, 9):
            copy = copy_board(board)
            if copy[i] == '*':
                copy[i] = '0'
                if win_check(copy, '0'):
                    n = i
    return n


def PVP(board, player):
    if player == 1:
        turn = 'X'
    else:
        turn = '0'
    flag = True
    while ('*' in board) and flag:
        try:
            n = int(
                input(f'\nPlayer {player} turn :\t'))-1
        except ValueError:
            print('\nIncorrect data! You must enter number, try again!')
            continue
        if 0 <= n <= 8:
            if board[n] == 'X' or board[n] == '0':
                print('\nThis field is busy try again!')
            else:
                board[n] = turn
                system('cls||clear')
                print_board(board)
                if win_check(board, turn):
                    print(f'\n\tPLAYER {player} WINS!\n')
                    flag = False
                if draw_check(board, turn):
                    print("\n\tIT'S A DRAW!\n")
                if player == 1:
                    player += 1
                    turn = '0'
                else:
                    player -= 1
                    turn = 'X'
        else:
            print('\n\tYou must enter the number from 1 to 9, try again !')
            continue


def AI(board, player, selection):
    if player == 'PLAYER':
        turn = 'X'
    else:
        turn = '0'
    flag = True
    while ('*' in board) and flag:
        if turn == 'X':
            try:
                n = int(
                    input(f'\n{player} turn :\t'))-1
            except ValueError:
                print('\nIncorrect data! You must enter number, try again!')
                continue
        else:
            if selection == 2:
                n = Easy_AI(board)
            else:
                n = Smart_AI(board)
        if 0 <= n <= 8:
            if board[n] == 'X' or board[n] == '0':
                print('\nThis field is busy try again!')
            else:
                board[n] = turn
                system('cls||clear')
                print_board(board)
                if win_check(board, turn):
                    print(f'\n\t{player} WINS!\n')
                    flag = False
                if draw_check(board, turn):
                    print("\n\tIT'S A DRAW!\n")
                if player == 'PLAYER':
                    player = 'BOT'
                    turn = '0'
                else:
                    player = 'PLAYER'
                    turn = 'X'
        else:
            print('\n\tYou must enter the number from 1 to 9, try again !')
            continue


board = ['*', '*', '*', '*', '*', '*', '*', '*', '*']
player = randint(1, 2)

selection = int(input(
    '\nEnter number of gamemode:\n\tPvP --> \t"1"\n\tEasy AI -->\t"2"\n\tSmart AI -->\t"3"\t'))
system('cls||clear')
print('\nEnter the field number from 1 to 9! As shown here:\n')
print_board(board, '123456789')
if selection == 1:
    print(f'\n\tPLAYER {player} STARTS!')
    PVP(board, player)
else:
    if player == 1:
        player = 'PLAYER'
    else:
        player = 'BOT'
    print(f'\n\t{player} STARTS!')
    AI(board, player, selection)
