import re


class RomanNumber:
    roman_to_decimal = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def __init__(self, rom_value):
        if self.is_roman(rom_value):
            self.rom_value = rom_value
        else:
            print('ошибка')
            self.rom_value = None

    def decimal_number(self):
        if self.rom_value is None:
            return None
        decimal = 0
        i = 0
        while i < len(self.rom_value):
            if (i + 1 < len(self.rom_value) and
                    self.roman_to_decimal[self.rom_value[i]] < self.roman_to_decimal[self.rom_value[i + 1]]):
                decimal += self.roman_to_decimal[self.rom_value[i + 1]] - self.roman_to_decimal[self.rom_value[i]]
                i += 2
            else:
                decimal += self.roman_to_decimal[self.rom_value[i]]
                i += 1
        return decimal

    @staticmethod
    def is_roman(value):
        pattern = '^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
        return bool(re.match(pattern, value))

    def __repr__(self):
        return self.rom_value if self.rom_value is not None else 'None'
