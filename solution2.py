class NavalBattle:
    """
    The NavalBattle class represents a game of naval battle. It has a playing field represented as a 2D list.
    """
    playing_field = [[0] * 10 for _ in range(10)]
    __playing_field = [['~'] * 10 for _ in range(10)]

    def __init__(self, symbol):
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

    def shot(self, x, y):
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
            else:
                NavalBattle.__playing_field[y][x] = 'o'
                print('мимо')
        else:
            print('ошибка')
