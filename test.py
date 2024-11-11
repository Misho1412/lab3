import unittest
from calc_area import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_area_rectangle(self):
        result = self.calc.area_rectangle(5, 10)
        self.assertEqual(result, 50)

        result = self.calc.area_rectangle(3, 7)
        self.assertEqual(result, 21)

        result = self.calc.area_rectangle(0, 10)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
