board = [str(x) for x in range(1, 10)]  # Создаем импровизированную доску (список из 9 цифр (строкового типа))

win_cords = board[:3], board[3:6], board[6:], board[::3], board[1::3], board[2::3], board[::4], board[2:7:2]


def check_win(board):
    """Функиця проверки выйгрышных позиций. Возвращает Х или О"""
    win_cords = board[:3], board[3:6], board[6:], board[::3], board[1::3], board[2::3], board[::4], board[2:7:2]
    for i in win_cords:
        if all(map(lambda x: x == "X", i)):
            return f"Победил {i[0]}"
        elif all(map(lambda x: x == "O", i)):
            return f"Победил {i[0]}"
    else:
        return False


def draw_board():
    print(*board[:3], sep=' | ')
    print(*board[3:6], sep=' | ')
    print(*board[6:10], sep=' | ')


def start_game():
    print('Добро пожаловать в игру Крестики-Нолики')
    print()
    attempt = 9
    while attempt != 0 and check_win(board) is False:  # Пока функция проверки False(запускать цикл)
        draw_board()  # Нарисовать доску
        ask = input('Куда поставим "X" ? ') # Ходит Х
        print()
        if ask == '' or ask not in '123456789':
            print('Попробуйте снова')
            continue
        board[int(ask) - 1] = "X"  # Замена на игровом поле значения на Х
        attempt -= 1
        if check_win(board) is False and attempt != 0:  # Проверка. Если функция првоерки все еще False, то ходит "O"
            draw_board()
            ask = input('Куда поставим "O" ? ')
            print()
            if ask == '' or ask not in '123456789':
                print('Попробуйте снова')
                continue
            board[int(ask) - 1] = "O"
            attempt -= 1

    else:  # Если цикл While завершился
        if attempt == 0:
            draw_board()
            print('Ничья !!!')
        else:
            draw_board()
            print('-----------------')
            print(check_win(board))


while True:
    start_game()
    print('-----------------------------------')
    input('Нажмите enter, чтобы начать заного')
    print()
    board = [str(x) for x in range(1, 10)]
