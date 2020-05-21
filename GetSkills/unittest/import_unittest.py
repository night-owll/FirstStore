import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        c=Calculator(1,2)
        result=c.add()
        self.assertEqual(result,10)

if __name__ == "__main__":
    unittest.main()