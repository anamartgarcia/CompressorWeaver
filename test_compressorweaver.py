# test_compressorweaver.py
"""
Tests for CompressorWeaver module.
"""

import unittest
from compressorweaver import CompressorWeaver

class TestCompressorWeaver(unittest.TestCase):
    """Test cases for CompressorWeaver class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CompressorWeaver()
        self.assertIsInstance(instance, CompressorWeaver)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CompressorWeaver()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
