
import unittest
from unittest.mock import patch, MagicMock
from httpie.downloads import filename_from_content_disposition

class TestHttpieDownloadsFilenameFromContentDisposition(unittest.TestCase):
    @patch('httpie.downloads.os.path.basename', return_value='jakubroztocil-httpie-0.4.1-20-g40bd8f6.tar.gz')
    def test_valid_input_happy_path(self, mock_basename):
        content_disposition = 'attachment; filename=jakubroztocil-httpie-0.4.1-20-g40bd8f6.tar.gz'
        result = filename_from_content_disposition(content_disposition)
        self.assertEqual(result, 'jakubroztocil-httpie-0.4.1-20-g40bd8f6.tar.gz')

    @patch('httpie.downloads.os.path.basename', return_value='example.txt')
    def test_valid_input_with_form_data(self, mock_basename):
        content_disposition = 'form-data; name="file"; filename=example.txt'
        result = filename_from_content_disposition(content_disposition)
        self.assertEqual(result, 'example.txt')

    @patch('httpie.downloads.os.path.basename', return_value='no-extension')
    def test_valid_input_without_extension(self, mock_basename):
        content_disposition = 'inline; filename=no-extension'
        result = filename_from_content_disposition(content_disposition)
        self.assertEqual(result, 'no-extension')

    @patch('httpie.downloads.os.path.basename', return_value='')
    def test_missing_filename(self, mock_basename):
        content_disposition = 'attachment'
        result = filename_from_content_disposition(content_disposition)
        self.assertIsNone(result)
