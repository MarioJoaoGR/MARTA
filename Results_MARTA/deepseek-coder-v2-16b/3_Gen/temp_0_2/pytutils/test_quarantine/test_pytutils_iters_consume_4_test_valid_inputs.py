
import pytest
from itertools import islice, count
import collections

def consume(iterator, n=None):
    """
    Efficiently advance an iterator n-steps ahead. If n is none, consume entirely.
    Consumes at C level (and therefore speed) in cpython.
    """
    if n is None:
        # feed the entire iterator into a zero-length deque
        collections.deque(iterator, maxlen=0)
    else:
        # advance to the empty slice starting at position n
        next(islice(iterator, n, n), None)

def test_valid_inputs():
    lst = [1, 2, 3, 4]
    it = iter(lst)
    
    consume(it)
    assert next(it) == 1
    
    consume(it, 2)
    assert next(it) == 3
    
    # Test consuming the entire iterator
    lst_full = [5, 6, 7, 8]
    it_full = iter(lst_full)
    consume(it_full)
    with pytest.raises(StopIteration):
        next(it_full)

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

pytutils/Test4DT_tests/test_pytutils_iters_consume_4_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        lst = [1, 2, 3, 4]
        it = iter(lst)
    
        consume(it)
>       assert next(it) == 1
E       StopIteration

pytutils/Test4DT_tests/test_pytutils_iters_consume_4_test_valid_inputs.py:23: StopIteration
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_iters_consume_4_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.07s ===============================
"""