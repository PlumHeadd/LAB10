import unittest
from app import add_task, get_tasks  
from functions import multiply_numbers, reverse_list, calculate_discount, MathOperations


class TestMultiplyNumbers(unittest.TestCase):
    def test_two_positive_numbers(self):
        self.assertEqual(multiply_numbers(3, 5), 15)
        
    def test_multiplication_with_zero(self):
        self.assertEqual(multiply_numbers(10, 0), 0)
        self.assertEqual(multiply_numbers(0, 5), 0)
        
    def test_negative_numbers(self):
        self.assertEqual(multiply_numbers(-2, 3), -6)
        self.assertEqual(multiply_numbers(-4, -5), 20)


class TestReverseList(unittest.TestCase):
    def test_normal_list(self):
        self.assertEqual(reverse_list([1,2,3]), [3,2,1])
        
    def test_empty_list(self):
        self.assertEqual(reverse_list([]), [])
        
    def test_single_element_list(self):
        self.assertEqual(reverse_list([10]), [10])


class TestCalculateDiscount(unittest.TestCase):
    def test_valid_input(self):
        self.assertAlmostEqual(calculate_discount(100, 10), 90.0)
        self.assertAlmostEqual(calculate_discount(200, 25), 150.0)
        
    def test_invalid_discount(self):
        with self.assertRaises(ValueError):
            calculate_discount(100, -10)
        with self.assertRaises(ValueError):
            calculate_discount(100, 110)
            
    def test_zero_price_or_discount(self):
        self.assertEqual(calculate_discount(0, 50), 0)
        self.assertEqual(calculate_discount(100, 0), 100)


class TestMathOperations(unittest.TestCase):
    def setUp(self):
        self.math_ops = MathOperations()
        
    def test_is_prime(self):
        # Prime numbers
        self.assertTrue(self.math_ops.is_prime(2))
        self.assertTrue(self.math_ops.is_prime(3))
        self.assertTrue(self.math_ops.is_prime(11))
        
        # Non-prime numbers
        self.assertFalse(self.math_ops.is_prime(4))
        self.assertFalse(self.math_ops.is_prime(9))
        
        # Edge cases
        self.assertFalse(self.math_ops.is_prime(0))
        self.assertFalse(self.math_ops.is_prime(1))
        self.assertFalse(self.math_ops.is_prime(-5))
        
    def test_factorial(self):
        # Positive integers
        self.assertEqual(self.math_ops.factorial(5), 120)
        
        # Edge case: 0
        self.assertEqual(self.math_ops.factorial(0), 1)
        
        # Invalid: negative numbers
        with self.assertRaises(ValueError):
            self.math_ops.factorial(-3)

if __name__ == '__main__':
    unittest.main()
