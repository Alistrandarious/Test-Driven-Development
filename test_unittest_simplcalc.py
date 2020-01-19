from simple_calc import SimpleCalc
import unittest


class Calctests(unittest.TestCase):

    calc = SimpleCalc()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 4), 6)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4, 2), 2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 2), 4)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 3), 2)

# Python - m unittest tests all tests in the area that I am looking. be sure to quit with quit() in the terminal. -v is
# verbose. Python is more talkative. Discover runs anything that starts with test in the filename. use pytest.

