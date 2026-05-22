
import unittest.mock as mock
from httpie.ssl_ import HTTPieHTTPSAdapter

class TestHTTPieHTTPSAdapter(unittest.TestCase):
    
    @mock.patch('httpie.ssl_.SSLContext')
    def test_get_default_ciphers_names(self, MockSSLContext):
        # Arrange
        mock_context = MockSSLContext.return_value
        mock_context.get_ciphers.return_value = [
            {'name': 'cipher1'},
            {'name': 'cipher2'}
        ]
        
        class DummyHTTPieHTTPSAdapter(HTTPieHTTPSAdapter):
            _create_ssl_context = lambda self, verify, ssl_version, ciphers: mock_context
        
        # Act
        default_ciphers = DummyHTTPieHTTPSAdapter.get_default_ciphers_names()
        
        # Assert
        self.assertEqual(default_ciphers, ['cipher1', 'cipher2'])

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_ssl__HTTPieHTTPSAdapter_get_default_ciphers_names_0_test_edge_cases
httpie/Test4DT_tests_codestral/test_httpie_ssl__HTTPieHTTPSAdapter_get_default_ciphers_names_0_test_edge_cases.py:5:29: E0602: Undefined variable 'unittest' (undefined-variable)


"""