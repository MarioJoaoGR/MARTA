
import pytest
from multiprocessing import Pool, get_context
from flutes.multiproc import PoolWrapper

def test_invalid_input():
    pool = PoolWrapper()
    
    # Test with None as the function to apply
    with pytest.raises(TypeError):
        list(pool.gather(None, [1, 2, 3]))
    
    # Test with a non-callable object as the function to apply
    with pytest.raises(TypeError):
        list(pool.gather("not_a_function", [1, 2, 3]))
    
    # Test with None as the iterable
    with pytest.raises(TypeError):
        list(pool.gather(lambda x: [x * 2], None))
    
    # Test with a non-iterable object as the iterable
    with pytest.raises(TypeError):
        list(pool.gather(lambda x: [x * 2], 12345))

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

flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper_gather_1_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        pool = PoolWrapper()
    
        # Test with None as the function to apply
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper_gather_1_test_invalid_input.py:10: Failed
----------------------------- Captured stdout call -----------------------------
[2026-03-24 19:00:46] (Worker  2) Traceback (most recent call last):
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 228, in _gather_fn
    for x in fn(*args, **kwargs):  # type: ignore[call-arg]
             ^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable

[2026-03-24 19:00:46] (Worker  3) Traceback (most recent call last):
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 228, in _gather_fn
    for x in fn(*args, **kwargs):  # type: ignore[call-arg]
             ^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable

[2026-03-24 19:00:46] (Worker  2) <TypeError> 'NoneType' object is not callable
[2026-03-24 19:00:46] (Worker  3) <TypeError> 'NoneType' object is not callable
[2026-03-24 19:00:46] (Worker  1) Traceback (most recent call last):
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 228, in _gather_fn
    for x in fn(*args, **kwargs):  # type: ignore[call-arg]
             ^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not callable

[2026-03-24 19:00:46] (Worker  1) <TypeError> 'NoneType' object is not callable
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper_gather_1_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.32s ===============================
"""