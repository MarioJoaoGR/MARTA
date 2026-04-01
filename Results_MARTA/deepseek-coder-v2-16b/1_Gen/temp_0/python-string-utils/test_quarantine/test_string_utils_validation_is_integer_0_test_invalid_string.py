
import pytest
from string_utils.validation import is_integer

def test_valid_integers():
    assert is_integer('42') == True
    assert is_integer('-42') == True
    assert is_integer('+42') == True
    assert is_integer('0') == True
    assert is_integer('000') == True  # Leading zeros are allowed in integers

def test_invalid_integers():
    assert is_integer('42.0') == False
    assert is_integer('1e3') == False
    assert is_integer('abc') == False
    assert is_integer(' ') == False  # Whitespace should not be considered a valid integer
    assert is_integer('') == False  # Empty string is not an integer

def test_edge_cases():
    with pytest.raises(TypeError):  # Ensure the function does not accept non-string inputs
        is_integer(42)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

python-string-utils/Test4DT_tests/test_string_utils_validation_is_integer_0_test_invalid_string.py . [ 33%]
F.                                                                       [100%]

=================================== FAILURES ===================================
____________________________ test_invalid_integers _____________________________

    def test_invalid_integers():
        assert is_integer('42.0') == False
>       assert is_integer('1e3') == False
E       AssertionError: assert True == False
E        +  where True = is_integer('1e3')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_integer_0_test_invalid_string.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_integer_0_test_invalid_string.py::test_invalid_integers
========================= 1 failed, 2 passed in 0.03s ==========================

"""