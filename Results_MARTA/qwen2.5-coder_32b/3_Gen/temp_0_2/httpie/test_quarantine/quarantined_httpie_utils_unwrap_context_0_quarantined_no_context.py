
import pytest
from unittest.mock import patch
from httpie.utils import unwrap_context, CustomException

def test_no_context():
    with patch('httpie.utils.unwrap_context') as mock_unwrap:
        # Mock the behavior of unwrap_context to return None for any input
        mock_unwrap.side_effect = lambda exc: None if isinstance(exc, Exception) else exc
        
        # Create a CustomException without context
        exc = CustomException()
        
        # Call the function and check that it returns the original exception
        result = unwrap_context(exc)
        assert result is exc

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_utils_unwrap_context_0_test_no_context
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_utils_unwrap_context_0_test_no_context.py:4:0: E0611: No name 'CustomException' in module 'httpie.utils' (no-name-in-module)


"""