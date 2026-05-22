
import unittest
from httpie.ssl_ import HTTPieHTTPSAdapter
from unittest.mock import patch, create_default_context

class TestHTTPieHTTPSAdapter(unittest.TestCase):
    @patch('httpie.ssl_.create_default_context')
    def test_create_ssl_context(self, mock_create_default_context):
        # Arrange
        verify = True
        ssl_version = 'TLSv1.2'
        ciphers = 'ECDHE-RSA-AES256-GCM-SHA384'
        
        expected_ssl_context = create_default_context()
        mock_create_default_context.return_value = expected_ssl_context
        
        # Act
        adapter = HTTPieHTTPSAdapter(verify=verify, ssl_version=ssl_version, ciphers=ciphers)
        
        # Assert
        self.assertEqual(adapter._ssl_context, expected_ssl_context)
        mock_create_default_context.assert_called_once_with(
            cafile=None, capath=None, cadata=None, purpose=create_default_context().__getattribute__,
            ssl_version='TLSv1.2', ciphers='ECDHE-RSA-AES256-GCM-SHA384'
        )

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_ssl__HTTPieHTTPSAdapter_proxy_manager_for_1_test_edge_cases
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_ssl__HTTPieHTTPSAdapter_proxy_manager_for_1_test_edge_cases.py:4:0: E0611: No name 'create_default_context' in module 'unittest.mock' (no-name-in-module)


"""