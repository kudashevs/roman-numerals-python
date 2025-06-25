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

    def test_it_converts_21(self):
        self.assertEqual(self.converter.convert(21), 'XXI')

    def test_it_converts_40(self):
        self.assertEqual(self.converter.convert(40), 'XL')

    def test_it_converts_50(self):
        self.assertEqual(self.converter.convert(50), 'L')

    def test_it_converts_60(self):
        self.assertEqual(self.converter.convert(60), 'LX')

    def test_it_converts_90(self):
        self.assertEqual(self.converter.convert(90), 'XC')

    def test_it_converts_100(self):
        self.assertEqual(self.converter.convert(100), 'C')

    def test_it_converts_400(self):
        self.assertEqual(self.converter.convert(400), 'CD')

    def test_it_converts_500(self):
        self.assertEqual(self.converter.convert(500), 'D')

    def test_it_converts_600(self):
        self.assertEqual(self.converter.convert(600), 'DC')

    def test_it_converts_900(self):
        self.assertEqual(self.converter.convert(900), 'CM')

    def test_it_converts_1000(self):
        self.assertEqual(self.converter.convert(1000), 'M')

if __name__ == '__main__':
    unittest.main()
