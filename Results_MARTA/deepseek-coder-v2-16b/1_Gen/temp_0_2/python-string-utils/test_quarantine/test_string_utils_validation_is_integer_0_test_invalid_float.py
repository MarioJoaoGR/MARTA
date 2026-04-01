
import pytest
from string_utils.validation import is_integer, is_number

@pytest.mark.parametrize("test_input, expected", [
    ('42', False),
    ('-42', False),
    ('+42', False),
    ('42.0', False),
    ('1e3', False),
    ('abc', False),
    (' ', False),
    ('', False),
])
def test_invalid_float(test_input, expected):
    assert is_integer(test_input) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 8 items

python-string-utils/Test4DT_tests/test_string_utils_validation_is_integer_0_test_invalid_float.py F [ 12%]
FF.F...                                                                  [100%]

=================================== FAILURES ===================================
_________________________ test_invalid_float[42-False] _________________________

test_input = '42', expected = False

    @pytest.mark.parametrize("test_input, expected", [
        ('42', False),
        ('-42', False),
        ('+42', False),
        ('42.0', False),
        ('1e3', False),
        ('abc', False),
        (' ', False),
        ('', False),
    ])
    def test_invalid_float(test_input, expected):
>       assert is_integer(test_input) == expected
E       AssertionError: assert True == False
E        +  where True = is_integer('42')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_integer_0_test_invalid_float.py:16: AssertionError
________________________ test_invalid_float[-42-False] _________________________

test_input = '-42', expected = False

    @pytest.mark.parametrize("test_input, expected", [
        ('42', False),
        ('-42', False),
        ('+42', False),
        ('42.0', False),
        ('1e3', False),
        ('abc', False),
        (' ', False),
        ('', False),
    ])
    def test_invalid_float(test_input, expected):
>       assert is_integer(test_input) == expected
E       AssertionError: assert True == False
E        +  where True = is_integer('-42')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_integer_0_test_invalid_float.py:16: AssertionError
________________________ test_invalid_float[+42-False] _________________________

test_input = '+42', expected = False

    @pytest.mark.parametrize("test_input, expected", [
        ('42', False),
        ('-42', False),
        ('+42', False),
        ('42.0', False),
        ('1e3', False),
        ('abc', False),
        (' ', False),
        ('', False),
    ])
    def test_invalid_float(test_input, expected):
>       assert is_integer(test_input) == expected
E       AssertionError: assert True == False
E        +  where True = is_integer('+42')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_integer_0_test_invalid_float.py:16: AssertionError
________________________ test_invalid_float[1e3-False] _________________________

test_input = '1e3', expected = False

    @pytest.mark.parametrize("test_input, expected", [
        ('42', False),
        ('-42', False),
        ('+42', False),
        ('42.0', False),
        ('1e3', False),
        ('abc', False),
        (' ', False),
        ('', False),
    ])
    def test_invalid_float(test_input, expected):
>       assert is_integer(test_input) == expected
E       AssertionError: assert True == False
E        +  where True = is_integer('1e3')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_integer_0_test_invalid_float.py:16: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_integer_0_test_invalid_float.py::test_invalid_float[42-False]
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_integer_0_test_invalid_float.py::test_invalid_float[-42-False]
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_integer_0_test_invalid_float.py::test_invalid_float[+42-False]
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_integer_0_test_invalid_float.py::test_invalid_float[1e3-False]
========================= 4 failed, 4 passed in 0.04s ==========================
"""