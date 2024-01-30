import unittest
from calculate import Calc


class MyTestCase(unittest.TestCase):
    def test_cal_add1(self):
        # 输入数据a, b和期望结果c
        a = 1
        b = 2
        c = 3
        # 测试结果为d
        calc = Calc()
        d = calc.add(a, b)
        self.assertEqual(c, d)  # add assertion here

    def test_cal_add2(self):
        # 输入数据a, b和期望结果c
        a = -5
        b = -5
        c = -10
        # 测试结果为d
        calc = Calc()
        d = calc.add(a, b)
        self.assertEqual(c, d)  # add assertion here

    def test_cal_add3(self):  # 测试边界值
        # 输入数据a, b和期望结果c
        a = 1000000000000000000000000000000000000000
        b = 1
        c = 1000000000000000000000000000000000000001
        # 测试结果为d
        calc = Calc()
        d = calc.add(a, b)
        self.assertEqual(c, d)  # add assertion here

    def test_cal_minus1(self):
        # 输入数据a, b和期望结果c
        a = 1
        b = 2
        c = -1
        # 测试结果为d
        calc = Calc()
        d = calc.minus(a, b)
        self.assertEqual(c, d)  # add assertion here

    def test_cal_minus2(self):
        # 输入数据a, b和期望结果c
        a = 2
        b = 1
        c = 1
        # 测试结果为d
        calc = Calc()
        d = calc.minus(a, b)
        self.assertEqual(c, d)  # add assertion here

    def test_cal_minus3(self):  # 测试边界值
        # 输入数据a, b和期望结果c
        a = 10000000000000000000000000000000000000000
        b = 9999999999999999999999999999999999999999
        c = 1
        # 测试结果为d
        calc = Calc()
        d = calc.minus(a, b)
        self.assertEqual(c, d)  # add assertion here

    def test_cal_minus4(self):  # 测试边界值
        # 输入数据a, b和期望结果c
        a = 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        b = 1
        c = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        # 测试结果为d
        calc = Calc()
        d = calc.minus(a, b)
        self.assertEqual(c, d)  # add assertion here


if __name__ == '__main__':
    unittest.main()
