
from string_utils.generation import roman_range
import pytest

def test_invalid_inputs():
    with pytest.raises(ValueError):
        list(roman_range(-1))  # stop must be within 1-3999

    with pytest.raises(ValueError):
        list(roman_range(4000))  # stop must be within 1-3999

    with pytest.raises(ValueError):
        list(roman_range(start=0))  # start must be >= 1

    with pytest.raises(ValueError):
        list(roman_range(start=-1))  # start must be >= 1

    with pytest.raises(ValueError):
        list(roman_range(step='a'))  # step must be an integer

    with pytest.raises(OverflowError):
        list(roman_range(stop=1, step=2))  # invalid start/stop/step configuration for forward iteration

    with pytest.raises(OverflowError):
        list(roman_range(stop=3999, step=-2))  # invalid start/stop/step configuration for backward iteration

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_generation_roman_range_1_test_invalid_inputs
python-string-utils/Test4DT_tests/test_string_utils_generation_roman_range_1_test_invalid_inputs.py:13:13: E1120: No value for argument 'stop' in function call (no-value-for-parameter)
python-string-utils/Test4DT_tests/test_string_utils_generation_roman_range_1_test_invalid_inputs.py:16:13: E1120: No value for argument 'stop' in function call (no-value-for-parameter)
python-string-utils/Test4DT_tests/test_string_utils_generation_roman_range_1_test_invalid_inputs.py:19:13: E1120: No value for argument 'stop' in function call (no-value-for-parameter)


"""