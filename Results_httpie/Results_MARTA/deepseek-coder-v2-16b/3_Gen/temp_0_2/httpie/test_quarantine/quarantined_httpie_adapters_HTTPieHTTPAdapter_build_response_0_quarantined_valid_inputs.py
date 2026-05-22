
import unittest
from httpie.adapters import HTTPHeadersDict
from unittest.mock import patch, MagicMock

class TestHTTPieHTTPAdapter(unittest.TestCase):
    
    @patch('httpie.adapters.HTTPHeadersDict')
    def test_build_response_valid_inputs(self, MockHTTPHeadersDict):
        adapter = HTTPieHTTPAdapter()
        req = MagicMock()
        resp = MagicMock()
        resp.headers = {"Content-Type": "application/json", "Set-Cookie": ["cookie1=value1", "cookie2=value2"]}
        
        MockHTTPHeadersDict.return_value = HTTPHeadersDict()
        
        response = adapter.build_response(req, resp)
        
        self.assertIsInstance(response.headers, HTTPHeadersDict)
        self.assertEqual(response.headers, HTTPHeadersDict())

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_adapters_HTTPieHTTPAdapter_build_response_0_test_valid_inputs
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_adapters_HTTPieHTTPAdapter_build_response_0_test_valid_inputs.py:10:18: E0602: Undefined variable 'HTTPieHTTPAdapter' (undefined-variable)


"""