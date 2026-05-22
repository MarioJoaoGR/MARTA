
import pytest
from unittest.mock import patch, MagicMock
from httpie.output.processing import MIME_RE

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
        assert is_valid_mime(mime) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_output_processing_is_valid_mime_1_test_is_valid_mime_basic
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_processing_is_valid_mime_1_test_is_valid_mime_basic.py:16:15: E0602: Undefined variable 'is_valid_mime' (undefined-variable)


"""