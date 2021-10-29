import time
import random as rd

"""
Моя первая самостоятельная программа.

"""


def greetings():
    """
    Эта функция будет приветствовать игроков, узнавать имена, разыгрывать очередность ходов \
    и знакомить с правилами игры.
    :return: name_1, name_2, priority
    """

    print('\n' * 10)
    print('                                 Вас приветствует игра крестики-нолики!')
    print('\n' * 2 + 'Правила игры очень простые, игрок должен ставить свой ход так, чтобы образовать линию из трех Х \
     в ряд')
    print('по вертикали, горизонтали или диагонали и не дать противнику выстроить свои О в такую линию. ')
    print('Игроки ходят по очереди, для того чтоб сделать ход надо нажать на клавишу с номером ячейки')
    print('в которую хотите сделать ход. Игра завершается когда один из игроков образует линию из 3 значков.')
    print('Если игрокам не удалось выстроить линию, а все поля заняты, то объявляется  - ничья.')
    scip = input('Если вы ознакомились с правилами и готовы играть нажмите "Ввод"')
    print('\n''Давайте познакомимся')
    p_1 = input('Игрок 1, введите имя: ')
    p_2 = input('Игрок 2, введите имя: ')
    print('\n' * 100)
    print('Чудесно, ' + p_1 + ' и ' + p_2 + ' теперь мы случайно определим кто ходит первым.')
    time.sleep(2)
    r = rd.randint(1, 2)
    # p_3 - хранит очередность ходов.
    if r == 1:
        p_3 = 0
        print('Первым ходит: ' + p_1 + '   Вторым ходит: ' + p_2)
    else:
        p_3 = 1
        print('Первым ходит: ' + p_2 + '   Вторым ходит: ' + p_1)
    time.sleep(2)
    print('\n' * 100)
    return p_1, p_2, p_3


def playing_field(gamer_1, s_g_1, gamer_2, s_g_2, s_g_0, p, round_counter):
    """
    эта функция будет создавать, обновлять и отрисовывать изменения на игровом поле.
    print('\n'*100) --> Рисует 100 пустых строк, тем самым затирая все что было в 100 строках
    :return:
    """
    print('\n' * 10)
    print('     Крестики нолики 1.0')
    print('   ' + str(round_counter) + ' - игр сыграно всего')
    print('   ' + str(s_g_0) + ' - игр сыграно в ничью')
    print('   ' + str(s_g_1) + ' - игр выиграл ' + gamer_1)
    print('   ' + str(s_g_2) + ' - игр выиграл ' + gamer_2)
    print('\n')
    print('   |       |       |       |')
    print('   |   ' + p[6] + '   |   ' + p[7] + '   |   ' + p[8] + '   |    7    8    9')
    print('   |       |       |       |')
    print('   -------------------------')
    print('   |       |       |       |')
    print('   |   ' + p[3] + '   |   ' + p[4] + '   |   ' + p[5] + '   |    4    5    6')
    print('   |       |       |       |')
    print('   -------------------------')
    print('   |       |       |       |')
    print('   |   ' + p[0] + '   |   ' + p[1] + '   |   ' + p[2] + '   |    1    2    3')
    print('   |       |       |       |')
    print('\n' * 3)


def game_master(name_1, name_2, priority, round_counter):
    """
    Эта функция будет контролировать игровой процесс.
    р - это список значений полей игры, для определения правильности ходов, ничьей или победы.
    s_g_0 - переменная будет хранить кол-во игр сыгранных в ничью
    s_g_1 - переменная будет хранить кол-во игр выигранных игроком_1
    s_g_2 - переменная будет хранить кол-во игр выигранных игроком_2
    priority - хранит очередность ходов.
    round_counter - счетчик раундов

    :return:
    """
    p = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    round_counter = 0
    s_g_0 = int(0)
    s_g_1 = int(0)
    s_g_2 = int(0)
    playing_field(name_1, s_g_1, name_2, s_g_2, s_g_0, p, round_counter)
    game_round(name_1, s_g_1, name_2, s_g_2, s_g_0, p, priority, round_counter)
    if p[0] == p[1] == p[2] == 'X' or p[3] == p[4] == p[5] == 'X' or p[6] == p[7] == p[8] == 'X' \
            or p[0] == p[3] == p[6] == 'X' or p[1] == p[4] == p[7] == 'X' or p[2] == p[5] == p[3] == 'X' \
            or p[0] == p[4] == p[8] == 'X' or p[2] == p[4] == p[6] == 'X':
        s_g_1 += 1
        round_counter += 1
        time.sleep(3)
        playing_field(name_1, s_g_1, name_2, s_g_2, s_g_0, p, round_counter)
        print('Начинаем следующий раунд!')
        time.sleep(3)
        print('\n' * 100)
        p = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        playing_field(name_1, s_g_1, name_2, s_g_2, s_g_0, p, round_counter)
        game_round(name_1, s_g_1, name_2, s_g_2, s_g_0, p, priority, round_counter)

    elif p[0] == p[1] == p[2] == 'O' or p[3] == p[4] == p[5] == 'O' or p[6] == p[7] == p[8] == 'O' \
            or p[0] == p[3] == p[6] == 'O' or p[1] == p[4] == p[7] == 'O' or p[2] == p[5] == p[3] == 'O' \
            or p[0] == p[4] == p[8] == 'O' or p[2] == p[4] == p[6] == 'O':
        s_g_2 += 1
        round_counter += 1
        playing_field(name_1, s_g_1, name_2, s_g_2, s_g_0, p, round_counter)
        time.sleep(3)
        print('\n' * 100)
        print('Начинаем следующий раунд!')
        time.sleep(3)
        print('\n' * 100)
        p = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        playing_field(name_1, s_g_1, name_2, s_g_2, s_g_0, p, round_counter)
        game_round(name_1, s_g_1, name_2, s_g_2, s_g_0, p, priority, round_counter)
    else:
        s_g_0 = int(s_g_0)
        s_g_0 += 1
        round_counter += 1
    p = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    playing_field(name_1, s_g_1, name_2, s_g_2, s_g_0, p, round_counter)
    time.sleep(2)
    print('\n' * 100)
    print('Начинаем следующий раунд!')
    print('\n' * 10)
    game_round(name_1, s_g_1, name_2, s_g_2, s_g_0, p, priority, round_counter)


def player_turn_1(name, p):
    y = '123456789'
    q = 0
    while q != 1:
        x = input('Игрок: ' + name + ', сделайте свой ход, нажмите кнопку 1-9 : ')
        if x in y and x != '':
            x = int(x)
            if p[x - 1] != ' ':
                print('Клеточка занята, выберите цифру не занятой клеточки!')
            else:
                p[x - 1] = 'X'
                q = 1
                priority = 1
                return priority
        else:
            print('Вы ввели не правильное число, введите цифру от 1 до 9.')


def player_turn_2(name, p):
    y = '123456789'
    q = 0
    while q != 1:
        x = input('Игрок: ' + name + ', сделайте свой ход, нажмите кнопку 1-9 : ')
        if x in y and x != '':
            x = int(x)
            if p[x - 1] != ' ':
                print('Клеточка занята, выберите цифру не занятой клеточки!')
            else:
                p[x - 1] = 'O'
                q = 1
                priority = 0
                return priority
        else:
            print('Вы ввели не правильное число, введите цифру от 1 до 9.')


def game_round(name_1, s_g_1, name_2, s_g_2, s_g_0, p, priority, round_counter):
    if p.count(' ') != 0:
        if round_counter == 0:
            if priority == 0:
                priority = player_turn_1(name_1, p)
                playing_field(name_1, s_g_1, name_2, s_g_2, s_g_0, p, round_counter)
                if p[0] == p[1] == p[2] == 'X' or p[3] == p[4] == p[5] == 'X' or p[6] == p[7] == p[8] == 'X' \
                        or p[0] == p[3] == p[6] == 'X' or p[1] == p[4] == p[7] == 'X' or p[2] == p[5] == p[3] == 'X' \
                        or p[0] == p[4] == p[8] == 'X' or p[2] == p[4] == p[6] == 'X':
                    print('Победил игрок -  ' + name_1 + ' Поздравляем!')
                    s_g_1 += 1
                    round_counter += 1
                else:
                    game_round(name_1, s_g_1, name_2, s_g_2, s_g_0, p, priority, round_counter)
            else:
                priority = player_turn_2(name_2, p)
                playing_field(name_1, s_g_1, name_2, s_g_2, s_g_0, p, round_counter)
                if p[0] == p[1] == p[2] == 'O' or p[3] == p[4] == p[5] == 'O' or p[6] == p[7] == p[8] == 'O' \
                        or p[0] == p[3] == p[6] == 'O' or p[1] == p[4] == p[7] == 'O' or p[2] == p[5] == p[3] == 'O' \
                        or p[0] == p[4] == p[8] == 'O' or p[2] == p[4] == p[6] == 'O':
                    print('Победил игрок -  ' + name_2 + ' Поздравляем!')
                    s_g_2 += 1
                    round_counter += 1
                else:
                    game_round(name_1, s_g_1, name_2, s_g_2, s_g_0, p, priority, round_counter)
        elif (round_counter + 1) % 2 == 0:
            if priority == 1:
                priority = player_turn_1(name_1, p)
                playing_field(name_1, s_g_1, name_2, s_g_2, s_g_0, p, round_counter)
                if p[0] == p[1] == p[2] == 'X' or p[3] == p[4] == p[5] == 'X' or p[6] == p[7] == p[8] == 'X' \
                        or p[0] == p[3] == p[6] == 'X' or p[1] == p[4] == p[7] == 'X' or p[2] == p[5] == p[3] == 'X' \
                        or p[0] == p[4] == p[8] == 'X' or p[2] == p[4] == p[6] == 'X':
                    print('Победил игрок -  ' + name_1 + ' Поздравляем!')
                    s_g_1 += 1
                    round_counter += 1
                else:
                    game_round(name_1, s_g_1, name_2, s_g_2, s_g_0, p, priority, round_counter)
            else:
                priority = player_turn_2(name_2, p)
                playing_field(name_1, s_g_1, name_2, s_g_2, s_g_0, p, round_counter)
                if p[0] == p[1] == p[2] == 'O' or p[3] == p[4] == p[5] == 'O' or p[6] == p[7] == p[8] == 'O' \
                        or p[0] == p[3] == p[6] == 'O' or p[1] == p[4] == p[7] == 'O' or p[2] == p[5] == p[3] == 'O' \
                        or p[0] == p[4] == p[8] == 'O' or p[2] == p[4] == p[6] == 'O':
                    print('Победил игрок -  ' + name_2 + ' Поздравляем!')
                    s_g_2 += 1
                    round_counter += 1
                else:
                    game_round(name_1, s_g_1, name_2, s_g_2, s_g_0, p, priority, round_counter)
        elif round_counter % 2:
            if priority == 0:
                priority = player_turn_1(name_1, p)
                playing_field(name_1, s_g_1, name_2, s_g_2, s_g_0, p, round_counter)
                if p[0] == p[1] == p[2] == 'X' or p[3] == p[4] == p[5] == 'X' or p[6] == p[7] == p[8] == 'X' \
                        or p[0] == p[3] == p[6] == 'X' or p[1] == p[4] == p[7] == 'X' or p[2] == p[5] == p[3] == 'X' \
                        or p[0] == p[4] == p[8] == 'X' or p[2] == p[4] == p[6] == 'X':
                    print('Победил игрок -  ' + name_1 + ' Поздравляем!')
                    s_g_1 += 1
                    round_counter += 1
                else:
                    game_round(name_1, s_g_1, name_2, s_g_2, s_g_0, p, priority, round_counter)
            else:
                priority = player_turn_2(name_2, p)
                playing_field(name_1, s_g_1, name_2, s_g_2, s_g_0, p, round_counter)
                if p[0] == p[1] == p[2] == 'O' or p[3] == p[4] == p[5] == 'O' or p[6] == p[7] == p[8] == 'O' \
                        or p[0] == p[3] == p[6] == 'O' or p[1] == p[4] == p[7] == 'O' or p[2] == p[5] == p[3] == 'O' \
                        or p[0] == p[4] == p[8] == 'O' or p[2] == p[4] == p[6] == 'O':
                    print('Победил игрок -  ' + name_2 + ' Поздравляем!')
                    s_g_2 += 1
                    round_counter += 1
                else:
                    game_round(name_1, s_g_1, name_2, s_g_2, s_g_0, p, priority, round_counter)
    else:
        return s_g_0


p1, p2, p3 = greetings()
game_master(p1, p2, p3, 0)
