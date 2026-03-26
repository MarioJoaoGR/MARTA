
import pytest
from multiprocessing import Pool
from flutes.multiproc import StatefulPoolType, PoolState

@pytest.fixture
def stateful_pool():
    return StatefulPoolType()

def test_get_states(stateful_pool):
    # Assuming the pool is properly initialized and configured
    states = stateful_pool.get_states()
    assert isinstance(states, list)
    for state in states:
        assert isinstance(state, PoolState)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_multiproc_StatefulPoolType_get_states_0_test_valid_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_get_states ________________________________

stateful_pool = <flutes.multiproc.StatefulPoolType state=RUN pool_size=128>

    def test_get_states(stateful_pool):
        # Assuming the pool is properly initialized and configured
        states = stateful_pool.get_states()
>       assert isinstance(states, list)
E       assert False
E        +  where False = isinstance(None, list)

flutes/Test4DT_tests/test_flutes_multiproc_StatefulPoolType_get_states_0_test_valid_case.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_StatefulPoolType_get_states_0_test_valid_case.py::test_get_states
============================== 1 failed in 0.20s ===============================
"""