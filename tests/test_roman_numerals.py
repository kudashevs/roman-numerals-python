import unittest
from unittest_data_provider import data_provider
from src.roman_numerals import RomanNumerals

class RomanNumeralsTest(unittest.TestCase):
    def setUp(self):
        self.converter = RomanNumerals()

    def test_roman_numerals_convert(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
