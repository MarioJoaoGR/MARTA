
import pytest
from flutes.multiproc import StatefulPoolType, PoolState  # Assuming these imports are correct

def test_get_states():
    stateful_pool = StatefulPoolType()  # Assuming this is properly initialized and configured
    
    with pytest.raises(NotImplementedError):
        stateful_pool.get_states()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_multiproc_StatefulPoolType_get_states_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_get_states ________________________________

    def test_get_states():
        stateful_pool = StatefulPoolType()  # Assuming this is properly initialized and configured
    
>       with pytest.raises(NotImplementedError):
E       Failed: DID NOT RAISE <class 'NotImplementedError'>

flutes/Test4DT_tests/test_flutes_multiproc_StatefulPoolType_get_states_0_test_valid_input.py:8: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_StatefulPoolType_get_states_0_test_valid_input.py::test_get_states
============================== 1 failed in 0.19s ===============================

"""