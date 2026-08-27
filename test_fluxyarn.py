# test_fluxyarn.py
"""
Tests for FluxYarn module.
"""

import unittest
from fluxyarn import FluxYarn

class TestFluxYarn(unittest.TestCase):
    """Test cases for FluxYarn class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = FluxYarn()
        self.assertIsInstance(instance, FluxYarn)
        
    def test_run_method(self):
        """Test the run method."""
        instance = FluxYarn()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
