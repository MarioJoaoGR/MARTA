
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
        # Mock the return value of guess_type for known extensions
        mock_guess_type.return_value = ('text/plain', None)  # Example: text file
        
        # Test a valid input with a known extension
        filename = "example.txt"
        result = get_content_type(filename)
        self.assertEqual(result, 'text/plain')
        
        # Test another valid input with a different known extension
        filename = "report.pdf"
        mock_guess_type.return_value = ('application/pdf', None)  # Example: PDF file
        result = get_content_type(filename)
        self.assertEqual(result, 'application/pdf')
        
        # Test an invalid input with an unknown extension
        filename = "unknownfile.xyz"
        mock_guess_type.return_value = (None, None)  # No MIME type found
        result = get_content_type(filename)
        self.assertIsNone(result)
