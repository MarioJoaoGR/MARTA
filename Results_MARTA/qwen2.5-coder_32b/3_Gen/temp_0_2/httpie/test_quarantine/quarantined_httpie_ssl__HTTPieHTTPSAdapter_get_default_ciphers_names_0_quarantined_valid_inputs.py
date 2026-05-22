
import unittest
from unittest.mock import patch, MagicMock
from httpie_https_adapter import HTTPieHTTPSAdapter

class TestHTTPieHTTPSAdapter(unittest.TestCase):
    
    @patch('httpie_https_adapter.HTTPieHTTPSAdapter._create_ssl_context')
    def test_get_default_ciphers_names(self, mock_create_ssl_context):
        # Mock the SSL context creation and its get_ciphers method
        mock_ssl_context = MagicMock()
        mock_ssl_context.get_ciphers.return_value = [
            {'name': 'cipher1'},
            {'name': 'cipher2'}
        ]
        
        # Set the return value of _create_ssl_context to the mocked SSL context
        mock_create_ssl_context.return_value = mock_ssl_context
        
        # Call the method under test
        ciphers_names = HTTPieHTTPSAdapter.get_default_ciphers_names()
        
        # Assert that the returned list contains the expected cipher names
        self.assertEqual(ciphers_names, ['cipher1', 'cipher2'])

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_ssl__HTTPieHTTPSAdapter_get_default_ciphers_names_0_test_valid_inputs
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_ssl__HTTPieHTTPSAdapter_get_default_ciphers_names_0_test_valid_inputs.py:4:0: E0401: Unable to import 'httpie_https_adapter' (import-error)


"""