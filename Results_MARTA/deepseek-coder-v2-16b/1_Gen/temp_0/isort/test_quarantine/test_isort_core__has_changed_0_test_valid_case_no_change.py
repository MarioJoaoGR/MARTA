
import pytest
from isort.core import _has_changed

@pytest.mark.parametrize("before, after, line_separator, ignore_whitespace, expected", [
    ("Hello, World!", "Hello, World!", "\n", False, False),
    (" Hello, World! ", "Hello, World!", "\n", True, True),
    ("Hello, World!", "Hello, World!\n", ".", False, True),
    ("Hello, World!", "Hello, World!", ".", True, False),
])
def test_valid_case_no_change(before, after, line_separator, ignore_whitespace, expected):
    assert _has_changed(before, after, line_separator, ignore_whitespace) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 4 items

isort/Test4DT_tests/test_isort_core__has_changed_0_test_valid_case_no_change.py . [ 25%]
FF.                                                                      [100%]

=================================== FAILURES ===================================
____ test_valid_case_no_change[ Hello, World! -Hello, World!-\n-True-True] _____

before = ' Hello, World! ', after = 'Hello, World!', line_separator = '\n'
ignore_whitespace = True, expected = True

    @pytest.mark.parametrize("before, after, line_separator, ignore_whitespace, expected", [
        ("Hello, World!", "Hello, World!", "\n", False, False),
        (" Hello, World! ", "Hello, World!", "\n", True, True),
        ("Hello, World!", "Hello, World!\n", ".", False, True),
        ("Hello, World!", "Hello, World!", ".", True, False),
    ])
    def test_valid_case_no_change(before, after, line_separator, ignore_whitespace, expected):
>       assert _has_changed(before, after, line_separator, ignore_whitespace) == expected
E       AssertionError: assert False == True
E        +  where False = _has_changed(' Hello, World! ', 'Hello, World!', '\n', True)

isort/Test4DT_tests/test_isort_core__has_changed_0_test_valid_case_no_change.py:12: AssertionError
____ test_valid_case_no_change[Hello, World!-Hello, World!\n-.-False-True] _____

before = 'Hello, World!', after = 'Hello, World!\n', line_separator = '.'
ignore_whitespace = False, expected = True

    @pytest.mark.parametrize("before, after, line_separator, ignore_whitespace, expected", [
        ("Hello, World!", "Hello, World!", "\n", False, False),
        (" Hello, World! ", "Hello, World!", "\n", True, True),
        ("Hello, World!", "Hello, World!\n", ".", False, True),
        ("Hello, World!", "Hello, World!", ".", True, False),
    ])
    def test_valid_case_no_change(before, after, line_separator, ignore_whitespace, expected):
>       assert _has_changed(before, after, line_separator, ignore_whitespace) == expected
E       AssertionError: assert False == True
E        +  where False = _has_changed('Hello, World!', 'Hello, World!\n', '.', False)

isort/Test4DT_tests/test_isort_core__has_changed_0_test_valid_case_no_change.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_core__has_changed_0_test_valid_case_no_change.py::test_valid_case_no_change[ Hello, World! -Hello, World!-\n-True-True]
FAILED isort/Test4DT_tests/test_isort_core__has_changed_0_test_valid_case_no_change.py::test_valid_case_no_change[Hello, World!-Hello, World!\n-.-False-True]
========================= 2 failed, 2 passed in 0.11s ==========================
"""