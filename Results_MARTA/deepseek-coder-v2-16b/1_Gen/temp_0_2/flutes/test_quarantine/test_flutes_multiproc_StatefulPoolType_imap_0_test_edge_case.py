
import pytest
from multiprocessing import Pool
from flutes.multiproc import StatefulPoolType

@pytest.fixture
def pool():
    return StatefulPoolType()

def test_edge_case(pool):
    # Define a mock function to be used as the task
    def mock_fn(state, x):
        return x * 2

    # Create an iterable for testing
    iterable = [1, 2, 3, 4]

    # Call the imap method with the mock function and iterable
    results = pool.imap(mock_fn, iterable, chunksize=2)

    # Collect the results into a list
    result_list = list(results)

    # Assert that the results are as expected
    assert result_list == [2, 4, 6, 8]

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

flutes/Test4DT_tests/test_flutes_multiproc_StatefulPoolType_imap_0_test_edge_case.py F [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

pool = <flutes.multiproc.StatefulPoolType state=RUN pool_size=128>

    def test_edge_case(pool):
        # Define a mock function to be used as the task
        def mock_fn(state, x):
            return x * 2
    
        # Create an iterable for testing
        iterable = [1, 2, 3, 4]
    
        # Call the imap method with the mock function and iterable
        results = pool.imap(mock_fn, iterable, chunksize=2)
    
        # Collect the results into a list
>       result_list = list(results)
E       TypeError: 'NoneType' object is not iterable

flutes/Test4DT_tests/test_flutes_multiproc_StatefulPoolType_imap_0_test_edge_case.py:22: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_StatefulPoolType_imap_0_test_edge_case.py::test_edge_case
============================== 1 failed in 0.19s ===============================
"""