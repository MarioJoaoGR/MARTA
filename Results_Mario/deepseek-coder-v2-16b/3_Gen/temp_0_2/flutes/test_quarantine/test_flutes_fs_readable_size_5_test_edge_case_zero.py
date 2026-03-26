
import pytest
from flutes.fs import readable_size

def test_edge_case_zero():
    assert readable_size(0) == "0.00B"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_fs_readable_size_5_test_edge_case_zero.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_edge_case_zero ______________________________

    def test_edge_case_zero():
>       assert readable_size(0) == "0.00B"
E       AssertionError: assert '0.00' == '0.00B'
E         
E         - 0.00B
E         ?     -
E         + 0.00

flutes/Test4DT_tests/test_flutes_fs_readable_size_5_test_edge_case_zero.py:6: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_fs_readable_size_5_test_edge_case_zero.py::test_edge_case_zero
============================== 1 failed in 0.10s ===============================
"""