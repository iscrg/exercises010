import re


class RomanNumber:
    """
    The RomanNumber class represents a Roman numeral. It provides methods for validating and converting Roman numerals.
    """
    roman_to_decimal = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
                        'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
                        'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}

    def __init__(self, value):
        """
        Initializes a RomanNumber object.

        :param value: A string representing a Roman numeral or an integer.
        :return: None
        """
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
        """
        Adds this RomanNumber to another RomanNumber.

        :param other: The other RomanNumber.
        :return: A new RomanNumber representing the sum.
        """
        if isinstance(other, RomanNumber):
            return RomanNumber(self.int_value + other.int_value)
        else:
            raise TypeError("Unsupported operand type for +")

    def __sub__(self, other):
        """
        Subtracts another RomanNumber from this RomanNumber.

        :param other: The other RomanNumber.
        :return: A new RomanNumber representing the difference.
        """
        if isinstance(other, RomanNumber):
            return RomanNumber(self.int_value - other.int_value)
        else:
            raise TypeError("Unsupported operand type for -")

    def __mul__(self, other):
        """
        Multiplies this RomanNumber by another RomanNumber.

        :param other: The other RomanNumber.
        :return: A new RomanNumber representing the product.
        """
        if isinstance(other, RomanNumber):
            return RomanNumber(self.int_value * other.int_value)
        else:
            raise TypeError("Unsupported operand type for *")

    def __truediv__(self, other):
        """
        Divides this RomanNumber by another RomanNumber.

        :param other: The other RomanNumber.
        :return: A new RomanNumber representing the quotient.
        """
        if isinstance(other, RomanNumber):
            return RomanNumber(self.int_value / other.int_value)
        else:
            raise TypeError("Unsupported operand type for /")

    def __floordiv__(self, other):
        """
        Performs floor division of this RomanNumber by another RomanNumber.

        :param other: The other RomanNumber.
        :return: A new RomanNumber representing the result of floor division.
        """
        if isinstance(other, RomanNumber):
            return RomanNumber(self.int_value // other.int_value)
        else:
            raise TypeError("Unsupported operand type for //")

    def __mod__(self, other):
        """
        Calculates the modulus of this RomanNumber by another RomanNumber.

        :param other: The other RomanNumber.
        :return: A new RomanNumber representing the modulus.
        """
        if isinstance(other, RomanNumber):
            return RomanNumber(self.int_value % other.int_value)
        else:
            raise TypeError("Unsupported operand type for %")

    def __pow__(self, other):
        """
        Raises this RomanNumber to the power of another RomanNumber.

        :param other: The other RomanNumber.
        :return: A new RomanNumber representing the result of the power operation.
        """
        if isinstance(other, RomanNumber):
            return RomanNumber(self.int_value ** other.int_value)
        else:
            raise TypeError("Unsupported operand type for **")

    def decimal_number(self):
        """
        Converts the Roman numeral to a decimal number.

        :return: The decimal number equivalent of the Roman numeral, or None if no Roman numeral is set.
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
        self.int_value = decimal
        return decimal

    def roman_number(self):
        """
        Converts the decimal number to a Roman numeral.

        :return: The Roman numeral equivalent of the decimal number, or None if no decimal number is set.
        """
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
        """
        Checks if a string is a valid Roman numeral.

        :param value: The string to check.
        :return: True if the string is a valid Roman numeral, False otherwise.
        """
        pattern = '^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
        try:
            return bool(re.match(pattern, value))
        except TypeError:
            return False

    @staticmethod
    def is_int(value):
        """
        Checks if a value is a valid integer for conversion to a Roman numeral.

        :param value: The value to check.
        :return: True if the value is a valid integer, False otherwise.
        """
        return 0 < value < 4000

    def __repr__(self):
        """
        Returns a string representation of the Roman numeral.

        :return: The Roman numeral as a string, or 'None' if no Roman numeral is set.
        """
        return self.rom_value if self.rom_value is not None else 'None'
