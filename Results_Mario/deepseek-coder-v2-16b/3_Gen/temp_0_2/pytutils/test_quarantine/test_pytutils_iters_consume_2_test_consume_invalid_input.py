
import pytest
from pytutils.iters import consume

def test_consume_invalid_input():
    lst = [1, 2, 3, 4]
    it = iter(lst)
    
    # Test with invalid `n` type (non-integer)
    with pytest.raises(TypeError):
        consume(it, "invalid")

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

pytutils/Test4DT_tests/test_pytutils_iters_consume_2_test_consume_invalid_input.py F [100%]

=================================== FAILURES ===================================
__________________________ test_consume_invalid_input __________________________

    def test_consume_invalid_input():
        lst = [1, 2, 3, 4]
        it = iter(lst)
    
        # Test with invalid `n` type (non-integer)
        with pytest.raises(TypeError):
>           consume(it, "invalid")

pytutils/Test4DT_tests/test_pytutils_iters_consume_2_test_consume_invalid_input.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

iterator = <list_iterator object at 0x7f3d2da32380>, n = 'invalid'

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
>           next(itertools.islice(iterator, n, n), None)
E           ValueError: Stop argument for islice() must be None or an integer: 0 <= x <= sys.maxsize.

pytutils/pytutils/iters.py:42: ValueError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_iters_consume_2_test_consume_invalid_input.py::test_consume_invalid_input
============================== 1 failed in 0.07s ===============================
"""