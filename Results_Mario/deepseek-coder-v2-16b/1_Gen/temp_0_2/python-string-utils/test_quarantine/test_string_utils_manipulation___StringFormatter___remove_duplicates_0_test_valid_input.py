
import pytest
from string_utils.manipulation import __StringFormatter

def test_valid_input():
    formatter = __StringFormatter("hello")
    match = re.search(r'(.*)(\1+)', formatter.input_string)
    
    if match:
        result = formatter.__remove_duplicates(match)
        assert result == 'h', f"Expected 'h' but got {result}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___StringFormatter___remove_duplicates_0_test_valid_input
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___remove_duplicates_0_test_valid_input.py:7:12: E0602: Undefined variable 're' (undefined-variable)


"""