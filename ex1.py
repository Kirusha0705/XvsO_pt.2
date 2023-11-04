# board = [str(x) for x in range(1, 10)]  #Создаем импровизированную доску (список из 9 цифр (строкового типа))


def draw_board():
    print(*board[:3], sep= ' | ')
    print(*board[3:6], sep= ' | ')
    print(*board[6:10], sep= ' | ')

def check_win(a):
    "Функция проверяет выйигрышные комбинации."
    if a == 'O':
        return a == 'O'
    else:
        return a == 'X'

def check_win2(*args):
    for i in args:
        if i == True:
            return f'Кажеться у нас есть победитель {i}'
        else:
            continue

board = [str(x) for x in range(1, 10)]

row1 = all(map(check_win, board[:3]))  #123
row2 = all(map(check_win, board[3:6]))  #456
row3 = all(map(check_win, board[6:]))  #789
col1 = all(map(check_win, board[::3]))  #147
col2 = all(map(check_win, board[1::3]))  #258
col3 = all(map(check_win, board[2::3]))  #369
diag1 = all(map(check_win, board[::4]))  #159
diag2 = all(map(check_win, board[2::2]))  #357

def start_game():
    print('Добро пожаловать в игру Крестики-Нолики')

    #В while нужно запихнуть условие пока строки столцы и диагонали не заполнены Х или О
    win_cords = [row1, row2, row3, col1, col2, col3, diag1, diag2]
    win = any(map(lambda x: x == True, win_cords))  #Любая из выйгрышных позиций True, изначально все False
    while win == False:
        draw_board()
        ask = int(input('Куда поставим "X" ? '))
        board.pop(ask - 1)
        board.insert(ask - 1, 'X')
        draw_board()

        ask = int(input('Куда поставим "O" ? '))
        board.pop(ask - 1)
        board.insert(ask - 1, 'O')
    else:
        print('ничья!')


while True:
    start_game()
    print('-----------------------------------')
    input('Нажмите enter, чтобы начать заного')





