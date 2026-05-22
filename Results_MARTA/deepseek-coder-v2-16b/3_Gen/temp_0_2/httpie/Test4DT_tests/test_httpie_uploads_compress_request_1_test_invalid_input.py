
import requests
import zlib
from unittest import TestCase, mock
from httpie.uploads import compress_request

class TestCompressRequest(TestCase):
    @mock.patch('httpie.uploads.zlib')
    def test_invalid_input(self, mock_zlib):
        # Arrange
        request = requests.PreparedRequest()
        request.body = b'some data'
        request.headers = {}
        
        always = True  # or False for testing different scenarios
        
        # Act
        compress_request(request, always)
        
        # Assert
        self.assertEqual(request.headers['Content-Encoding'], 'deflate')
        mock_zlib.compressobj.assert_called_once()
        mock_zlib.compressobj().compress.assert_called()
        mock_zlib.compressobj().flush.assert_called()
