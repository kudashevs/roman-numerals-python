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

    def test_it_throws_exception_when_greater_than_3999(self):
        with self.assertRaises(ValueError):
            self.converter.convert(4000)

    def test_it_converts_1(self):
        self.assertEqual(self.converter.convert(1), 'I')

    def test_it_converts_2(self):
        self.assertEqual(self.converter.convert(2), 'II')

    def test_it_converts_3(self):
        self.assertEqual(self.converter.convert(3), 'III')

    def test_it_converts_4(self):
        self.assertEqual(self.converter.convert(4), 'IV')

    def test_it_converts_5(self):
        self.assertEqual(self.converter.convert(5), 'V')

if __name__ == '__main__':
    unittest.main()
