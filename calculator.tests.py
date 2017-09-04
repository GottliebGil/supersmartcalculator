import unittest
import calculator


class CalculatorTests(unittest.TestCase):
    def testPlus(self):
        arg = '1+2'
        res = calculator.main(arg)
        res = float(res)
        self.failUnlessEqual(res, 3)

    def testMinus(self):
        arg = '1-2'
        res = calculator.main(arg)
        res = float(res)
        self.failUnlessEqual(res, -1)

    def test_times(self):
        arg = '5*4'
        res = calculator.main(arg)
        res = float(res)
        self.failUnlessEqual(res, 20)

    def test_parentheses(self):
        arg = '5*(2+1)'
        res = calculator.main(arg)
        res = float(res)
        self.failUnlessEqual(res, 15)

    def test_nested_parentheses(self):
        arg = '5*(2+(3*2))'
        res = calculator.main(arg)
        res = float(res)
        self.failUnlessEqual(res, 40)

    def test_multiple_parentheses(self):
        arg = '(3+5)*(1+2)'
        res = calculator.main(arg)
        res = float(res)
        self.failUnlessEqual(res, 24)
    
    def test_tons_of_stuff(self):
        arg = '(5*(2+4)-9*5*2*(-1))+10'
        res = calculator.main(arg)
        res = float(res)
        self.failUnlessEqual(res, 130)


def main():
    unittest.main()


if __name__ == '__main__':
    print 'start testing'
    main()