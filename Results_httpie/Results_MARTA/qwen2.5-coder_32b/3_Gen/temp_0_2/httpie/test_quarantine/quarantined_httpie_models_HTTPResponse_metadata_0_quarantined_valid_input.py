
import unittest
from unittest.mock import patch
from httpie.models import HTTPResponse

class TestHTTPResponseMetadata(unittest.TestCase):
    def test_valid_input(self):
        # Define a mock elapsed time for testing purposes
        ELAPSED_TIME_LABEL = 'Elapsed Time'
        
        class MockResponse:
            elapsed = type('elapsed', (object,), {'total_seconds': lambda self: 1.234567})()
            
            def __init__(self):
                self._httpie_headers_parsed_at = 0.0
        
        mock_response = MockResponse()
        http_response = HTTPResponse(mock_response)
        
        with patch('httpie.models.monotonic', return_value=123456789):
            result = http_response.metadata()
        
        expected_result = '\n'.join([f'{ELAPSED_TIME_LABEL}: 1.234567s'])
        self.assertEqual(result, expected_result)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_models_HTTPResponse_metadata_0_test_valid_input
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_models_HTTPResponse_metadata_0_test_valid_input.py:21:21: E1102: http_response.metadata is not callable (not-callable)


"""