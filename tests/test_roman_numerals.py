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

    def test_it_converts_6(self):
        self.assertEqual(self.converter.convert(6), 'VI')

    def test_it_converts_7(self):
        self.assertEqual(self.converter.convert(7), 'VII')

    def test_it_converts_8(self):
        self.assertEqual(self.converter.convert(8), 'VIII')

    def test_it_converts_9(self):
        self.assertEqual(self.converter.convert(9), 'IX')

    def test_it_converts_10(self):
        self.assertEqual(self.converter.convert(10), 'X')

if __name__ == '__main__':
    unittest.main()
