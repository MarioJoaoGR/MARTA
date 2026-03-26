
import pytest
from flutes.multiproc import safe_pool
from multiprocessing import Pool, Queue

class State(object):
    def __init__(self):
        self.queue = Queue()

    def process_item(self, state, item):
        result = item * 2
        state.queue.put(result)
        return result

@pytest.fixture
def pool():
    return safe_pool(State)

def test_imap(pool):
    items = [1, 2, 3, 4]
    results = pool.imap(State().process_item, items, chunksize=2, args=(State(),))
    assert list(results) == [2, 4, 6, 8]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_multiproc_StatefulPoolType_imap_0_test_edge_case.py F [100%]

=================================== FAILURES ===================================
__________________________________ test_imap ___________________________________

pool = <contextlib._GeneratorContextManager object at 0x7f90dbf81410>

    def test_imap(pool):
        items = [1, 2, 3, 4]
>       results = pool.imap(State().process_item, items, chunksize=2, args=(State(),))
E       AttributeError: '_GeneratorContextManager' object has no attribute 'imap'

flutes/Test4DT_tests/test_flutes_multiproc_StatefulPoolType_imap_0_test_edge_case.py:21: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_StatefulPoolType_imap_0_test_edge_case.py::test_imap
============================== 1 failed in 0.10s ===============================
"""