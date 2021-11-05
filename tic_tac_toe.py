import time
import random as rd

"""
Моя первая самостоятельная программа.

"""


def greetings():
    """
    Эта функция будет приветствовать игроков, узнавать имена, разыгрывать очередность ходов \
    и знакомить с правилами игры.
    :return: name_1, name_2
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
        p_1, p_2 = p_2, p_1
    else:
        p_3 = 1
        print('Первым ходит: ' + p_2 + '   Вторым ходит: ' + p_1)
    time.sleep(2)
    print('\n' * 100)
    return p_1, p_2


def playing_field(gamer_1, s_g_1, gamer_2, s_g_2, s_g_0, p, round_counter):
    """
    Эта функция будет создавать, обновлять и отрисовывать изменения на игровом поле.
    Print('\n'*100) --> Рисует 100 пустых строк, тем самым затирая все что было в 100 строках
    :return: none
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


def game_master(name_1, name_2):
    """
    Эта функция будет контролировать игровой процесс.
    р - это список значений клеток поля игры, для определения правильности ходов, ничьей или победы.
    s_g_0 - переменная будет хранить кол-во игр сыгранных в ничью
    s_g_1 - переменная будет хранить кол-во игр выигранных игроком_1
    s_g_2 - переменная будет хранить кол-во игр выигранных игроком_2
    round_counter - счетчик раундов

    :return: none
    """
    p = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    round_counter = 0
    s_g_0 = int(0)
    s_g_1 = int(0)
    s_g_2 = int(0)
    winner = 4
    counter = 0
    while counter <= 11:
        if round_counter % 2 != 0:
            p, winner, round_counter = game_round_odd(name_1, name_2, p, s_g_0, s_g_1, s_g_2, round_counter)
        else:
            p, winner, round_counter = game_round_even(name_1, name_2, p, s_g_0, s_g_1, s_g_2, round_counter)
        round_counter += 1
        counter += 1
        p = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        if winner == 0:
            s_g_0 += 1
        elif winner == 1:
            s_g_1 += 1
        elif winner == 2:
            s_g_2 += 1
        else:
            print('Ошибка определения победителя в game_master')
        time.sleep(3)


def game_round_odd(name_1, name_2, p, s_g_0, s_g_1, s_g_2, round_counter):
    """
    нечетный раунд
    :param name_1:
    :param name_2:
    :param p:
    :param s_g_0:
    :param s_g_1:
    :param s_g_2:
    :param round_counter:
    :return: р - список содержащий значения клеток поля
    """
    winner = 0
    turn_counter = 1
    while turn_counter < 10:
        if win(p) == 0:
            if turn_counter % 2 != 0:
                playing_field(name_1, s_g_1, name_2, s_g_2, s_g_0, p, round_counter)
                game_turn(p, name_1, 'X')
                turn_counter += 1
            else:
                playing_field(name_1, s_g_1, name_2, s_g_2, s_g_0, p, round_counter)
                game_turn(p, name_2, 'O')
                turn_counter += 1
        elif win(p) == 1:
            playing_field(name_1, s_g_1, name_2, s_g_2, s_g_0, p, round_counter)
            print('Победил игрок -  ' + name_1 + ' Поздравляем!')
            winner = 1
            return p, winner, round_counter
        elif win(p) == 2:
            playing_field(name_1, s_g_1, name_2, s_g_2, s_g_0, p, round_counter)
            print('Победил игрок -  ' + name_2 + ' Поздравляем!')
            winner = 2
            return p, winner, round_counter
        else:
            playing_field(name_1, s_g_1, name_2, s_g_2, s_g_0, p, round_counter)
            print('Ходы закончились, ничья, попробуйте сыграть еще!')
            return p, winner, round_counter
    return p


def game_round_even(name_1, name_2, p, s_g_0, s_g_1, s_g_2, round_counter):
    """
    четный раунд
    :param name_1:
    :param name_2:
    :param p:
    :param s_g_0:
    :param s_g_1:
    :param s_g_2:
    :param round_counter:
    :return: p - список содержащий значения клеток поля
    """
    winner = 0
    turn_counter = 1
    while turn_counter < 11:
        if win(p) == 0:
            if turn_counter % 2 != 0:
                playing_field(name_1, s_g_1, name_2, s_g_2, s_g_0, p, round_counter)
                game_turn(p, name_2, 'X')
                turn_counter += 1
            else:
                playing_field(name_1, s_g_1, name_2, s_g_2, s_g_0, p, round_counter)
                game_turn(p, name_1, 'O')
                turn_counter += 1
        elif win(p) == 1:
            playing_field(name_1, s_g_1, name_2, s_g_2, s_g_0, p, round_counter)
            print('Победил игрок -  ' + name_2 + ' Поздравляем!')
            winner = 2
            return p, winner, round_counter
        elif win(p) == 2:
            playing_field(name_1, s_g_1, name_2, s_g_2, s_g_0, p, round_counter)
            print('Победил игрок -  ' + name_1 + ' Поздравляем!')
            winner = 1
            return p, winner, round_counter
        else:
            playing_field(name_1, s_g_1, name_2, s_g_2, s_g_0, p, round_counter)
            print('Ходы закончились, ничья, попробуйте сыграть еще!')
            return p, winner, round_counter
    return p


def game_turn(p, name, symbol):
    """
    Функция обрабатывает ход игрока, проверяет правильность ввода и \
     добавляет в список поля крестик или нолик

    :param p: список содержащий значения клеток поля перед ходом
    :param name: имя текущего игрока
    :param symbol: крестик или нолик
    :return: р - список содержащий значения клеток поля после хода
    """
    y = '123456789'
    q = 0
    while q != 1:
        x = input('Игрок: ' + name + ', сделайте свой ход, нажмите кнопку 1-9 : ')
        if x in y and x != '':
            x = int(x)
            if p[x - 1] != ' ':
                print('Клеточка занята, выберите цифру не занятой клеточки!')
            else:
                p[x - 1] = symbol
                q = 1
                return p
        else:
            print('Вы ввели не правильное число, введите цифру от 1 до 9.')
    pass


def win(p):
    """ Функция определяет завершение раунда
    возвращаемые значения:
    принимаемое значение:
    р - список содержащий значения клеток поля
    w = 1 - победил игрок_1
    w = 2 - победил игрок_2
    w = 3 - ничья
    :return: w

    """
    w = 0
    if p[0] == p[1] == p[2] == 'X' or p[3] == p[4] == p[5] == 'X' or p[6] == p[7] == p[8] == 'X' \
            or p[0] == p[3] == p[6] == 'X' or p[1] == p[4] == p[7] == 'X' or p[2] == p[5] == p[3] == 'X' \
            or p[0] == p[4] == p[8] == 'X' or p[2] == p[4] == p[6] == 'X':
        w = 1
        return w
    elif p[0] == p[1] == p[2] == 'O' or p[3] == p[4] == p[5] == 'O' or p[6] == p[7] == p[8] == 'O' \
            or p[0] == p[3] == p[6] == 'O' or p[1] == p[4] == p[7] == 'O' or p[2] == p[5] == p[3] == 'O' \
            or p[0] == p[4] == p[8] == 'O' or p[2] == p[4] == p[6] == 'O':
        w = 2
        return w
    elif p.count(' ') == 0:
        w = 3
        return w
    else:
        return w


p1, p2 = greetings()
# print(p1, p2)
game_master(p1, p2)
