
import unittest
from httpie.utils import get_content_type
from unittest.mock import patch
import mimetypes

class TestGetContentType(unittest.TestCase):
    
    @patch('httpie.utils.mimetypes')
    def test_none_input(self, mock_mimetypes):
        # Set up the mock to return None for any guess
        mock_mimetypes.guess_type.return_value = (None, None)
        
        # Call the function with a filename that doesn't have an extension
        result = get_content_type("nonexistentfile")
        
        # Assert that the function returned None
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
