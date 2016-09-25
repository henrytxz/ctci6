from unittest import TestCase
from Chapter16.calculator_16_26 import calculate

class TestCalculate(TestCase):
    def test_calculate(self):
        self.assertRaises(ValueError, calculate, '*3+')
        self.assertRaises(ValueError, calculate, '3//2')
        self.assertRaises(ValueError, calculate, '+=')
        self.assertRaises(ValueError, calculate, '+-')
        self.assertEquals(calculate('8*9/3'), 24)
