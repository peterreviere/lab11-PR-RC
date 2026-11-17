# https://github.com/peterreviere/lab11-PR-RC
# Partner 1: Peter Reviere
# Partner 2: Renato Corrales
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
     def test_add(self):
         self.assertEqual(add(8, 5), 13)
         self.assertEqual(add(0, 0), 0)
         self.assertEqual(add(5, 5), 10)

     def test_subtract(self):
         self.assertEqual(sub(8, 5), 3)
         self.assertEqual(sub(0, 0), 0)
         self.assertEqual(sub(5, 5), 0)

     def test_multiply(self):
         self.assertEqual(mul(8, 5), 40)
         self.assertEqual(mul(0, 0), 0)
         self.assertEqual(mul(5, 5), 25)

     def test_divide(self):
         self.assertEqual(div(5, 10), 2)
         self.assertEqual(div(1, 5), 5)
         self.assertEqual(div(5, 5), 1)

     def test_divide_by_zero(self):
         with self.assertRaises(ZeroDivisionError):
             div(0, 5)
     def test_logarithm(self):
         self.assertEqual(log(9, 3), 2)
         self.assertEqual(log(8, 2), 3)
         self.assertEqual(log(1, 10), 0)

     def test_log_invalid_base(self):
         with self.assertRaises(ValueError):
             log(5, 0)

     def test_log_invalid_argument(self):
         with self.assertRaises(ValueError):
             log(0, 5)

     def test_hypotenuse(self):
        self.assertEqual(hypotenuse(2, 2), (8 ** (1/2)))
        self.assertEqual(hypotenuse(1, 1), (2 ** (1/2)))
        self.assertEqual(hypotenuse(4, 3), 5)

     def test_sqrt(self):
         self.assertEqual(square_root(1), 1)
         self.assertEqual(square_root(4), 2)
         with self.assertRaises(ValueError):
             square_root(-1)

if __name__ == "__main__":
    unittest.main()