
import unittest
from unittest.mock import patch, MagicMock
from httpie.ssl_ import HTTPieHTTPSAdapter

class TestHTTPieHTTPSAdapter(unittest.TestCase):
    
    @patch('httpie.ssl_.HTTPieHTTPSAdapter._create_ssl_context')
    def test_get_default_ciphers_names(self, mock_create_ssl_context):
        # Mock the SSL context creation and its get_ciphers method
        mock_ssl_context = MagicMock()
        mock_ssl_context.get_ciphers.return_value = [
            {'name': 'cipher1'},
            {'name': 'cipher2'}
        ]
        mock_create_ssl_context.return_value = mock_ssl_context
        
        # Call the method under test
        ciphers = HTTPieHTTPSAdapter.get_default_ciphers_names()
        
        # Assert that the mocked methods were called correctly
        mock_create_ssl_context.assert_called_once_with(verify=False)
        self.assertEqual(len(ciphers), 2)
        self.assertIn('cipher1', ciphers)
        self.assertIn('cipher2', ciphers)
