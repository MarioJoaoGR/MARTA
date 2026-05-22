
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
        
        # Call the iter_lines method
        result = list(http_response.iter_lines(chunk_size=1024))
        
        # Assert that the result matches the expected output
        self.assertEqual(result, [("line1", b'\n'), ("line2", b'\n'), ("line3", b'\n')])

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_models_HTTPResponse_iter_lines_0_test_valid_input
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_models_HTTPResponse_iter_lines_0_test_valid_input.py:12:24: E1120: No value for argument 'orig' in constructor call (no-value-for-parameter)


"""