
import pytest
from unittest.mock import patch
from httpie.adapters import HTTPHeadersDict, HTTPieHTTPAdapter
from requests import Request, Response

class TestHTTPieHTTPAdapter:
    
    @patch('httpie.adapters.HTTPHeadersDict')
    def test_build_response_valid_inputs(self, mock_headersdict):
        adapter = HTTPieHTTPAdapter()
        
        # Create a mock request and response object
        req = Request("GET", "http://example.com")
        resp = Response()
        resp.headers = {"Content-Type": "application/json", "Set-Cookie": ["cookie1=value1", "cookie2=value2"]}
        
        # Call the build_response method
        response = adapter.build_response(req, resp)
        
        assert isinstance(response.headers, HTTPHeadersDict)
        assert len(response.headers) == 3  # Including 'Set-Cookie' which has multiple values

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_adapters_HTTPieHTTPAdapter_build_response_1_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
____________ TestHTTPieHTTPAdapter.test_build_response_valid_inputs ____________

self = <test_httpie_adapters_HTTPieHTTPAdapter_build_response_1_test_valid_inputs.TestHTTPieHTTPAdapter object at 0x7fc6a53fd9d0>
mock_headersdict = <MagicMock name='HTTPHeadersDict' id='140491145276176'>

    @patch('httpie.adapters.HTTPHeadersDict')
    def test_build_response_valid_inputs(self, mock_headersdict):
        adapter = HTTPieHTTPAdapter()
    
        # Create a mock request and response object
        req = Request("GET", "http://example.com")
        resp = Response()
        resp.headers = {"Content-Type": "application/json", "Set-Cookie": ["cookie1=value1", "cookie2=value2"]}
    
        # Call the build_response method
        response = adapter.build_response(req, resp)
    
>       assert isinstance(response.headers, HTTPHeadersDict)
E       AssertionError: assert False
E        +  where False = isinstance(<MagicMock name='HTTPHeadersDict()' id='140491145332240'>, HTTPHeadersDict)
E        +    where <MagicMock name='HTTPHeadersDict()' id='140491145332240'> = <Response [None]>.headers

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_adapters_HTTPieHTTPAdapter_build_response_1_test_valid_inputs.py:21: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_adapters_HTTPieHTTPAdapter_build_response_1_test_valid_inputs.py::TestHTTPieHTTPAdapter::test_build_response_valid_inputs
============================== 1 failed in 0.18s ===============================
"""