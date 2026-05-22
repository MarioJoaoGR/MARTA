
import unittest
from unittest.mock import patch, create_default_context
from httpie.ssl_ import HTTPieHTTPSAdapter

class TestHTTPieHTTPSAdapter(unittest.TestCase):
    @patch('httpie.ssl_.create_default_context', autospec=True)
    def test_init_poolmanager(self, mock_create_default_context):
        # Arrange
        adapter = HTTPieHTTPSAdapter(verify=True)
        
        # Act
        with patch.object(adapter, '_ssl_context') as mock_ssl_context:
            result = adapter.init_poolmanager()
            
            # Assert
            mock_create_default_context.assert_called_once_with()
            self.assertEqual(result._ssl_context, mock_ssl_context)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_ssl__HTTPieHTTPSAdapter_init_poolmanager_0_test_edge_cases
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_ssl__HTTPieHTTPSAdapter_init_poolmanager_0_test_edge_cases.py:3:0: E0611: No name 'create_default_context' in module 'unittest.mock' (no-name-in-module)


"""