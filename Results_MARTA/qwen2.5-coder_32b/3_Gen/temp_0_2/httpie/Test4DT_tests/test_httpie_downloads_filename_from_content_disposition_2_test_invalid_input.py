
import unittest
from unittest.mock import patch
from httpie.downloads import filename_from_content_disposition

class TestHttpieDownloadsFilenameFromContentDisposition(unittest.TestCase):
    
    @patch('httpie.downloads.os')
    def test_invalid_input(self, mock_os):
        # Mock the behavior of os.path.basename to return None for any input
        mock_os.path.basename.return_value = None
        
        # Test cases with invalid inputs
        self.assertIsNone(filename_from_content_disposition('attachment'))
        self.assertIsNone(filename_from_content_disposition('form-data; name="file"; filename='))
        self.assertIsNone(filename_from_content_disposition('inline; filename='))
