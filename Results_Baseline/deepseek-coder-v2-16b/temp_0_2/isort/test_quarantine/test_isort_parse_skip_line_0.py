
from isort.parse import skip_line

def test_skip_line_inside_quotes():
    result = skip_line('print("Hello, World!")', '"', 0, ())
    assert result == (False, '"')

def test_skip_line_contains_comment():
    result = skip_line('# This is a comment\nprint("Hello")', '', 0, ())
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

isort/Test4DT_tests/test_isort_parse_skip_line_0.py F.                   [100%]

=================================== FAILURES ===================================
_________________________ test_skip_line_inside_quotes _________________________

    def test_skip_line_inside_quotes():
        result = skip_line('print("Hello, World!")', '"', 0, ())
>       assert result == (False, '"')
E       assert (True, '"') == (False, '"')
E         
E         At index 0 diff: True != False
E         Use -v to get more diff

isort/Test4DT_tests/test_isort_parse_skip_line_0.py:6: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_parse_skip_line_0.py::test_skip_line_inside_quotes
========================= 1 failed, 1 passed in 0.10s ==========================
"""