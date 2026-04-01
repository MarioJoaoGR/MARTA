
import pytest
from string_utils.manipulation import is_string, InvalidInputError
from __StringFormatter import __StringFormatter

def test_valid_input():
    formatter = __StringFormatter("valid string")
    assert formatter.input_string == "valid string"
    
    with pytest.raises(InvalidInputError):
        bad_formatter = __StringFormatter(12345)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___StringFormatter___fix_saxon_genitive_1_test_valid_input
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___fix_saxon_genitive_1_test_valid_input.py:4:0: E0401: Unable to import '__StringFormatter' (import-error)


"""