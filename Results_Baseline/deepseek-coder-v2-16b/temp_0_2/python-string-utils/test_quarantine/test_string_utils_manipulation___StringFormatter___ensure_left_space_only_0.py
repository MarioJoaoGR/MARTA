
import base64
import zlib
import pytest
from string_utils.manipulation import StringCompressor

# Helper function to compare strings in a case-insensitive manner
def str_equal(str1, str2):
    return len(str1) == len(str2) and str1.lower() == str2.lower()

@pytest.mark.parametrize("input_string, encoding, expected", [
    ('H4sIAAAAAAAAA3NSVFVU1FQBAAAA', 'utf-8', "Hello, World!"),
    ('eNrzSM3JyddRCM8vyklRBAAfngRq', 'utf-8', "Hello, World!")
])
def test_decompress(input_string, encoding, expected):
    result = StringCompressor.decompress(input_string, encoding)
    assert str_equal(result, expected), f"Expected '{expected}', but got '{result}'"

@pytest.mark.parametrize("input_string", [
    '', None  # Empty and null strings should raise ValueError
])
def test_decompress_invalid_input(input_string):
    with pytest.raises(ValueError):
        StringCompressor.decompress(input_string)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___StringFormatter___ensure_left_space_only_0
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___ensure_left_space_only_0.py:5:0: E0611: No name 'StringCompressor' in module 'string_utils.manipulation' (no-name-in-module)

"""