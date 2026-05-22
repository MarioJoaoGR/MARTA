
import pytest
from unittest.mock import patch, MagicMock
from httpie.output.processing import is_valid_mime

# Define a module-level variable for MIME_RE to satisfy the function's precondition
MIME_RE = re.compile(r'^[a-zA-Z0-9/]+$')  # Example pattern, adjust as needed

@pytest.mark.parametrize("mime, expected", [
    ("image/png", True),
    ("text/html", True),
    ("application/pdf", True),
    ("invalid-mime", False),
    (None, False),
    ("", False),
])
def test_is_valid_mime_basic(mime, expected):
    with patch('httpie.output.processing.MIME_RE', MagicMock()):
        # Mock the MIME_RE to always return True for valid mimes and False otherwise
        mock_re = MagicMock()
        mock_re.match.side_effect = lambda x: bool(x in ["image/png", "text/html", "application/pdf"])
        httpie.output.processing.MIME_RE = mock_re
        
        assert is_valid_mime(mime) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_output_processing_is_valid_mime_0_test_is_valid_mime_basic
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_processing_is_valid_mime_0_test_is_valid_mime_basic.py:7:10: E0602: Undefined variable 're' (undefined-variable)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_processing_is_valid_mime_0_test_is_valid_mime_basic.py:22:8: E0602: Undefined variable 'httpie' (undefined-variable)


"""