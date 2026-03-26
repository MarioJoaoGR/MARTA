
import pytest
from pymonet.monad_try import Try

def test_edge_cases():
    try_instance = Try(value='some_value', is_success=False)
    
    def fail_callback(val):
        assert val is None
    
    try_instance.on_fail(fail_callback)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pyMonet
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pyMonet/Test4DT_tests/test_pymonet_monad_try_Try_on_fail_1_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        try_instance = Try(value='some_value', is_success=False)
    
        def fail_callback(val):
            assert val is None
    
>       try_instance.on_fail(fail_callback)

pyMonet/Test4DT_tests/test_pymonet_monad_try_Try_on_fail_1_test_edge_cases.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pyMonet/pymonet/monad_try.py:89: in on_fail
    fail_callback(self.value)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

val = 'some_value'

    def fail_callback(val):
>       assert val is None
E       AssertionError: assert 'some_value' is None

pyMonet/Test4DT_tests/test_pymonet_monad_try_Try_on_fail_1_test_edge_cases.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_monad_try_Try_on_fail_1_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.06s ===============================
"""