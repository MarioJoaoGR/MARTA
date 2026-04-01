
import pytest
from isort.core import _has_changed, remove_whitespace

@pytest.mark.parametrize("before, after, line_separator, ignore_whitespace, expected", [
    ("Hello, World!", "Hello, World!", "\n", False, False),
    (" Hello, World! ", "Hello, World!", "\n", False, True),
    ("Hello, World!", "Hello, World!", ".", True, False),
    ("Remove \n all \t newlines and tabs.", "Removeallnewlinesandtabs.", "\n", True, True),
])
def test_has_changed(before, after, line_separator, ignore_whitespace, expected):
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

isort/Test4DT_tests/test_isort_core__has_changed_0_test_error_case_type_mismatch.py . [ 25%]
F..                                                                      [100%]

=================================== FAILURES ===================================
________ test_has_changed[ Hello, World! -Hello, World!-\n-False-True] _________

before = ' Hello, World! ', after = 'Hello, World!', line_separator = '\n'
ignore_whitespace = False, expected = True

    @pytest.mark.parametrize("before, after, line_separator, ignore_whitespace, expected", [
        ("Hello, World!", "Hello, World!", "\n", False, False),
        (" Hello, World! ", "Hello, World!", "\n", False, True),
        ("Hello, World!", "Hello, World!", ".", True, False),
        ("Remove \n all \t newlines and tabs.", "Removeallnewlinesandtabs.", "\n", True, True),
    ])
    def test_has_changed(before, after, line_separator, ignore_whitespace, expected):
>       assert _has_changed(before, after, line_separator, ignore_whitespace) == expected
E       AssertionError: assert False == True
E        +  where False = _has_changed(' Hello, World! ', 'Hello, World!', '\n', False)

isort/Test4DT_tests/test_isort_core__has_changed_0_test_error_case_type_mismatch.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_core__has_changed_0_test_error_case_type_mismatch.py::test_has_changed[ Hello, World! -Hello, World!-\n-False-True]
========================= 1 failed, 3 passed in 0.12s ==========================
"""