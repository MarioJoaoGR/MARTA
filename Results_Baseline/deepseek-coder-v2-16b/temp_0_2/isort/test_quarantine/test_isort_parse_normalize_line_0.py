
import pytest
import re
from isort.parse import normalize_line

@pytest.mark.parametrize("raw_line, expected", [
    ("from .cimport some_module", ('from  cimport some_module', 'from .cimport some_module')),
    ("from . import some_module", ('from  import some_module', 'from . import some_module')),
    ("import* something", ('import * something', 'import* something')),
    ("\timport   some_module", (' import some_module', '\timport   some_module')),
])
def test_normalize_line(raw_line, expected):
    normalized_line, raw_input = normalize_line(raw_line)
    assert normalized_line == expected[0], f"Expected: '{expected[0]}' but got: '{normalized_line}'"
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

isort/Test4DT_tests/test_isort_parse_normalize_line_0.py FF.F            [100%]

=================================== FAILURES ===================================
___________ test_normalize_line[from .cimport some_module-expected0] ___________

raw_line = 'from .cimport some_module'
expected = ('from  cimport some_module', 'from .cimport some_module')

    @pytest.mark.parametrize("raw_line, expected", [
        ("from .cimport some_module", ('from  cimport some_module', 'from .cimport some_module')),
        ("from . import some_module", ('from  import some_module', 'from . import some_module')),
        ("import* something", ('import * something', 'import* something')),
        ("\timport   some_module", (' import some_module', '\timport   some_module')),
    ])
    def test_normalize_line(raw_line, expected):
        normalized_line, raw_input = normalize_line(raw_line)
>       assert normalized_line == expected[0], f"Expected: '{expected[0]}' but got: '{normalized_line}'"
E       AssertionError: Expected: 'from  cimport some_module' but got: 'from . cimport some_module'
E       assert 'from . cimport some_module' == 'from  cimport some_module'
E         
E         - from  cimport some_module
E         + from . cimport some_module
E         ?      +

isort/Test4DT_tests/test_isort_parse_normalize_line_0.py:14: AssertionError
___________ test_normalize_line[from . import some_module-expected1] ___________

raw_line = 'from . import some_module'
expected = ('from  import some_module', 'from . import some_module')

    @pytest.mark.parametrize("raw_line, expected", [
        ("from .cimport some_module", ('from  cimport some_module', 'from .cimport some_module')),
        ("from . import some_module", ('from  import some_module', 'from . import some_module')),
        ("import* something", ('import * something', 'import* something')),
        ("\timport   some_module", (' import some_module', '\timport   some_module')),
    ])
    def test_normalize_line(raw_line, expected):
        normalized_line, raw_input = normalize_line(raw_line)
>       assert normalized_line == expected[0], f"Expected: '{expected[0]}' but got: '{normalized_line}'"
E       AssertionError: Expected: 'from  import some_module' but got: 'from . import some_module'
E       assert 'from . import some_module' == 'from  import some_module'
E         
E         - from  import some_module
E         + from . import some_module
E         ?      +

isort/Test4DT_tests/test_isort_parse_normalize_line_0.py:14: AssertionError
____________ test_normalize_line[\timport   some_module-expected3] _____________

raw_line = '\timport   some_module'
expected = (' import some_module', '\timport   some_module')

    @pytest.mark.parametrize("raw_line, expected", [
        ("from .cimport some_module", ('from  cimport some_module', 'from .cimport some_module')),
        ("from . import some_module", ('from  import some_module', 'from . import some_module')),
        ("import* something", ('import * something', 'import* something')),
        ("\timport   some_module", (' import some_module', '\timport   some_module')),
    ])
    def test_normalize_line(raw_line, expected):
        normalized_line, raw_input = normalize_line(raw_line)
>       assert normalized_line == expected[0], f"Expected: '{expected[0]}' but got: '{normalized_line}'"
E       AssertionError: Expected: ' import some_module' but got: ' import   some_module'
E       assert ' import   some_module' == ' import some_module'
E         
E         -  import some_module
E         +  import   some_module
E         ?        ++

isort/Test4DT_tests/test_isort_parse_normalize_line_0.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_parse_normalize_line_0.py::test_normalize_line[from .cimport some_module-expected0]
FAILED isort/Test4DT_tests/test_isort_parse_normalize_line_0.py::test_normalize_line[from . import some_module-expected1]
FAILED isort/Test4DT_tests/test_isort_parse_normalize_line_0.py::test_normalize_line[\timport   some_module-expected3]
========================= 3 failed, 1 passed in 0.10s ==========================
"""