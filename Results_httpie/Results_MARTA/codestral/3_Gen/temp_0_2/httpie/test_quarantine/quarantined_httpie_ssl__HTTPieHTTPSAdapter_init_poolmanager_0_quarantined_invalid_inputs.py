
import unittest
from unittest.mock import patch, create_autospec
from httpie.ssl_ import create_default_context
from httpie_https_adapter import HTTPieHTTPSAdapter

class TestHTTPieHTTPSAdapter(unittest.TestCase):
    @patch('httpie.ssl_.create_default_context', autospec=True)
    def test_init_with_valid_inputs(self, mock_create_default_context):
        # Arrange
        verify = True
        ssl_version = 'TLSv1.2'
        ciphers = 'ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256'
        
        # Act
        adapter = HTTPieHTTPSAdapter(verify=verify, ssl_version=ssl_version, ciphers=ciphers)
        
        # Assert
        mock_create_default_context.assert_called_once_with()
        self.assertEqual(adapter._ssl_context, mock_create_default_context.return_value)
        self.assertTrue(adapter._ssl_context.check_hostname)
        self.assertTrue(adapter._ssl_context.verify_mode == 2)
        self.assertIn(ciphers, adapter._ssl_context.get_ciphers())
        
    @patch('httpie.ssl_.create_default_context', autospec=True)
    def test_init_without_ciphers(self, mock_create_default_context):
        # Arrange
        verify = True
        ssl_version = 'TLSv1.2'
        
        # Act
        adapter = HTTPieHTTPSAdapter(verify=verify, ssl_version=ssl_version)
        
        # Assert
        mock_create_default_context.assert_called_once_with()
        self.assertEqual(adapter._ssl_context, mock_create_default_context.return_value)
        self.assertTrue(adapter._ssl_context.check_hostname)
        self.assertTrue(adapter._ssl_context.verify_mode == 2)
        
    @patch('httpie.ssl_.create_default_context', autospec=True)
    def test_init_without_ssl_version(self, mock_create_default_context):
        # Arrange
        verify = True
        ciphers = 'ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256'
        
        # Act
        adapter = HTTPieHTTPSAdapter(verify=verify, ciphers=ciphers)
        
        # Assert
        mock_create_default_context.assert_called_once_with()
        self.assertEqual(adapter._ssl_context, mock_create_default_context.return_value)
        self.assertTrue(adapter._ssl_context.check_hostname)
        self.assertTrue(adapter._ssl_context.verify_mode == 2)
        
    @patch('httpie.ssl_.create_default_context', autospec=True)
    def test_init_without_inputs(self, mock_create_default_context):
        # Arrange
        verify = True
        
        # Act
        adapter = HTTPieHTTPSAdapter(verify=verify)
        
        # Assert
        mock_create_default_context.assert_called_once_with()
        self.assertEqual(adapter._ssl_context, mock_create_default_context.return_value)
        self.assertTrue(adapter._ssl_context.check_hostname)
        self.assertTrue(adapter._ssl_context.verify_mode == 2)
        
    def test_init_poolmanager(self):
        # Arrange
        verify = True
        ssl_version = 'TLSv1.2'
        ciphers = 'ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256'
        adapter = HTTPieHTTPSAdapter(verify=verify, ssl_version=ssl_version, ciphers=ciphers)
        
        # Act
        with patch('http.client.HTTPSConnectionPool') as mock_pool:
            adapter.init_poolmanager()
            
        # Assert
        mock_pool.assert_called_once_with(host='localhost', port=443, context=adapter._ssl_context)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_ssl__HTTPieHTTPSAdapter_init_poolmanager_0_test_invalid_inputs
httpie/Test4DT_tests_codestral/test_httpie_ssl__HTTPieHTTPSAdapter_init_poolmanager_0_test_invalid_inputs.py:4:0: E0611: No name 'create_default_context' in module 'httpie.ssl_' (no-name-in-module)
httpie/Test4DT_tests_codestral/test_httpie_ssl__HTTPieHTTPSAdapter_init_poolmanager_0_test_invalid_inputs.py:5:0: E0401: Unable to import 'httpie_https_adapter' (import-error)


"""