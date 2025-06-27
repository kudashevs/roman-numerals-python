class RomanNumerals:
    _GLYPHS = [
        (5, 'V'),
        (4, 'IV'),
        (1, 'I'),
    ]

    def __init__(self):
        pass

    def convert(self, amount: int) -> str:
        if amount <= 0 or amount >= 4000:
            raise ValueError(f'{amount} cannot be converted a roman number')

        return self._convert_to_roman(amount)


    def _convert_to_roman(self, amount: int) -> str:
        if amount <= 0:
            return ''

        for arabic, roman in self._GLYPHS:
            if amount >= arabic:
               return roman + self._convert_to_roman(amount - arabic)
