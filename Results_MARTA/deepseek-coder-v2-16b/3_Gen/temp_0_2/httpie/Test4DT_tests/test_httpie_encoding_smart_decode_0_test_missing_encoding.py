
import unittest
from unittest.mock import patch, MagicMock
from httpie.encoding import smart_decode

class TestSmartDecode(unittest.TestCase):
    @patch('httpie.encoding.detect_encoding')
    def test_missing_encoding(self, mock_detect_encoding):
        # Mock the detect_encoding function to return a default encoding if not provided
        mock_detect_encoding.return_value = 'utf-8'
        
        content = b'Hello, World!'
        expected_output = ('Hello, World!', 'utf-8')
        
        # Call the smart_decode function with no encoding specified
        result = smart_decode(content, '')
        
        self.assertEqual(result, expected_output)
