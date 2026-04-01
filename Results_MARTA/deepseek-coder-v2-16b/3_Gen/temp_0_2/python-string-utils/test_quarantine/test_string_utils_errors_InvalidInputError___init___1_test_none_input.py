
from string_utils.errors import InvalidInputError

def test_none_input():
    try:
        process_string(None)
    except InvalidInputError as e:
        assert str(e) == 'Expected "str", received "NoneType"'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_errors_InvalidInputError___init___1_test_none_input
python-string-utils/Test4DT_tests/test_string_utils_errors_InvalidInputError___init___1_test_none_input.py:6:8: E0602: Undefined variable 'process_string' (undefined-variable)


"""