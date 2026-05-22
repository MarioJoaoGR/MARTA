
import unittest
from httpie.models import HTTPResponse
from unittest.mock import patch, MagicMock

class TestHTTPResponseIterLines(unittest.TestCase):
    def test_valid_input(self):
        # Create a mock HTTPResponse object
        mock_response = MagicMock()
        mock_response.iter_lines.return_value = ["line1", "line2", "line3"]
        
        http_response = HTTPResponse()
        http_response._orig = mock_response
        
        # Test the iter_lines method with a chunk size of 1024
        result = list(http_response.iter_lines(chunk_size=1024))
        
        # Assert that the result is as expected
        self.assertEqual(result, [("line1", b'\n'), ("line2", b'\n'), ("line3", b'\n')])

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_models_HTTPResponse_iter_lines_1_test_valid_input
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_models_HTTPResponse_iter_lines_1_test_valid_input.py:12:24: E1120: No value for argument 'orig' in constructor call (no-value-for-parameter)


"""