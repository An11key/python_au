from HexNumber import hexn
from HexNumber import summ
import unittest

class NameTestCase(unittest.TestCase):
    def test_num1_bigger_then_num2(self):
        num1 = hexn('123F')
        num2 = hexn('45E')
        res = summ(num1, num2)
        self.assertEqual(res.num, '169D')
    def test_All_null(self):
        num1 = hexn('0')
        num2 = hexn('0')
        res = summ(num1, num2)
        self.assertEqual(res.num, '0')
    def test_num2_bigger_then_num1(self):
        num1 = hexn('0')
        num2 = hexn('45E')
        res = summ(num1, num2)
        self.assertEqual(res.num, '45E')
    def test_equel_length(self):
        num1 = hexn('123F')
        num2 = hexn('45AE')
        res = summ(num1, num2)
        self.assertEqual(res.num, '57ED')
    def test_simply_nums(self):
        num1 = hexn('2')
        num2 = hexn('4')
        res = summ(num1, num2)
        self.assertEqual(res.num, '6')
    def test_without_nums(self):
        num1 = hexn('ABC')
        num2 = hexn('FAB')
        res = summ(num1, num2)
        self.assertEqual(res.num, '1A67')


if __name__ == "__name__":
    unittest.main()