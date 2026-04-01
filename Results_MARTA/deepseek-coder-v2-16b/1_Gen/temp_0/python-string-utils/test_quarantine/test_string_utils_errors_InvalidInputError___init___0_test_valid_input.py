
from string_utils.errors import InvalidInputError

def test_valid_input():
    with pytest.raises(InvalidInputError) as excinfo:
        process_string("not a string")
    assert str(excinfo.value) == 'Expected "str", received "{}"'.format(type("not a string").__name__)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_errors_InvalidInputError___init___0_test_valid_input
python-string-utils/Test4DT_tests/test_string_utils_errors_InvalidInputError___init___0_test_valid_input.py:5:9: E0602: Undefined variable 'pytest' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_errors_InvalidInputError___init___0_test_valid_input.py:6:8: E0602: Undefined variable 'process_string' (undefined-variable)

"""