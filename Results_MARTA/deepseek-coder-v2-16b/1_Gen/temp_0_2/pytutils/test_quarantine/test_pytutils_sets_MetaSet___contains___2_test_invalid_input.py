
import pytest
from pytutils.sets import MetaSet

def test_invalid_input():
    meta_set = MetaSet()
    with pytest.raises(TypeError):
        assert 1 in meta_set  # This will fail because the __contains__ method expects an item, not a number

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

pytutils/Test4DT_tests/test_pytutils_sets_MetaSet___contains___2_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        meta_set = MetaSet()
        with pytest.raises(TypeError):
>           assert 1 in meta_set  # This will fail because the __contains__ method expects an item, not a number
E           assert 1 in MetaSet(_meta_func=<function MetaSet.<lambda> at 0x7f023a0237e0>, _store=set(), _meta={}, _initial=None)

pytutils/Test4DT_tests/test_pytutils_sets_MetaSet___contains___2_test_invalid_input.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_sets_MetaSet___contains___2_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.07s ===============================
"""