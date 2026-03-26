
import pytest
from flutes.multiproc import safe_pool
from multiprocessing import Pool, Queue

class State:
    def __init__(self):
        self.queue = Queue()
    
    def process_item(self, item: int) -> int:
        return item * 2

@pytest.fixture
def stateful_pool():
    pool = safe_pool(State)
    yield pool
    # Clean up if necessary

def test_valid_case(stateful_pool):
    results = list(stateful_pool.imap_unordered(State().process_item, range(10), chunksize=2))
    assert results == [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

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

flutes/Test4DT_tests/test_flutes_multiproc_StatefulPoolType_imap_unordered_0_test_valid_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

stateful_pool = <contextlib._GeneratorContextManager object at 0x7f84716fe190>

    def test_valid_case(stateful_pool):
>       results = list(stateful_pool.imap_unordered(State().process_item, range(10), chunksize=2))
E       AttributeError: '_GeneratorContextManager' object has no attribute 'imap_unordered'

flutes/Test4DT_tests/test_flutes_multiproc_StatefulPoolType_imap_unordered_0_test_valid_case.py:20: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_StatefulPoolType_imap_unordered_0_test_valid_case.py::test_valid_case
============================== 1 failed in 0.08s ===============================
"""