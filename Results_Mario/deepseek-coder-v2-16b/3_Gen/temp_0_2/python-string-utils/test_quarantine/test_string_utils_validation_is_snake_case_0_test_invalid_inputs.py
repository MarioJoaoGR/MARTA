
import pytest
from string_utils.validation import is_snake_case

@pytest.mark.parametrize("test_input, separator, expected", [
    ('foo_bar_baz', '_', True),
    ('Foo_Bar', '_', False),  # Contains uppercase letters
    ('123_foo', '_', False),   # Starts with a number
    ('foo-bar_baz', '-', True),  # Uses '-' as separator
    (None, '_', False),         # None input
    ('', '_', False),           # Empty string
    ('foo_bar_baz123', '_', True),  # Contains numbers but valid snake case
])
def test_invalid_inputs(test_input, separator, expected):
    assert is_snake_case(test_input, separator) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 7 items

python-string-utils/Test4DT_tests/test_string_utils_validation_is_snake_case_0_test_invalid_inputs.py . [ 14%]
F.F...                                                                   [100%]

=================================== FAILURES ===================================
_____________________ test_invalid_inputs[Foo_Bar-_-False] _____________________

test_input = 'Foo_Bar', separator = '_', expected = False

    @pytest.mark.parametrize("test_input, separator, expected", [
        ('foo_bar_baz', '_', True),
        ('Foo_Bar', '_', False),  # Contains uppercase letters
        ('123_foo', '_', False),   # Starts with a number
        ('foo-bar_baz', '-', True),  # Uses '-' as separator
        (None, '_', False),         # None input
        ('', '_', False),           # Empty string
        ('foo_bar_baz123', '_', True),  # Contains numbers but valid snake case
    ])
    def test_invalid_inputs(test_input, separator, expected):
>       assert is_snake_case(test_input, separator) == expected
E       AssertionError: assert True == False
E        +  where True = is_snake_case('Foo_Bar', '_')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_snake_case_0_test_invalid_inputs.py:15: AssertionError
___________________ test_invalid_inputs[foo-bar_baz---True] ____________________

test_input = 'foo-bar_baz', separator = '-', expected = True

    @pytest.mark.parametrize("test_input, separator, expected", [
        ('foo_bar_baz', '_', True),
        ('Foo_Bar', '_', False),  # Contains uppercase letters
        ('123_foo', '_', False),   # Starts with a number
        ('foo-bar_baz', '-', True),  # Uses '-' as separator
        (None, '_', False),         # None input
        ('', '_', False),           # Empty string
        ('foo_bar_baz123', '_', True),  # Contains numbers but valid snake case
    ])
    def test_invalid_inputs(test_input, separator, expected):
>       assert is_snake_case(test_input, separator) == expected
E       AssertionError: assert False == True
E        +  where False = is_snake_case('foo-bar_baz', '-')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_snake_case_0_test_invalid_inputs.py:15: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_snake_case_0_test_invalid_inputs.py::test_invalid_inputs[Foo_Bar-_-False]
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_snake_case_0_test_invalid_inputs.py::test_invalid_inputs[foo-bar_baz---True]
========================= 2 failed, 5 passed in 0.04s ==========================
"""