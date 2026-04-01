
import pytest
from string_utils.validation import is_integer

@pytest.mark.parametrize("test_input, expected", [
    ('42', True),
    ('-42', True),
    ('+42', True),
    ('0', True),
    ('-0', True),
    ('000', True),
    ('1e3', False),
    ('42.0', False),
    ('abc', False),
    ('123abc', False),
    (' ', False),
    ('', False)
])
def test_valid_integer(test_input, expected):
    assert is_integer(test_input) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 12 items

python-string-utils/Test4DT_tests/test_string_utils_validation_is_integer_0_test_valid_integer.py . [  8%]
.....F.....                                                              [100%]

=================================== FAILURES ===================================
________________________ test_valid_integer[1e3-False] _________________________

test_input = '1e3', expected = False

    @pytest.mark.parametrize("test_input, expected", [
        ('42', True),
        ('-42', True),
        ('+42', True),
        ('0', True),
        ('-0', True),
        ('000', True),
        ('1e3', False),
        ('42.0', False),
        ('abc', False),
        ('123abc', False),
        (' ', False),
        ('', False)
    ])
    def test_valid_integer(test_input, expected):
>       assert is_integer(test_input) == expected
E       AssertionError: assert True == False
E        +  where True = is_integer('1e3')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_integer_0_test_valid_integer.py:20: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_integer_0_test_valid_integer.py::test_valid_integer[1e3-False]
========================= 1 failed, 11 passed in 0.03s =========================

"""