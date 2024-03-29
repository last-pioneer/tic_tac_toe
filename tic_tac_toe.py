#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Моя первая самостоятельная программа. Экспериментирую.
"""
import time
import random as rd


def greetings():
    """
    Эта функция будет приветствовать игроков, знакомить с правилами игры, узнавать имена и
    разыгрывать очередность ходов.
    :return:
    p_1 - [имя игрока, символ хода, очередность, кол-во побед]
    p_2 - [имя игрока, символ хода, очередность, кол-во побед]
    """

    print('\n' * 10)
    print('                                 Вас приветствует игра крестики-нолики!')
    print('\n' * 2 + 'Правила игры очень простые, игрок должен ставить свой ход так, чтобы')
    print('образовать линию из трех Х или 0 в ряд по вертикали, горизонтали или')
    print('диагонали и не дать противнику выстроить свои 0 в такую линию. ')
    print('Игроки ходят по очереди, для того чтоб сделать ход надо нажать на клавишу')
    print('с номером ячейки в которую хотите сделать ход. Игра завершается когда один')
    print('из игроков образует линию из 3 значков. Если игрокам не удалось выстроить линию,')
    print('а все поля заняты, то объявляется  - ничья. Если вы ознакомились с правилами и')
    input('готовы играть нажмите "Ввод"' + '\n')
    print('Давайте познакомимся')
    p_1 = input('Игрок 1, введите имя: ')
    p_2 = input('Игрок 2, введите имя: ')
    print('\n' * 100)
    print('Чудесно, ' + p_1 + ' и ' + p_2 + ' теперь мы случайно определим очередность ходов. ')
    print('Также определим кому играть Х а кому 0.')
    #    time.sleep(3)
    print('\n' * 100)
    r = rd.randint(1, 4)
    if r == 1:
        p_1 = [p_1, 'X', 0, 0]
        p_2 = [p_2, '0', 1, 0]
        print('Первым ходит: ' + p_1[0] + ',  вы играете: X')
        print('Вторым ходит: ' + p_2[0] + ',  вы играете: 0')
    elif r == 2:
        p_1 = [p_1, 'X', 1, 0]
        p_2 = [p_2, '0', 0, 0]
        print('Первым ходит: ' + p_2[0] + ',  вы играете: X')
        print('Вторым ходит: ' + p_1[0] + ',  вы играете: 0')
    elif r == 3:
        p_1 = [p_1, '0', 0, 0]
        p_2 = [p_2, 'X', 1, 0]
        print('Первым ходит: ' + p_1[0] + ',  вы играете: 0')
        print('Вторым ходит: ' + p_2[0] + ',  вы играете: X')
    else:
        p_1 = [p_1, '0', 1, 0]
        p_2 = [p_2, 'X', 0, 0]
        print('Первым ходит: ' + p_2[0] + ',  вы играете: 0\n'
                                          'Вторым ходит: ' + p_1[0] + ',  вы играете: X')
    #    time.sleep(4)
    print('\n' * 100)
    return p_1, p_2


def playing_field(p_1, p_2, counters):
    """
    Эта функция будет создавать, обновлять и отрисовывать изменения на игровом поле.
    Print('\n'*100) --> Рисует 100 пустых строк, тем самым затирая все что было в 100 строках
    """
    g = counters[2]
    print('\n' * 10)
    print('     Крестики нолики 1.0')
    print('   ' + str(counters[0]) + ' - игр сыграно всего')
    print('   ' + str(counters[1]) + ' - игр сыграно в ничью')
    print('   ' + str(p_1[3]) + ' - игр выиграл ' + p_1[0] + '  играет: ' + str(p_1[1]))
    print('   ' + str(p_2[3]) + ' - игр выиграл ' + p_2[0] + '  играет: ' + str(p_2[1]))
    print('\n')
    print('Для выхода из игры введите: N или Н')
    print('\n')
    print('   |       |       |       |')
    print('   |   ' + str(g[6]) + '   |   ' + str(g[7]) + '   |   ' + str(g[8]) + '   |    7    8    9')
    print('   |       |       |       |')
    print('   -------------------------')
    print('   |       |       |       |')
    print('   |   ' + str(g[3]) + '   |   ' + str(g[4]) + '   |   ' + str(g[5]) + '   |    4    5    6')
    print('   |       |       |       |')
    print('   -------------------------')
    print('   |       |       |       |')
    print('   |   ' + str(g[0]) + '   |   ' + str(g[1]) + '   |   ' + str(g[2]) + '   |    1    2    3')
    print('   |       |       |       |')
    print('\n' * 3)


def game_input(name, counters):
    """
    Функция обрабатывает данные введенные игроком с клавиатуры
    ход игрока, проверяет правильность ввода данных.
    :return:
    """
    y = "123456789"
    while True:
        x = input('Игрок: ' + name + ', сделайте свой ход, нажмите кнопку 1-9 : ')
        if x.lower() == 'n' or x.lower() == 'н':
            return "N"
        elif x in y and x != "":
            if 0 <= int(x) <= 9:
                if counters[2][int(x) - 1] == ' ':
                    return int(x)
                else:
                    print('Неверный ход, выберите незанятую клеточку.')
        else:
            print('Выбор неверный, введите цифру от 1 до 9.')


def win(p, g):
    """
    Функция определяет, завершился ли ход победой.
    :return: Bool
    """
    if p[0] == p[1] == p[2] == g[1] or p[3] == p[4] == p[5] == g[1] or p[6] == p[7] == p[8] == g[1] \
            or p[0] == p[3] == p[6] == g[1] or p[1] == p[4] == p[7] == g[1] or p[2] == p[5] == p[8] == g[1] \
            or p[0] == p[4] == p[8] == g[1] or p[2] == p[4] == p[6] == g[1]:
        return 1
    elif " " not in p:  # counters[2].count(" ") == 0:
        return 2
    else:
        return 0


def turn_handler(p_1, p_2, counters, p_3):
    x = game_input(p_3[0], counters)
    if str(x) == "N":
        print('\n' * 100)
        print("Возвращайтесь скорей!\nИграйте в хорошие игры!")
        time.sleep(3)
        return False
    counters[2][int(x) - 1] = p_3[1]
    z = win(counters[2], p_3)
    if z == 1:
        counters[0] += 1
        p_3[3] += 1
        playing_field(p_1, p_2, counters)
        print(p_3[0] + " - Победа за вами!")
        time.sleep(3)
        counters[2] = [' '] * 9
        return False
    elif z == 2:
        counters[0] += 1
        counters[1] += 1
        playing_field(p_1, p_2, counters)
        print("Ничья!\nПопробуйте сыграть ещё!")
        counters[2] = [' '] * 9
        return True
    else:
        return True


def continue_game():
    x = input("Хотите сыграть еще? Введите любой символ.\nЗавершить игру "
              "введите N или Н: ")
    return not (x.lower() == 'n' or x.lower() == 'н')


def game_round(p_1, p_2, counters):
    """
    Функция передает ход от одного игрока другому.
    :return:
    """
    k = 0
    while True:
        playing_field(p_1, p_2, counters)
        k += 1
        if k % 2 == 0 and turn_handler(p_1, p_2, counters, p_1):
            print('что за хуйня! 1 ')
        elif k % 2 != 0 and turn_handler(p_1, p_2, counters, p_2):
            print('что за хуйня! 2')
        else:
            if continue_game():
                continue
            else:
                break


def game_master(p_1, p_2):
    """
    Эта функция будет контролировать игровой процесс.
    counters[0] - round_counter - счетчик раундов
    counters[1] - переменная будет хранить кол-во игр сыгранных в ничью
    counters[2] - р - это список значений клеток поля игры.
    :return: none
    """
    v = [' '] * 9
    counters = [0, 0, v]
    rounds = 0
    while True:
        if rounds % 2 == 0:
            rounds += 1
            if not game_round(p_1, p_2, counters):
                break
            else:
                continue
        else:
            rounds += 1
            if not game_round(p_1, p_2, counters):
                break
            else:
                continue


# v = [' '] * 9
# counters = [0, 0, v]
player_1 = ['Ваня', 0, 1, 5]
player_2 = ['Игорь', 'X', 0, 5]
game_master(player_1, player_2)
# game_round(player_1, player_2, counters)
# turn_handler(player_1, player_2, counters, player_1)
