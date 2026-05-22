
import mimetypes
from unittest.mock import patch

def test_valid_input():
    with patch('mimetypes.guess_type') as mock_guess_type:
        # Set up the mock to return a known content type for valid file extensions
        mock_guess_type.return_value = ('text/plain', None)
        
        # Test cases
        assert get_content_type("example.txt") == 'text/plain'
        assert get_content_type("report.pdf") == 'application/pdf'  # Assuming this is a known MIME type
        assert get_content_type("unknownfile.xyz") is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_utils_get_content_type_5_test_valid_input
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_utils_get_content_type_5_test_valid_input.py:11:15: E0602: Undefined variable 'get_content_type' (undefined-variable)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_utils_get_content_type_5_test_valid_input.py:12:15: E0602: Undefined variable 'get_content_type' (undefined-variable)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_utils_get_content_type_5_test_valid_input.py:13:15: E0602: Undefined variable 'get_content_type' (undefined-variable)


"""