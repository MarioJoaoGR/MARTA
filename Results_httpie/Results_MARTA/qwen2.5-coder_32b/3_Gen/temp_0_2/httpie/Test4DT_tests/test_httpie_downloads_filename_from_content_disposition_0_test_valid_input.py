
import unittest
from unittest.mock import patch, MagicMock
from httpie.downloads import filename_from_content_disposition

class TestHttpieDownloadsFilenameFromContentDisposition(unittest.TestCase):
    
    @patch('httpie.downloads.os.path.basename')
    @patch('httpie.downloads.Message')
    def test_valid_input(self, MockMessage, MockBasename):
        # Arrange
        mock_msg = MockMessage.return_value
        mock_msg.get_filename.return_value = 'jakubroztocil-httpie-0.4.1-20-g40bd8f6.tar.gz'
        
        MockBasename.return_value = 'jakubroztocil-httpie-0.4.1-20-g40bd8f6.tar.gz'
        
        # Act
        result = filename_from_content_disposition('attachment; filename=jakubroztocil-httpie-0.4.1-20-g40bd8f6.tar.gz')
        
        # Assert
        self.assertEqual(result, 'jakubroztocil-httpie-0.4.1-20-g40bd8f6.tar.gz')
        
    @patch('httpie.downloads.os.path.basename')
    @patch('httpie.downloads.Message')
    def test_valid_input_with_form_data(self, MockMessage, MockBasename):
        # Arrange
        mock_msg = MockMessage.return_value
        mock_msg.get_filename.return_value = 'example.txt'
        
        MockBasename.return_value = 'example.txt'
        
        # Act
        result = filename_from_content_disposition('form-data; name="file"; filename=example.txt')
        
        # Assert
        self.assertEqual(result, 'example.txt')
        
    @patch('httpie.downloads.os.path.basename')
    @patch('httpie.downloads.Message')
    def test_valid_input_without_extension(self, MockMessage, MockBasename):
        # Arrange
        mock_msg = MockMessage.return_value
        mock_msg.get_filename.return_value = 'no-extension'
        
        MockBasename.return_value = 'no-extension'
        
        # Act
        result = filename_from_content_disposition('inline; filename=no-extension')
        
        # Assert
        self.assertEqual(result, 'no-extension')
        
    @patch('httpie.downloads.os.path.basename')
    @patch('httpie.downloads.Message')
    def test_invalid_input(self, MockMessage, MockBasename):
        # Arrange
        mock_msg = MockMessage.return_value
        mock_msg.get_filename.return_value = None
        
        MockBasename.return_value = 'no-extension'
        
        # Act
        result = filename_from_content_disposition('attachment')
        
        # Assert
        self.assertIsNone(result)
