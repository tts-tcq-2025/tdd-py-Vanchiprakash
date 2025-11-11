"""
Additional tests to achieve 100% coverage
"""

import unittest
from string_calculator import StringCalculator


class TestStringCalculatorEdgeCases(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.calculator = StringCalculator()
    
    def test_normalize_delimiters_with_none(self):
        """Test _normalize_delimiters when delimiters parameter is None"""
        # This will test the internal method with None parameter
        result = self.calculator._normalize_delimiters("1,2\n3", None)
        self.assertEqual(result, "1,2,3")
    
    def test_invalid_custom_delimiter_format(self):
        """Test invalid custom delimiter formats"""
        # Test custom delimiter without newline - should be treated as numbers
        with self.assertRaises(ValueError):
            # This should fail because "//;" is not a valid number
            self.calculator.add("//;")


if __name__ == '__main__':
    unittest.main()
