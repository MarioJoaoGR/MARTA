
import unittest
from unittest.mock import patch
import mimetypes

def get_content_type(filename):
    """
    Return the content type for ``filename`` in format appropriate
    for Content-Type headers, or ``None`` if the file type is unknown
    to ``mimetypes``.

    """
    return mimetypes.guess_type(filename, strict=False)[0]

class TestGetContentType(unittest.TestCase):
    
    @patch('mimetypes.guess_type')
    def test_valid_input(self, mock_guess_type):
        # Mock the return value of guess_type for a known file type
        mock_guess_type.return_value = ('text/plain', None)
        
        # Test with a valid filename
        result = get_content_type("example.txt")
        self.assertEqual(result, 'text/plain')
        
        # Test with another known file type
        mock_guess_type.return_value = ('application/pdf', None)
        result = get_content_type("report.pdf")
        self.assertEqual(result, 'application/pdf')
        
        # Test with an unknown file type
        mock_guess_type.return_value = (None, None)
        result = get_content_type("unknownfile.xyz")
        self.assertIsNone(result)
