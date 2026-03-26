
from python_string_utils import compress
import unittest

class TestStringUtilCompression(unittest.TestCase):
    
    def test_compress_short_string(self):
        original_length = len("aaaaaaaaaa")
        compressed = compress("aaaaaaaaaa")
        self.assertLess(len(compressed), original_length)
        
    def test_compress_random_string(self):
        original_length = len("a" * 100)  # Assuming a random string of length 100 for the purpose of this test
        compressed = compress("a" * 100)
        self.assertLess(len(compressed), original_length)
        
    def test_compress_string_with_no_repeating_sequence(self):
        original_length = len("abcdefghijklmnopqrstuvwxyz" * 5)
        compressed = compress("abcdefghijklmnopqrstuvwxyz" * 5)
        self.assertLess(len(compressed), original_length)
        
    def test_compress_string_with_utf8_encoding(self):
        original_length = len("Hello, 世界!")
        compressed = compress("Hello, 世界!")
        self.assertLess(len(compressed), original_length)

if __name__ == '__main__':
    unittest.main()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation_compress_0
python-string-utils/Test4DT_tests/test_string_utils_manipulation_compress_0.py:2:0: E0401: Unable to import 'python_string_utils' (import-error)

"""