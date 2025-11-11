#!/usr/bin/env python3

"""
Test runner for StringCalculator
This file is expected by the GitHub Actions workflow
"""

import unittest
import sys
import os

# Add current directory to path to import our modules
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import all our test modules
from test_string_calculator import TestStringCalculator
from test_edge_cases import TestStringCalculatorEdgeCases

if __name__ == '__main__':
    # Create test loader
    loader = unittest.TestLoader()
    
    # Create test suite
    test_suite = unittest.TestSuite()
    
    # Add all test cases from our test classes
    test_suite.addTest(loader.loadTestsFromTestCase(TestStringCalculator))
    test_suite.addTest(loader.loadTestsFromTestCase(TestStringCalculatorEdgeCases))
    
    # Run the tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    # Exit with proper code
    sys.exit(0 if result.wasSuccessful() else 1)
