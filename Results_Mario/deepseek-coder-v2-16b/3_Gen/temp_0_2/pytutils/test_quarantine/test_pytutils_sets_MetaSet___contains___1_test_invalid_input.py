
import pytest
from pytutils.sets import MetaSet

@pytest.fixture(name="meta_set")
def create_meta_set():
    return MetaSet()

def test_invalid_input(meta_set):
    with pytest.raises(TypeError):
        meta_set.__contains__("invalid input")

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

pytutils/Test4DT_tests/test_pytutils_sets_MetaSet___contains___1_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

meta_set = MetaSet(_meta_func=<function MetaSet.<lambda> at 0x7f2bc7d93ba0>, _store=set(), _meta={}, _initial=None)

    def test_invalid_input(meta_set):
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

pytutils/Test4DT_tests/test_pytutils_sets_MetaSet___contains___1_test_invalid_input.py:10: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_sets_MetaSet___contains___1_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.07s ===============================
"""