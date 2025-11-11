"""
Test-Driven Development for StringCalculator
Following TDD approach:
"""

import unittest
from string_calculator import StringCalculator


class TestStringCalculator(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.calculator = StringCalculator()
    
    def test_empty_string_returns_zero(self):
        """Test that an empty string returns 0"""
        result = self.calculator.add("")
        self.assertEqual(result, 0)
    
    def test_single_number_returns_number(self):
        """Test that a single number returns that number"""
        result = self.calculator.add("1")
        self.assertEqual(result, 1)
        
        result = self.calculator.add("5")
        self.assertEqual(result, 5)
    
    def test_two_numbers_comma_separated_returns_sum(self):
        """Test that two numbers separated by comma return their sum"""
        result = self.calculator.add("1,2")
        self.assertEqual(result, 3)
        
        result = self.calculator.add("5,7")
        self.assertEqual(result, 12)
    
    def test_multiple_numbers_comma_separated_returns_sum(self):
        """Test that multiple numbers separated by commas return their sum"""
        result = self.calculator.add("1,2,3")
        self.assertEqual(result, 6)
        
        result = self.calculator.add("1,2,3,4,5")
        self.assertEqual(result, 15)
        
        result = self.calculator.add("10,20,30")
        self.assertEqual(result, 60)
    
    def test_newline_delimiter_returns_sum(self):
        """Test that numbers separated by newlines return their sum"""
        result = self.calculator.add("1\n2,3")
        self.assertEqual(result, 6)
        
        result = self.calculator.add("1\n2\n3")
        self.assertEqual(result, 6)
    
    def test_custom_delimiter_returns_sum(self):
        """Test that custom delimiters work correctly"""
        result = self.calculator.add("//;\n1;2")
        self.assertEqual(result, 3)
        
        result = self.calculator.add("//|\n1|2|3")
        self.assertEqual(result, 6)
    
    def test_negative_numbers_throw_exception(self):
        """Test that negative numbers throw an exception with the negative numbers listed"""
        with self.assertRaises(ValueError) as context:
            self.calculator.add("-1,2")
        self.assertIn("negatives not allowed", str(context.exception))
        self.assertIn("-1", str(context.exception))
        
        with self.assertRaises(ValueError) as context:
            self.calculator.add("1,-2,-3")
        self.assertIn("negatives not allowed", str(context.exception))
        self.assertIn("-2", str(context.exception))
        self.assertIn("-3", str(context.exception))
    
    def test_numbers_bigger_than_1000_ignored(self):
        """Test that numbers bigger than 1000 are ignored"""
        result = self.calculator.add("2,1001")
        self.assertEqual(result, 2)
        
        result = self.calculator.add("1000,1001,2")
        self.assertEqual(result, 1002)  # 1000 + 2, 1001 ignored
        
        result = self.calculator.add("1,2,3000")
        self.assertEqual(result, 3)
    
    def test_delimiters_of_any_length(self):
        """Test that delimiters of any length work correctly"""
        result = self.calculator.add("//[***]\n1***2***3")
        self.assertEqual(result, 6)
        
        result = self.calculator.add("//[##]\n4##5##6")
        self.assertEqual(result, 15)
        
        result = self.calculator.add("//[delim]\n10delim20delim30")
        self.assertEqual(result, 60)
    
    def test_edge_cases(self):
        """Test edge cases for full coverage"""
        # Test mixed delimiters with default settings
        result = self.calculator.add("1,2\n3")
        self.assertEqual(result, 6)
        
        # Test empty custom delimiter format (should fallback to default)
        result = self.calculator.add("//\n1,2,3")
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()

