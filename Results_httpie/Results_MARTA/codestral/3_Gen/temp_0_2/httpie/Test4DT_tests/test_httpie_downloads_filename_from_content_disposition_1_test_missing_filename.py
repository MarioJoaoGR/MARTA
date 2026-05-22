
import unittest
from httpie.downloads import filename_from_content_disposition
from unittest.mock import patch, MagicMock

class TestHttpieDownloadsFilenameFromContentDisposition(unittest.TestCase):
    
    @patch('httpie.downloads.os.path.basename', return_value='example.txt')
    def test_missing_filename(self, mock_basename):
        # Test when the filename is missing in the Content-Disposition header
        content_disposition = 'form-data; name="file"'
        result = filename_from_content_disposition(content_disposition)
        self.assertIsNone(result)

    @patch('httpie.downloads.os.path.basename', return_value='jakubroztocil-httpie-0.4.1-20-g40bd8f6.tar.gz')
    def test_valid_filename(self, mock_basename):
        # Test when the filename is present and valid in the Content-Disposition header
        content_disposition = 'attachment; filename=jakubroztocil-httpie-0.4.1-20-g40bd8f6.tar.gz'
        result = filename_from_content_disposition(content_disposition)
        self.assertEqual(result, 'jakubroztocil-httpie-0.4.1-20-g40bd8f6.tar.gz')

    @patch('httpie.downloads.os.path.basename', return_value='no-extension')
    def test_filename_with_no_extension(self, mock_basename):
        # Test when the filename has no extension
        content_disposition = 'inline; filename=no-extension'
        result = filename_from_content_disposition(content_disposition)
        self.assertEqual(result, 'no-extension')
