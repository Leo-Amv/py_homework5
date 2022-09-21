# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint


candies = 2021
player = randint(1, 2)
print('\nEnter the number of sweets from 1 to 28 !\n')
print(f'\tPLAYER {player} STARTS!')
print(f'\n\tTotal sweets:\t{candies}')


try:
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
except ValueError:
    print('Incorrect data! You must enter number, try again!')
