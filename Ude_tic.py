# Очистка экрана в iPython Notebook
import random

# Глобальные переменные
theBoard = [' '] * 10   # список из пробелов
available = [str(num) for num in range(0, 10)]  # Генератор списков - List Comprehension
players = [0, 'X', 'O']  # players[1] == 'X' и players[-1] == 'O'


def display_board(a, b):
    print('Возможные   Крестики-Нолики\n' +
          '  ходы\n\n  ' +
          a[7]+'|'+a[8]+'|'+a[9]+'        '+b[7]+'|'+b[8]+'|'+b[9]+'\n  ' +
          '-----        -----\n  ' +
          a[4]+'|'+a[5]+'|'+a[6]+'        '+b[4]+'|'+b[5]+'|'+b[6]+'\n  ' +
          '-----        -----\n  ' +
          a[1]+'|'+a[2]+'|'+a[3]+'        '+b[1]+'|'+b[2]+'|'+b[3]+'\n')


"""
def display_board(a, b):
    print('Возможные   Крестики-Нолики\n  ходы\n\n  {a[7]}|{a[8]}|{a[9]}        '
          '{b[7]}|{b[8]}|{b[9]}\n  -----        -----\n  {a[4]}|{a[5]}|{a[6]}        '
          '{b[4]}|{b[5]}|{b[6]}\n  -----        -----\n  {a[1]}|{a[2]}|{a[3]}        '
          '{b[1]}|{b[2]}|{b[3]}\n')
"""


def place_marker(avail, board, marker, position):
    board[position] = marker
    avail[position] = ' '


def win_check(board, mark):
    return ((board[7] == board[8] == board[9] == mark) or  # горизонталь сверху
            (board[4] == board[5] == board[6] == mark) or  # горизонталь в середине
            (board[1] == board[2] == board[3] == mark) or  # горизонталь снизу
            (board[7] == board[4] == board[1] == mark) or  # вертикаль слева
            (board[8] == board[5] == board[2] == mark) or  # вертикаль в середине
            (board[9] == board[6] == board[3] == mark) or  # вертикаль справа
            (board[7] == board[5] == board[3] == mark) or  # диагональ
            (board[9] == board[5] == board[1] == mark))  # диагональ


def random_player():
    return random.choice((-1, 1))


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    return ' ' not in board[1:]


def player_choice(board, player):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        try:
            position = int(input('Игрок %s, выберите следующую клетку: (1-9) ' % (player)))
        except:
            print("Извините, попробуйте снова.")

    return position


def replay():
    return input('Вы хотите сыграть снова? Введите Yes или No: ').lower().startswith('y')


while True:
    print('Добро пожаловать в игру Крестики-Нолики!')

    toggle = random_player()
    player = players[toggle]
    print('В этом раунде, первым ходит Игрок %s!' % (player))

    game_on = True
    input('Нажмите Enter для продолжения')
    while game_on:
        display_board(available, theBoard)
        position = player_choice(theBoard, player)
        place_marker(available, theBoard, player, position)

        if win_check(theBoard, player):
            display_board(available, theBoard)
            print('Поздравляю! Игрок ' + player + ' выиграл!')
            game_on = False
        else:
            if full_board_check(theBoard):
                display_board(available, theBoard)
                print('Ничья!')
                break
            else:
                toggle *= -1
                player = players[toggle]

    # reset the board and available moves list
    theBoard = [' '] * 10
    available = [str(num) for num in range(0, 10)]

    if not replay():
        break
