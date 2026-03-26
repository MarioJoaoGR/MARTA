
import pytest
from pytutils.iters import consume
import itertools
import collections

def test_edge_cases():
    lst = []
    it = iter(lst)
    
    with pytest.raises(StopIteration):
        consume(it)
        next(it)  # The iterator should be exhausted after consuming all elements.
    
    lst = [1, 2, 3, 4]
    it = iter(lst)
    
    consume(it, 2)
    assert next(it) == 3
    
    with pytest.raises(StopIteration):
        consume(it)
        next(it)  # The iterator should be exhausted after consuming all elements.
    
    lst = None
    it = iter(lst if lst is not None else [])
    
    with pytest.raises(TypeError):
        consume(it)

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

pytutils/Test4DT_tests/test_pytutils_iters_consume_5_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        lst = []
        it = iter(lst)
    
        with pytest.raises(StopIteration):
            consume(it)
            next(it)  # The iterator should be exhausted after consuming all elements.
    
        lst = [1, 2, 3, 4]
        it = iter(lst)
    
        consume(it, 2)
        assert next(it) == 3
    
        with pytest.raises(StopIteration):
            consume(it)
            next(it)  # The iterator should be exhausted after consuming all elements.
    
        lst = None
        it = iter(lst if lst is not None else [])
    
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

pytutils/Test4DT_tests/test_pytutils_iters_consume_5_test_edge_cases.py:28: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_iters_consume_5_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.07s ===============================
"""