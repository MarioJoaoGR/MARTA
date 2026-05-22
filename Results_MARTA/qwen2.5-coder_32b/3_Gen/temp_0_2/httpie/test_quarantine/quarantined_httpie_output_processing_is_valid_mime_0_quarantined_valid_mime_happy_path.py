
import re
from unittest.mock import patch, MagicMock
import pytest

# Assuming MIME_RE is a module-level variable that should be mocked
MIME_RE = re.compile(r'^[a-zA-Z]+/[a-zA-Z0-9-+.]+$')

def is_valid_mime(mime):
    return mime and MIME_RE.match(mime)

@patch('httpie.output.processing.MIME_RE', MagicMock())
def test_valid_mime_happy_path():
    # Mocking the MIME_RE to always match
    httpie.output.processing.MIME_RE.return_value = True
    
    assert is_valid_mime("image/png") == True
    assert is_valid_mime("text/html") == True
    assert is_valid_mime("application/pdf") == True
    assert is_valid_mime("invalid-mime") == False

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_output_processing_is_valid_mime_0_test_valid_mime_happy_path
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_processing_is_valid_mime_0_test_valid_mime_happy_path.py:15:4: E0602: Undefined variable 'httpie' (undefined-variable)


"""