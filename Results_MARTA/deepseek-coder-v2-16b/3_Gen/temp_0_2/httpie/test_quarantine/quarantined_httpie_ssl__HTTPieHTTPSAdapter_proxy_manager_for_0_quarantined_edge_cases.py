
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
        
        # Act
        adapter = HTTPieHTTPSAdapter(verify=verify, ssl_version=ssl_version, ciphers=ciphers)
        
        # Assert
        mock_create_default_context.assert_called_once_with()
        self.assertEqual(adapter._ssl_context, mock_create_default_context.return_value)
        self.assertEqual(adapter._ssl_context.verify_mode, create_default_context().CERT_REQUIRED if verify else create_default_context().CERT_NONE)
        self.assertEqual(adapter._ssl_context.ssl_version, getattr(ssl, ssl_version))
        self.assertEqual(adapter._ssl_context.ciphers, ciphers)

    @patch('httpie.ssl_.create_default_context')
    def test_proxy_manager_for(self, mock_create_default_context):
        # Arrange
        adapter = HTTPieHTTPSAdapter(verify=True)
        
        # Act
        manager = adapter.proxy_manager_for()
        
        # Assert
        self.assertEqual(manager['ssl_context'], adapter._ssl_context)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_ssl__HTTPieHTTPSAdapter_proxy_manager_for_0_test_edge_cases
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_ssl__HTTPieHTTPSAdapter_proxy_manager_for_0_test_edge_cases.py:4:0: E0611: No name 'create_default_context' in module 'unittest.mock' (no-name-in-module)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_ssl__HTTPieHTTPSAdapter_proxy_manager_for_0_test_edge_cases.py:22:25: E1101: Instance of 'SSLContext' has no 'ssl_version' member (no-member)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_ssl__HTTPieHTTPSAdapter_proxy_manager_for_0_test_edge_cases.py:22:67: E0602: Undefined variable 'ssl' (undefined-variable)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_ssl__HTTPieHTTPSAdapter_proxy_manager_for_0_test_edge_cases.py:23:25: E1101: Instance of 'SSLContext' has no 'ciphers' member (no-member)


"""