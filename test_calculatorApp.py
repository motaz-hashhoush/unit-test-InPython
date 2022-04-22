import unittest
from unittest.mock import patch
from calculatorApp import *


class TestCalculate(unittest.TestCase):

    def setUp(self):
        print("Setup start")
        self.patcher_divide = patch('calculatorApp.divide', return_value=1)
        self.MockClass1 = self.patcher_divide.start()
        self.addCleanup(self.patcher_divide.stop)

    def test_check_user_input(self):
        self.assertRaises(ValueError, check_user_input, 'ops')
        self.assertRaises(ValueError, check_user_input, '')
        self.assertEqual(check_user_input("1.5"), 1.5)

    def test_AddPass(self):
        self.assertEqual(calculate('1', 6, 3), 9)

    def test_subtract(self):
        self.assertEqual(calculate('2', 3, 3), 0)

    def test_multiply(self):
        self.assertEqual(calculate('3', 3, 3), (3, '*', 3, '=', 9))

    def test_divide(self):
        self.assertRaises(ZeroDivisionError, divide, 0, 0)
        self.assertEqual(divide(0, 1), 0)
        self.assertEqual(divide(1, 1), 1)

    def test_calculate(self):
        self.assertRaises(Exception, calculate, '9', 1, 2)
        self.assertRaises(ValueError, calculate, '9', '', '')
        self.assertRaises(ZeroDivisionError, calculate, '4', '1', '0')
        self.assertEqual(calculate('4', '1', '2'), (1, '/', 2, '=', 1))

    def test_isExit(self):
        self.assertTrue(isExit('no'))
        self.assertFalse(isExit('yes'))
        self.assertRaises(ValueError, isExit, '1')


if __name__ == '__main__':
    unittest.main()
