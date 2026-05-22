
import unittest
from unittest.mock import patch, MagicMock
from httpie.ssl_ import HTTPieHTTPSAdapter

class TestHTTPieHTTPSAdapter(unittest.TestCase):
    
    @patch('httpie.ssl_.HTTPieHTTPSAdapter._create_ssl_context')
    def test_get_default_ciphers_names(self, mock_create_ssl_context):
        # Mock the SSL context creation with verify=False
        mock_ssl_context = MagicMock()
        mock_ssl_context.get_ciphers.return_value = [
            {'name': 'cipher1'},
            {'name': 'cipher2'}
        ]
        mock_create_ssl_context.return_value = mock_ssl_context
        
        # Call the method under test
        ciphers_names = HTTPieHTTPSAdapter.get_default_ciphers_names()
        
        # Assertions
        self.assertEqual(len(ciphers_names), 2)
        self.assertIn('cipher1', ciphers_names)
        self.assertIn('cipher2', ciphers_names)
