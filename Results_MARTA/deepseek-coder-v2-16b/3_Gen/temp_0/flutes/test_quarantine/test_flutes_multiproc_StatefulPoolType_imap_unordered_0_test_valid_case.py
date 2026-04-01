
import pytest
from flutes.multiproc import StatefulPoolType, safe_pool
from multiprocessing import Pool, Queue
from typing import List, Any, Callable, Mapping, Iterator

class State:
    def __init__(self):
        self.queue = Queue()
    
    def process_item(self, item: int) -> int:
        # Example function to process each item in the iterable
        return item * 2

@pytest.fixture
def stateful_pool():
    pool = safe_pool(State)
    return pool

def test_valid_case(stateful_pool):
    results = list(stateful_pool.imap_unordered(State().process_item, range(10), chunksize=2))
    assert len(results) == 10
    for result in results:
        assert result == (result // 2) * 2

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_multiproc_StatefulPoolType_imap_unordered_0_test_valid_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

stateful_pool = <contextlib._GeneratorContextManager object at 0x7f97762d6dd0>

    def test_valid_case(stateful_pool):
>       results = list(stateful_pool.imap_unordered(State().process_item, range(10), chunksize=2))
E       AttributeError: '_GeneratorContextManager' object has no attribute 'imap_unordered'

flutes/Test4DT_tests/test_flutes_multiproc_StatefulPoolType_imap_unordered_0_test_valid_case.py:21: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_StatefulPoolType_imap_unordered_0_test_valid_case.py::test_valid_case
============================== 1 failed in 0.10s ===============================
"""