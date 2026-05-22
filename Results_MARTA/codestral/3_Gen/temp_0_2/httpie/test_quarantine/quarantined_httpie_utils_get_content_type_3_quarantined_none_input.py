
import mimetypes
from unittest.mock import patch

def test_none_input():
    with patch('mimetypes.guess_type') as mock_guess_type:
        mock_guess_type.return_value = None
        
        assert get_content_type(None) is None
        mock_guess_type.assert_called_once_with(None, strict=False)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_utils_get_content_type_3_test_none_input
httpie/Test4DT_tests_codestral/test_httpie_utils_get_content_type_3_test_none_input.py:9:15: E0602: Undefined variable 'get_content_type' (undefined-variable)


"""