
from string_utils.generation import validate
import pytest

def test_invalid_input_error_handling():
    with pytest.raises(ValueError) as excinfo:
        validate('hello', 'number')
    assert str(excinfo.value) == '"number" must be an integer in the range 1-3999'

    with pytest.raises(ValueError) as excinfo:
        validate(4000, 'year')
    assert str(excinfo.value) == '"year" must be an integer in the range 1-3999'

    with pytest.raises(ValueError) as excinfo:
        validate(-5, 'age', allow_negative=True)
    assert str(excinfo.value) == '"age" must be an integer in the range 1-3999'

    try:
        validate(2500, 'year')
    except ValueError as e:
        pytest.fail("Unexpected ValueError: {}".format(e))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_generation_validate_0_test_invalid_input_error_handling
python-string-utils/Test4DT_tests/test_string_utils_generation_validate_0_test_invalid_input_error_handling.py:2:0: E0611: No name 'validate' in module 'string_utils.generation' (no-name-in-module)


"""