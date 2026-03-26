
import pytest
from string_utils.validation import is_number

@pytest.mark.parametrize("test_input, expected", [
    ('42', False),
    ('-42', False),
    ('+42', False),
    ('42.0', False),
    ('1e3', False),
    ('abc', False),
    ('123.45e6', False),
    ('-123.45e6', False),
    ('+123.45e6', False)
])
def test_invalid_float(test_input, expected):
    assert is_number(test_input) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 9 items

python-string-utils/Test4DT_tests/test_string_utils_validation_is_integer_0_test_invalid_float.py F [ 11%]
FFFF.FFF                                                                 [100%]

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
        ('123.45e6', False),
        ('-123.45e6', False),
        ('+123.45e6', False)
    ])
    def test_invalid_float(test_input, expected):
>       assert is_number(test_input) == expected
E       AssertionError: assert True == False
E        +  where True = is_number('42')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_integer_0_test_invalid_float.py:17: AssertionError
________________________ test_invalid_float[-42-False] _________________________

test_input = '-42', expected = False

    @pytest.mark.parametrize("test_input, expected", [
        ('42', False),
        ('-42', False),
        ('+42', False),
        ('42.0', False),
        ('1e3', False),
        ('abc', False),
        ('123.45e6', False),
        ('-123.45e6', False),
        ('+123.45e6', False)
    ])
    def test_invalid_float(test_input, expected):
>       assert is_number(test_input) == expected
E       AssertionError: assert True == False
E        +  where True = is_number('-42')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_integer_0_test_invalid_float.py:17: AssertionError
________________________ test_invalid_float[+42-False] _________________________

test_input = '+42', expected = False

    @pytest.mark.parametrize("test_input, expected", [
        ('42', False),
        ('-42', False),
        ('+42', False),
        ('42.0', False),
        ('1e3', False),
        ('abc', False),
        ('123.45e6', False),
        ('-123.45e6', False),
        ('+123.45e6', False)
    ])
    def test_invalid_float(test_input, expected):
>       assert is_number(test_input) == expected
E       AssertionError: assert True == False
E        +  where True = is_number('+42')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_integer_0_test_invalid_float.py:17: AssertionError
________________________ test_invalid_float[42.0-False] ________________________

test_input = '42.0', expected = False

    @pytest.mark.parametrize("test_input, expected", [
        ('42', False),
        ('-42', False),
        ('+42', False),
        ('42.0', False),
        ('1e3', False),
        ('abc', False),
        ('123.45e6', False),
        ('-123.45e6', False),
        ('+123.45e6', False)
    ])
    def test_invalid_float(test_input, expected):
>       assert is_number(test_input) == expected
E       AssertionError: assert True == False
E        +  where True = is_number('42.0')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_integer_0_test_invalid_float.py:17: AssertionError
________________________ test_invalid_float[1e3-False] _________________________

test_input = '1e3', expected = False

    @pytest.mark.parametrize("test_input, expected", [
        ('42', False),
        ('-42', False),
        ('+42', False),
        ('42.0', False),
        ('1e3', False),
        ('abc', False),
        ('123.45e6', False),
        ('-123.45e6', False),
        ('+123.45e6', False)
    ])
    def test_invalid_float(test_input, expected):
>       assert is_number(test_input) == expected
E       AssertionError: assert True == False
E        +  where True = is_number('1e3')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_integer_0_test_invalid_float.py:17: AssertionError
______________________ test_invalid_float[123.45e6-False] ______________________

test_input = '123.45e6', expected = False

    @pytest.mark.parametrize("test_input, expected", [
        ('42', False),
        ('-42', False),
        ('+42', False),
        ('42.0', False),
        ('1e3', False),
        ('abc', False),
        ('123.45e6', False),
        ('-123.45e6', False),
        ('+123.45e6', False)
    ])
    def test_invalid_float(test_input, expected):
>       assert is_number(test_input) == expected
E       AssertionError: assert True == False
E        +  where True = is_number('123.45e6')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_integer_0_test_invalid_float.py:17: AssertionError
_____________________ test_invalid_float[-123.45e6-False] ______________________

test_input = '-123.45e6', expected = False

    @pytest.mark.parametrize("test_input, expected", [
        ('42', False),
        ('-42', False),
        ('+42', False),
        ('42.0', False),
        ('1e3', False),
        ('abc', False),
        ('123.45e6', False),
        ('-123.45e6', False),
        ('+123.45e6', False)
    ])
    def test_invalid_float(test_input, expected):
>       assert is_number(test_input) == expected
E       AssertionError: assert True == False
E        +  where True = is_number('-123.45e6')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_integer_0_test_invalid_float.py:17: AssertionError
_____________________ test_invalid_float[+123.45e6-False] ______________________

test_input = '+123.45e6', expected = False

    @pytest.mark.parametrize("test_input, expected", [
        ('42', False),
        ('-42', False),
        ('+42', False),
        ('42.0', False),
        ('1e3', False),
        ('abc', False),
        ('123.45e6', False),
        ('-123.45e6', False),
        ('+123.45e6', False)
    ])
    def test_invalid_float(test_input, expected):
>       assert is_number(test_input) == expected
E       AssertionError: assert True == False
E        +  where True = is_number('+123.45e6')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_integer_0_test_invalid_float.py:17: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_integer_0_test_invalid_float.py::test_invalid_float[42-False]
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_integer_0_test_invalid_float.py::test_invalid_float[-42-False]
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_integer_0_test_invalid_float.py::test_invalid_float[+42-False]
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_integer_0_test_invalid_float.py::test_invalid_float[42.0-False]
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_integer_0_test_invalid_float.py::test_invalid_float[1e3-False]
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_integer_0_test_invalid_float.py::test_invalid_float[123.45e6-False]
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_integer_0_test_invalid_float.py::test_invalid_float[-123.45e6-False]
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_integer_0_test_invalid_float.py::test_invalid_float[+123.45e6-False]
========================= 8 failed, 1 passed in 0.03s ==========================
"""