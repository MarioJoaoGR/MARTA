
import unittest
from unittest.mock import patch, MagicMock
from httpie.downloads import filename_from_content_disposition

class TestHttpieDownloadsFilenameFromContentDisposition(unittest.TestCase):
    @patch('httpie.downloads.os')
    def test_edge_case_none(self, mock_os):
        # Mock the Message class and its get_filename method
        msg = MagicMock()
        msg.get_filename.return_value = None
        
        with patch('httpie.downloads.Message', return_value=msg):
            result = filename_from_content_disposition('attachment')
            self.assertIsNone(result)
