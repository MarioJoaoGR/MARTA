
import pytest
from your_module import random_string  # Replace 'your_module' with the actual module name

def test_invalid_input():
    with pytest.raises(ValueError):
        assert random_string(-1) is None
        assert random_string(0) is None
        assert random_string('a') is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_generation_random_string_1_test_invalid_input
python-string-utils/Test4DT_tests/test_string_utils_generation_random_string_1_test_invalid_input.py:3:0: E0401: Unable to import 'your_module' (import-error)


"""