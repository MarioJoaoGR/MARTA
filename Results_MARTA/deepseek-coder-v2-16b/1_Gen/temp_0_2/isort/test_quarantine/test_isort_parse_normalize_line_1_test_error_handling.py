
import pytest
from unittest.mock import patch
import re
from isort.parse import normalize_line

@pytest.mark.parametrize("raw_line, expected", [
    ("from .cimport some_module", ('from  cimport some_module', 'from .cimport some_module')),
    ("from ..import some_module", ('from  import some_module', 'from ..import some_module')),
    ("\tfrom   import\tsome_module", ('from  import some_module', '\tfrom   import\tsome_module'))
])
def test_normalize_line(raw_line, expected):
    with patch('builtins.print') as mock_print:
        normalized_line, original_line = normalize_line(raw_line)
        assert normalized_line.strip() == expected[0].strip(), f"Expected {expected[0].strip()} but got {normalized_line.strip()}"

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

isort/Test4DT_tests/test_isort_parse_normalize_line_1_test_error_handling.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
___________ test_normalize_line[from .cimport some_module-expected0] ___________

raw_line = 'from .cimport some_module'
expected = ('from  cimport some_module', 'from .cimport some_module')

    @pytest.mark.parametrize("raw_line, expected", [
        ("from .cimport some_module", ('from  cimport some_module', 'from .cimport some_module')),
        ("from ..import some_module", ('from  import some_module', 'from ..import some_module')),
        ("\tfrom   import\tsome_module", ('from  import some_module', '\tfrom   import\tsome_module'))
    ])
    def test_normalize_line(raw_line, expected):
        with patch('builtins.print') as mock_print:
            normalized_line, original_line = normalize_line(raw_line)
>           assert normalized_line.strip() == expected[0].strip(), f"Expected {expected[0].strip()} but got {normalized_line.strip()}"
E           AssertionError: Expected from  cimport some_module but got from . cimport some_module
E           assert 'from . cimport some_module' == 'from  cimport some_module'
E             
E             - from  cimport some_module
E             + from . cimport some_module
E             ?      +

isort/Test4DT_tests/test_isort_parse_normalize_line_1_test_error_handling.py:15: AssertionError
___________ test_normalize_line[from ..import some_module-expected1] ___________

raw_line = 'from ..import some_module'
expected = ('from  import some_module', 'from ..import some_module')

    @pytest.mark.parametrize("raw_line, expected", [
        ("from .cimport some_module", ('from  cimport some_module', 'from .cimport some_module')),
        ("from ..import some_module", ('from  import some_module', 'from ..import some_module')),
        ("\tfrom   import\tsome_module", ('from  import some_module', '\tfrom   import\tsome_module'))
    ])
    def test_normalize_line(raw_line, expected):
        with patch('builtins.print') as mock_print:
            normalized_line, original_line = normalize_line(raw_line)
>           assert normalized_line.strip() == expected[0].strip(), f"Expected {expected[0].strip()} but got {normalized_line.strip()}"
E           AssertionError: Expected from  import some_module but got from .. import some_module
E           assert 'from .. import some_module' == 'from  import some_module'
E             
E             - from  import some_module
E             + from .. import some_module
E             ?      ++

isort/Test4DT_tests/test_isort_parse_normalize_line_1_test_error_handling.py:15: AssertionError
_________ test_normalize_line[\tfrom   import\tsome_module-expected2] __________

raw_line = '\tfrom   import\tsome_module'
expected = ('from  import some_module', '\tfrom   import\tsome_module')

    @pytest.mark.parametrize("raw_line, expected", [
        ("from .cimport some_module", ('from  cimport some_module', 'from .cimport some_module')),
        ("from ..import some_module", ('from  import some_module', 'from ..import some_module')),
        ("\tfrom   import\tsome_module", ('from  import some_module', '\tfrom   import\tsome_module'))
    ])
    def test_normalize_line(raw_line, expected):
        with patch('builtins.print') as mock_print:
            normalized_line, original_line = normalize_line(raw_line)
>           assert normalized_line.strip() == expected[0].strip(), f"Expected {expected[0].strip()} but got {normalized_line.strip()}"
E           AssertionError: Expected from  import some_module but got from   import some_module
E           assert 'from   import some_module' == 'from  import some_module'
E             
E             - from  import some_module
E             + from   import some_module
E             ?     +

isort/Test4DT_tests/test_isort_parse_normalize_line_1_test_error_handling.py:15: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_parse_normalize_line_1_test_error_handling.py::test_normalize_line[from .cimport some_module-expected0]
FAILED isort/Test4DT_tests/test_isort_parse_normalize_line_1_test_error_handling.py::test_normalize_line[from ..import some_module-expected1]
FAILED isort/Test4DT_tests/test_isort_parse_normalize_line_1_test_error_handling.py::test_normalize_line[\tfrom   import\tsome_module-expected2]
============================== 3 failed in 0.12s ===============================
"""