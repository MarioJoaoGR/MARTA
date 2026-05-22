
import unittest
from unittest.mock import patch
from httpie.encoding import smart_decode, detect_encoding

class TestSmartDecode(unittest.TestCase):
    def test_invalid_input(self):
        with patch('httpie.encoding.detect_encoding', return_value='utf-8'):
            content = b'\x80\x81\x82'  # Invalid byte sequence
            expected_output = ('\ufffd\ufffd\ufffd', 'utf-8')
            result = smart_decode(content, '')
            self.assertEqual(result, expected_output)
