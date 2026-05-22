
import unittest
from unittest.mock import patch
from httpie.encoding import smart_decode, detect_encoding
from typing import Tuple, Union

ContentBytes = bytes

def test_valid_input():
    content = b'Hello, World!'
    expected_output = ('Hello, World!', 'utf-8')
    
    with patch('httpie.encoding.detect_encoding', return_value='utf-8'):
        result = smart_decode(content, 'utf-8')
        assert result == expected_output
