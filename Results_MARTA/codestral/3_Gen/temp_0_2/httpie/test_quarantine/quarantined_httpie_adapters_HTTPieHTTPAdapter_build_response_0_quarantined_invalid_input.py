
from httpie.adapters import HTTPHeadersDict
import requests
from unittest.mock import patch

class HTTPieHTTPAdapter:
    def build_response(self, req, resp):
        """Wrap the original headers with the `HTTPHeadersDict` to preserve multiple headers that have the same name."""
        
        response = super().build_response(req, resp)
        response.headers = HTTPHeadersDict(getattr(resp, 'headers', {}))
        return response

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_adapters_HTTPieHTTPAdapter_build_response_0_test_invalid_input
httpie/Test4DT_tests_codestral/test_httpie_adapters_HTTPieHTTPAdapter_build_response_0_test_invalid_input.py:10:19: E1101: Super of 'HTTPieHTTPAdapter' has no 'build_response' member (no-member)


"""