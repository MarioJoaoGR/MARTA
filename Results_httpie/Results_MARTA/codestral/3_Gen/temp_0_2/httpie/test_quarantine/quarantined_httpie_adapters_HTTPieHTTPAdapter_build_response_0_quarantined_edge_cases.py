
import unittest
from unittest.mock import patch, MagicMock
from httpie.adapters import HTTPHeadersDict

class TestHTTPieHTTPAdapter(unittest.TestCase):
    
    @patch('httpie.adapters.HTTPHeadersDict')
    def test_build_response(self, MockHTTPHeadersDict):
        adapter = HTTPieHTTPAdapter()
        req = MagicMock()
        resp = MagicMock()
        resp.headers = {"Content-Type": "application/json", "Set-Cookie": ["cookie1=value1", "cookie2=value2"]}
        
        # Mock the return value of getattr(resp, 'headers', {}) to be resp.headers
        mock_getattr = MagicMock(return_value=resp.headers)
        with patch('httpie.adapters.HTTPieHTTPAdapter.build_response.__globals__['getattr']', mock_getattr):
            response = adapter.build_response(req, resp)
        
        self.assertIsInstance(response.headers, HTTPHeadersDict)
        MockHTTPHeadersDict.assert_called_with(resp.headers)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_adapters_HTTPieHTTPAdapter_build_response_0_test_edge_cases
httpie/Test4DT_tests_codestral/test_httpie_adapters_HTTPieHTTPAdapter_build_response_0_test_edge_cases.py:17:20: E0001: Parsing failed: 'invalid syntax. Perhaps you forgot a comma? (Test4DT_tests_codestral.test_httpie_adapters_HTTPieHTTPAdapter_build_response_0_test_edge_cases, line 17)' (syntax-error)


"""