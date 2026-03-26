
from string_utils.errors import InvalidInputError
import pytest

def test_none_input():
    with pytest.raises(InvalidInputError) as excinfo:
        process_string(None)
    assert str(excinfo.value) == 'Expected "str", received "NoneType"'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_errors_InvalidInputError___init___0_test_none_input
python-string-utils/Test4DT_tests/test_string_utils_errors_InvalidInputError___init___0_test_none_input.py:7:8: E0602: Undefined variable 'process_string' (undefined-variable)


"""