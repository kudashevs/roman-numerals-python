import unittest
from unittest_data_provider import data_provider
from src.roman_numerals import RomanNumerals

class RomanNumeralsTest(unittest.TestCase):
    def setUp(self):
        self.converter = RomanNumerals()

    def test_it_throws_exception_when_less_than_1(self):
        with self.assertRaises(ValueError):
            self.converter.convert(0)
        with self.assertRaises(ValueError):
            self.converter.convert(-1)

if __name__ == '__main__':
    unittest.main()
