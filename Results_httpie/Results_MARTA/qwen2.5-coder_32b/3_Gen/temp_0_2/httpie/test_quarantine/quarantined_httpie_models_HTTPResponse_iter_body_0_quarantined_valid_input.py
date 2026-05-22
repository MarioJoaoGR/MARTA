
import unittest
from unittest.mock import patch, MagicMock
from httpie.models import HTTPResponse

class TestHTTPResponse(unittest.TestCase):
    def test_valid_input(self):
        # Create a mock response object from requests
        mock_response = MagicMock()
        mock_response.iter_content.return_value = ['chunk1', 'chunk2']  # Mock the iter_content method
        
        # Instantiate HTTPResponse with the mock response
        http_response = HTTPResponse(response=mock_response)
        
        # Call the iter_body method and check if it returns the expected chunks
        result = list(http_response.iter_body(chunk_size=1))
        self.assertEqual(result, ['chunk1', 'chunk2'])

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_models_HTTPResponse_iter_body_0_test_valid_input
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_models_HTTPResponse_iter_body_0_test_valid_input.py:13:24: E1123: Unexpected keyword argument 'response' in constructor call (unexpected-keyword-arg)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_models_HTTPResponse_iter_body_0_test_valid_input.py:13:24: E1120: No value for argument 'orig' in constructor call (no-value-for-parameter)


"""