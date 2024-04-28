import re


class RomanNumber:
    roman_to_decimal = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
                        'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
                        'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}

    def __init__(self, value):
        self.rom_value = None
        self.int_value = None

        if self.is_roman(value):
            self.rom_value = value
            self.decimal_number()
        elif value.is_integer():
            self.int_value = int(value)
            self.roman_number()
        else:
            print('ошибка')

    def __add__(self, other):
        if isinstance(other, RomanNumber):
            return RomanNumber(self.int_value + other.int_value)
        else:
            raise TypeError("Unsupported operand type for +")

    def __sub__(self, other):
        if isinstance(other, RomanNumber):
            return RomanNumber(self.int_value - other.int_value)
        else:
            raise TypeError("Unsupported operand type for -")

    def __mul__(self, other):
        if isinstance(other, RomanNumber):
            return RomanNumber(self.int_value * other.int_value)
        else:
            raise TypeError("Unsupported operand type for *")

    def __truediv__(self, other):
        if isinstance(other, RomanNumber):
            return RomanNumber(self.int_value / other.int_value)
        else:
            raise TypeError("Unsupported operand type for /")

    def __floordiv__(self, other):
        if isinstance(other, RomanNumber):
            return RomanNumber(self.int_value // other.int_value)
        else:
            raise TypeError("Unsupported operand type for //")

    def __mod__(self, other):
        if isinstance(other, RomanNumber):
            return RomanNumber(self.int_value % other.int_value)
        else:
            raise TypeError("Unsupported operand type for %")

    def __pow__(self, other):
        if isinstance(other, RomanNumber):
            return RomanNumber(self.int_value ** other.int_value)
        else:
            raise TypeError("Unsupported operand type for **")

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
        self.int_value = decimal
        return decimal

    def roman_number(self):
        if self.int_value is None:
            return None
        num = self.int_value
        result = ''

        for rom, dec in self.roman_to_decimal.items():
            result += num // dec * rom
            num %= dec

        self.rom_value = result
        return result

    @staticmethod
    def is_roman(value):
        pattern = '^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
        try:
            return bool(re.match(pattern, value))
        except TypeError:
            return False

    @staticmethod
    def is_int(value):
        return 0 < value < 4000

    def __repr__(self):
        return self.rom_value if self.rom_value is not None else 'None'
