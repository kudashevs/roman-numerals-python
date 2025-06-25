class RomanNumerals:
    _GLYPHS = [
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I'),
    ]

    def __init__(self):
        pass

    def convert(self, amount: int) -> str:
        if amount <= 0 or amount >= 4000:
            raise ValueError(f'{amount} cannot be converted a roman number')

        result = ''
        for arabic, roman in RomanNumerals._GLYPHS:
            while amount >= arabic:
                result += roman
                amount -= arabic

        return result