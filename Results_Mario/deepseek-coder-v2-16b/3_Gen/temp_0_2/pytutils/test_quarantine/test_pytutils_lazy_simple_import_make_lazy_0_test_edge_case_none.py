
from pytutils.lazy.simple_import import make_lazy
import pytest
import sys
from types import ModuleType

def test_edge_case_none():
    with pytest.raises(TypeError):
        make_lazy(None)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pytutils/Test4DT_tests/test_pytutils_lazy_simple_import_make_lazy_0_test_edge_case_none.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_edge_case_none ______________________________

>   ???
E   Failed: DID NOT RAISE <class 'TypeError'>

pytutils/Test4DT_tests/test_pytutils_lazy_simple_import_make_lazy_0_test_edge_case_none.py:8: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_lazy_simple_import_make_lazy_0_test_edge_case_none.py::test_edge_case_none
============================== 1 failed in 0.07s ===============================
"""