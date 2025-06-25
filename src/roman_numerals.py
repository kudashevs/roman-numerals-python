class RomanNumerals:
    def __init__(self):
        pass

    def convert(self, amount: int) -> str:
        if amount <= 0:
            raise ValueError(f'{amount} cannot be converted a roman number')
