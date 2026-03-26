
import pytest
from flutes.iterator import scanl
import operator

# Test cases for scanl function
def test_scanl_basic():
    result = list(scanl(operator.add, [1, 2, 3, 4]))
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

flutes/Test4DT_tests/test_flutes_iterator_scanl_0.py F.                  [100%]

=================================== FAILURES ===================================
_______________________________ test_scanl_basic _______________________________

    def test_scanl_basic():
        result = list(scanl(operator.add, [1, 2, 3, 4]))
>       assert result == [0, 1, 3, 6]
E       assert [1, 3, 6, 10] == [0, 1, 3, 6]
E         
E         At index 0 diff: 1 != 0
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_iterator_scanl_0.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_scanl_0.py::test_scanl_basic
========================= 1 failed, 1 passed in 0.10s ==========================
"""