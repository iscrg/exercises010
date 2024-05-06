import re


class RomanNumber:
    """
    The RomanNumber class represents a Roman numeral. It provides methods for validating and converting Roman numerals.
    """
    roman_to_decimal = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def __init__(self, rom_value):
        """
        Initializes a RomanNumber object.

        :param rom_value: A string representing a Roman numeral.
        :return: None
        """
        if self.is_roman(rom_value):
            self.rom_value = rom_value
        else:
            print('ошибка')
            self.rom_value = None

    def decimal_number(self):
        """
        Converts the Roman numeral to a decimal number.

        :return: The decimal number equivalent of the Roman numeral.
        """
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
        """
        Checks if a string is a valid Roman numeral.

        :param value: The string to check.
        :return: True if the string is a valid Roman numeral, False otherwise.
        """
        pattern = '^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
        return bool(re.match(pattern, value))

    def __repr__(self):
        """
        Returns a string representation of the Roman numeral.

        :return: The Roman numeral as a string.
        """
        return self.rom_value if self.rom_value is not None else 'None'
