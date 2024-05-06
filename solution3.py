import random


class NavalBattle:
    """
    The NavalBattle class represents a game of naval battle. It has a playing field represented as a 2D list.
    """
    playing_field = [[0] * 10 for _ in range(10)]
    __playing_field = [['~'] * 10 for _ in range(10)]

    def __init__(self, symbol: str):
        """
        Initializes a NavalBattle object.

        :param symbol: A string representing the symbol to use for hits on the playing field.
        :return: None
        """
        self.symbol = symbol

    @staticmethod
    def show():
        """
        Prints the current state of the playing field.

        :return: None
        """
        for line in NavalBattle.__playing_field:
            print(" ".join(line))

    def shot(self, x: int, y: int):
        """
        Takes a shot at the specified coordinates on the playing field.

        :param x: The x-coordinate of the shot.
        :param y: The y-coordinate of the shot.
        :return: None
        """
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
    def __capacity_check(x: int, y: int, size: int, is_horizontal: bool):
        """
        Checks if a ship of a given size can be placed at the specified coordinates on the playing field.

        :param x: The x-coordinate of the top-left corner of the ship.
        :param y: The y-coordinate of the top-left corner of the ship.
        :param size: The size of the ship.
        :param is_horizontal: True if the ship is placed horizontally, False if it's placed vertically.
        :return: True if the ship can be placed, False otherwise.
        """
        if is_horizontal:
            if x + size <= 9:
                return True

        if not is_horizontal:
            if y + size <= 9:
                return True

        return False

    @staticmethod
    def __intersection_check(x: int, y: int, size: int, is_horizontal: bool):
        """
        Checks if a ship of a given size intersects with any existing ships on the playing field.

        :param x: The x-coordinate of the top-left corner of the ship.
        :param y: The y-coordinate of the top-left corner of the ship.
        :param size: The size of the ship.
        :param is_horizontal: True if the ship is placed horizontally, False if it's placed vertically.
        :return: True if the ship does not intersect with any existing ships, False otherwise.
        """
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
    def __touch_check(x: int, y: int, size: int, is_horizontal: bool):
        """
        Checks if a ship of a given size touches any existing ships on the playing field.

        :param x: The x-coordinate of the top-left corner of the ship.
        :param y: The y-coordinate of the top-left corner of the ship.
        :param size: The size of the ship.
        :param is_horizontal: True if the ship is placed horizontally, False if it's placed vertically.
        :return: True if the ship does not touch any existing ships, False otherwise.
        """
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
    def __place(x: int, y: int, size: int, is_horizontal: bool):
        """
        Places a ship of a given size at the specified coordinates on the playing field.

        :param x: The x-coordinate of the top-left corner of the ship.
        :param y: The y-coordinate of the top-left corner of the ship.
        :param size: The size of the ship.
        :param is_horizontal: True if the ship is placed horizontally, False if it's placed vertically.
        """
        if is_horizontal:
            for i in range(x, x+size):
                NavalBattle.playing_field[y][i] = 1
        else:
            for i in range(y, y+size):
                NavalBattle.playing_field[i][x] = 1

    @staticmethod
    def new_game():
        """
        Starts a new game of naval battle. This method resets the playing field and randomly places ships.

        :return: None
        """
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
