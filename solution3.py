import random


class NavalBattle:
    playing_field = [[0] * 10 for _ in range(10)]
    __playing_field = [['~'] * 10 for _ in range(10)]

    def __init__(self, symbol):
        """
        :param symbol:
        """
        self.symbol = symbol

    @staticmethod
    def show():
        for line in NavalBattle.__playing_field:
            print(" ".join(line))

    def shot(self, x, y):
        x -= 1
        y -= 1

        if NavalBattle.__playing_field[y][x] == '~':
            if NavalBattle.playing_field[y][x] == 1:
                NavalBattle.__playing_field[y][x] = self.symbol
                print('попал')
            elif NavalBattle.playing_field[x - 1][y - 1] == 'o' or NavalBattle.playing_field[x - 1][
                y - 1] == self.symbol:
                print('ошибка')
            else:
                NavalBattle.__playing_field[y][x] = 'o'
                print('мимо')
        else:
            print('ошибка')

    @staticmethod
    def __capacity_check(x, y, size, is_horizontal):
        if is_horizontal:
            if x + size <= 9:
                return True

        if not is_horizontal:
            if y + size <= 9:
                return True

        return False

    @staticmethod
    def __intersection_check(x, y, size, is_horizontal):
        if is_horizontal:
            for i in range(x, x+size+1):
                if NavalBattle.playing_field[y][i] == 1:
                    return False
        if not is_horizontal:
            for i in range(y, y+size+1):
                if NavalBattle.playing_field[i][x] == 1:
                    return False
        return True

    @staticmethod
    def __touch_check(x, y, size, is_horizontal):
        if is_horizontal:
            for i in range(x, x+size):
                try:
                    if NavalBattle.playing_field[y-1][i] == 1:
                        return False
                except IndexError:
                    pass

                try:
                    if NavalBattle.playing_field[y+1][i] == 1:
                        return False
                except IndexError:
                    pass

            try:
                if NavalBattle.playing_field[y+1][x+size+1] == 1:
                    return False
            except IndexError:
                pass

            try:
                if NavalBattle.playing_field[y][x+size+1] == 1:
                    return False
            except IndexError:
                pass

            try:
                if NavalBattle.playing_field[y-1][x+size+1] == 1:
                    return False
            except IndexError:
                pass

            try:
                if NavalBattle.playing_field[y-1][x-1] == 1:
                    return False
            except IndexError:
                pass

            try:
                if NavalBattle.playing_field[y][x-1] == 1:
                    return False
            except IndexError:
                pass

            try:
                if NavalBattle.playing_field[y+1][x-1] == 1:
                    return False
            except IndexError:
                pass

        if not is_horizontal:
            for i in range(y, y+size):
                try:
                    if NavalBattle.playing_field[i][x-1] == 1:
                        return False
                except IndexError:
                    pass

                try:
                    if NavalBattle.playing_field[i][x+1] == 1:
                        return False
                except IndexError:
                    pass

            try:
                if NavalBattle.playing_field[y+size+1][x+1] == 1:
                    return False
            except IndexError:
                pass

            try:
                if NavalBattle.playing_field[y+size+1][x] == 1:
                    return False
            except IndexError:
                pass

            try:
                if NavalBattle.playing_field[y+size+1][x-1] == 1:
                    return False
            except IndexError:
                pass

            try:
                if NavalBattle.playing_field[y-1][x-1] == 1:
                    return False
            except IndexError:
                pass

            try:
                if NavalBattle.playing_field[y-1][x] == 1:
                    return False
            except IndexError:
                pass

            try:
                if NavalBattle.playing_field[y-1][x+1] == 1:
                    return False
            except IndexError:
                pass

        return True

    @staticmethod
    def __place(x, y, size, is_horizontal):
        if is_horizontal:
            for i in range(x, x+size):
                NavalBattle.playing_field[y][i] = 1
        else:
            for i in range(y, y+size):
                NavalBattle.playing_field[i][x] = 1

    @staticmethod
    def new_game():
        NavalBattle.playing_field = [[0] * 10 for _ in range(10)]
        NavalBattle.__playing_field = [['~'] * 10 for _ in range(10)]
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        is_horizontal = random.randint(0, 1)

        sizes = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

        for size in sizes:
            while not (NavalBattle.__capacity_check(x, y, size, is_horizontal) and
                        NavalBattle.__intersection_check(x, y, size, is_horizontal) and
                        NavalBattle.__touch_check(x, y, size, is_horizontal)):
                    x = random.randint(0, 9)
                    y = random.randint(0, 9)
                    is_horizontal = random.randint(0, 1)
            else:
                NavalBattle.__place(x, y, size, is_horizontal)
