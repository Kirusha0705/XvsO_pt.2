

def draw_board():
    "Функция возвращает список из цифр(строк) от 1 до 9"
    board = [str(x) for x in range(1, 10)]
    return board

def check_win():
    pass


def start_game():
    board = draw_board()  #Присваиваю переменной board список [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print('Добро пожаловать в игру Крестики-Нолики')
    print('Это ваше поле')
    print('--------------')
    print(*board[:3], sep=' | ')  #Срез 1, 2, 3
    print(*board[3:6], sep=' | ')
    print(*board[6:10], sep=' | ')
    print('--------------')

    #В while нужно запихнуть условие пока строки столцы и диагонали не заполнены Х или О
    a = 1
    while a > 0:







        a -= 1



    else:
        print('ничья!')





while True:
    start_game()
    print('-----------------------------------')
    input('Нажмите enter, чтобы начать заного')



