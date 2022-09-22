# Создайте программу для игры в ""Крестики-нолики"".

from random import randint
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


def PVP(board, player):
    if player == 1:
        turn = 'X'
    else:
        turn = '0'
    flag = True
    while ('*' in board) and flag:
        # system('cls||clear')
        try:
            n = int(
                input(f'\nPlayer {player} turn :\t'))-1
        except ValueError:
            print('\nIncorrect data! You must enter number, try again!')
            continue
        if 0 <= n < 10:
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


board = ['*', '*', '*', '*', '*', '*', '*', '*', '*']
player = randint(1, 2)

choise = int(input(
    '\nEnter number of gamemode:\n\tPvP --> \t"1"\n\tEasy AI -->\t"2"\n\tSmart AI -->\t"3"\t'))
if choise == 1:
    system('cls||clear')
    print('\nEnter the field number from 1 to 9! As shown here:\n')
    print_board(board, '123456789')
    print(f'\n\tPLAYER {player} STARTS!')
    PVP(board, player)
