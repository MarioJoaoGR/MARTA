
import pytest
from string import ascii_letters, digits
import random
from your_module import random_string  # Replace 'your_module' with the actual module name where random_string is defined.

def test_edge_case_zero():
    size = 0
    with pytest.raises(ValueError):
        random_string(size)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_generation_random_string_1_test_edge_case_zero
python-string-utils/Test4DT_tests/test_string_utils_generation_random_string_1_test_edge_case_zero.py:5:0: E0401: Unable to import 'your_module' (import-error)


"""