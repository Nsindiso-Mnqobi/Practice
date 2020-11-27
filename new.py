import math     
import unittest

def calcCircumferance(r):
    return r*2*math.pi

print(calcCircumferance(5))

class Testmathcode(unittest.TestCase):
    def test_circumference(self):
        self.assertEqual(calcCircumferance(5), 31.41592653589793)

    def test_circumference(self):
        actual = calcCircumferance(0)
        self.assertEqual(actual, 0)

    def test_circumferenceInvalid(self):
        self.assertRaises(calcCircumferance('power'))

unittest.main()