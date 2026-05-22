
import unittest
from unittest.mock import patch
from httpie.encoding import smart_decode, detect_encoding
from typing import Tuple, Any

ContentBytes = bytes  # Assuming ContentBytes is defined somewhere in the codebase or standard library

def test_valid_input():
    content = b'Hello, World!'
    expected_output = ('Hello, World!', 'utf-8')
    
    with patch('httpie.encoding.detect_encoding', return_value='utf-8'):
        decoded_content, detected_encoding = smart_decode(content, 'utf-8')
        
        assert isinstance(decoded_content, str), "Decoded content should be a string"
        assert isinstance(detected_encoding, str), "Detected encoding should be a string"
        assert decoded_content == expected_output[0], f"Expected {expected_output[0]} but got {decoded_content}"
        assert detected_encoding == expected_output[1], f"Expected {expected_output[1]} but got {detected_encoding}"

if __name__ == "__main__":
    test_valid_input()
