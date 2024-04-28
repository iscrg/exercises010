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
            else:
                NavalBattle.__playing_field[y][x] = 'o'
                print('мимо')
        else:
            print('ошибка')
