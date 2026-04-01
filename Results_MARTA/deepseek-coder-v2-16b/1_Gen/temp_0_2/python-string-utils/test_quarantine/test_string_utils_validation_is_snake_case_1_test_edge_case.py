
import re
from string_utils.validation import is_snake_case
import pytest

@pytest.mark.parametrize("input_string, expected", [
    ('foo_bar_baz', True),
    ('foo', False),
    ('Foo_Bar_Baz', False),  # Contains uppercase letters
    ('1foo_bar_baz', False),  # Starts with a number
    ('foo-bar-baz', False),   # Uses dash instead of underscore
    ('foo_bar_baz123', True) # Contains digits
])
def test_edge_case(input_string, expected):
    assert is_snake_case(input_string) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 6 items

python-string-utils/Test4DT_tests/test_string_utils_validation_is_snake_case_1_test_edge_case.py . [ 16%]
.F...                                                                    [100%]

=================================== FAILURES ===================================
______________________ test_edge_case[Foo_Bar_Baz-False] _______________________

input_string = 'Foo_Bar_Baz', expected = False

    @pytest.mark.parametrize("input_string, expected", [
        ('foo_bar_baz', True),
        ('foo', False),
        ('Foo_Bar_Baz', False),  # Contains uppercase letters
        ('1foo_bar_baz', False),  # Starts with a number
        ('foo-bar-baz', False),   # Uses dash instead of underscore
        ('foo_bar_baz123', True) # Contains digits
    ])
    def test_edge_case(input_string, expected):
>       assert is_snake_case(input_string) == expected
E       AssertionError: assert True == False
E        +  where True = is_snake_case('Foo_Bar_Baz')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_snake_case_1_test_edge_case.py:15: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_snake_case_1_test_edge_case.py::test_edge_case[Foo_Bar_Baz-False]
========================= 1 failed, 5 passed in 0.04s ==========================
"""