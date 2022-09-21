# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint


def AI(candies, player):
    if player == 1:
        player = 'PLAYER'
    else:
        player = 'BOT'
    print(f'\t{player} STARTS!')
    while candies > 0:
        if player == 'PLAYER':
            n = int(
                input(f'\n{player} turn :\t'))
        else:
            n = randint(1, 29)
            print(f'\n{player} turn :\t{n}')
        if 0 < n < 29:
            candies -= n
            print(f'Leftover candy:\t{candies}')
            if candies <= 0:
                print(f'\n\t{player} WINS!\n')
            if player == 'PLAYER':
                player = 'BOT'
            else:
                player = 'PLAYER'
        else:
            print('\n\tYou must enter the number from 1 to 28, try again !')
            continue


def PVP(candies, player):
    print(f'\n\tPLAYER {player} STARTS!')
    while candies > 0:
        n = int(
            input(f'\nPlayer {player} turn :\t'))
        if 0 < n < 29:
            candies -= n
            print(f'Leftover candy:\t{candies}')
            if candies <= 0:
                print(f'\n\tPLAYER {player} WINS!\n')
            if player == 1:
                player += 1
            else:
                player -= 1
        else:
            print('\n\tYou must enter the number from 1 to 28, try again !')
            continue


try:
    candies = 200
    player = randint(1, 2)
    choise = int(input(
        '\nEnter number of gamemode:\n\tPvP --> \t"1"\n\tEasy AI -->\t"2"\n\tSmart AI -->\t"3"\t'))
    print('\nEnter the number of sweets from 1 to 28 !\n')
    print(f'\tTotal sweets:\t{candies}')
    if choise == 1:
        PVP(candies, player)
    elif choise == 2:
        AI(candies, player)
    else:
        pass

except ValueError:
    print('Incorrect data! You must enter number, try again!')
