
import pytest
from isort.comments import parse

def test_parse_no_comment():
    assert parse("from math import sqrt") == ('from math import sqrt', '')

def test_parse_with_comment():
    assert parse("import os # Importing operating system module") == ('import os', 'Importing operating system module')

def test_parse_only_comment():
    assert parse("# This is a comment, not an import statement") == ('', 'This is a comment, not an import statement')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

isort/Test4DT_tests/test_isort_comments_parse_0_test_edge_case_none.py . [ 33%]
F.                                                                       [100%]

=================================== FAILURES ===================================
___________________________ test_parse_with_comment ____________________________

    def test_parse_with_comment():
>       assert parse("import os # Importing operating system module") == ('import os', 'Importing operating system module')
E       AssertionError: assert ('import os '...ystem module') == ('import os',...ystem module')
E         
E         At index 0 diff: 'import os ' != 'import os'
E         Use -v to get more diff

isort/Test4DT_tests/test_isort_comments_parse_0_test_edge_case_none.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_comments_parse_0_test_edge_case_none.py::test_parse_with_comment
========================= 1 failed, 2 passed in 0.14s ==========================
"""