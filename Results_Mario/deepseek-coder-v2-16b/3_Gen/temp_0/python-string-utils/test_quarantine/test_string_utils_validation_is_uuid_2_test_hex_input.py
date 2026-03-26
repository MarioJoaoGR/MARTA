
from unittest.mock import patch, MagicMock
import re
import pytest
from string_utils.validation import UUID_RE, UUID_HEX_OK_RE
from your_module_containing_is_uuid import is_uuid

@pytest.fixture(autouse=True)
def mock_regex():
    with patch('string_utils.validation.UUID_RE', MagicMock()) as mock_uuid_re, \
         patch('string_utils.validation.UUID_HEX_OK_RE', MagicMock()) as mock_hex_ok_re:
        yield

def test_is_uuid_standard():
    assert is_uuid('6f8aa2f9-686c-4ac3-8766-5712354a04cf') == True
    mock_uuid_re.assert_called_with(r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}')

def test_is_uuid_hex():
    assert is_uuid('6f8aa2f9686c4ac387665712354a04cf', allow_hex=True) == True
    mock_hex_ok_re.assert_called_with(r'[0-9a-f]{32}')

def test_is_uuid_invalid():
    assert is_uuid('invalid') == False

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation_is_uuid_2_test_hex_input
python-string-utils/Test4DT_tests/test_string_utils_validation_is_uuid_2_test_hex_input.py:6:0: E0401: Unable to import 'your_module_containing_is_uuid' (import-error)
python-string-utils/Test4DT_tests/test_string_utils_validation_is_uuid_2_test_hex_input.py:16:4: E0602: Undefined variable 'mock_uuid_re' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_validation_is_uuid_2_test_hex_input.py:20:4: E0602: Undefined variable 'mock_hex_ok_re' (undefined-variable)


"""