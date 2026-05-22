
import pytest
from unittest.mock import patch, MagicMock
from httpie.output.processing import is_valid_mime

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
        # The mock object should be accessible here as httpie.output.processing.MIME_RE
        if mime:
            httpie.output.processing.MIME_RE.match.return_value = True
        else:
            httpie.output.processing.MIME_RE.match.return_value = None
        
        assert is_valid_mime(mime) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_output_processing_is_valid_mime_0_test_is_valid_mime_basic
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_processing_is_valid_mime_0_test_is_valid_mime_basic.py:18:12: E0602: Undefined variable 'httpie' (undefined-variable)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_processing_is_valid_mime_0_test_is_valid_mime_basic.py:20:12: E0602: Undefined variable 'httpie' (undefined-variable)


"""