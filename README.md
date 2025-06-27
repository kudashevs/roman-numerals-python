# Roman Numerals kata

The goal of the kata is to create a method that converts Arabic numbers into Roman numerals.


## Instructions

Write a method `String convert(int amount)` that takes an Arabic number and converts it into an according Roman numeral
string representation. The valid numbers are from 1 to 3999 inclusive, otherwise, an error is emitted. Examples:

1 ➔ I
2 ➔ II
3 ➔ III
4 ➔ IV
5 ➔ V
9 ➔ IX
21 ➔ XXI
50 ➔ L
100 ➔ C
500 ➔ D
1000 ➔ M
3999 ➔ MMMCMXCIX


## Installation and setup

Open a terminal. Clone the repository. Change your directory to a cloned one and execute:
```
python -m venv venv
venv/Scripts/activate
pip install -r requirements.txt
python -m unittest
```
