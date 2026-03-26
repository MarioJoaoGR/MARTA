
import pytest
from flutes.multiproc import PoolWrapper

def square(x):
    return x * x

@pytest.fixture
def pool():
    return PoolWrapper()

def test_gather(pool):
    results = list(pool.gather(square, range(10), chunksize=2))
    assert len(results) == 10

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

flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper_gather_0_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_________________________________ test_gather __________________________________

pool = <flutes.multiproc.PoolWrapper state=RUN pool_size=128>

    def test_gather(pool):
        results = list(pool.gather(square, range(10), chunksize=2))
>       assert len(results) == 10
E       assert 0 == 10
E        +  where 0 = len([])

flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper_gather_0_test_edge_cases.py:14: AssertionError
----------------------------- Captured stdout call -----------------------------
[2026-03-24 16:21:26] (Worker  3) Traceback (most recent call last):
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 228, in _gather_fn
    for x in fn(*args, **kwargs):  # type: ignore[call-arg]
TypeError: 'int' object is not iterable
[2026-03-24 16:21:26] (Worker  4) Traceback (most recent call last):
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 228, in _gather_fn
    for x in fn(*args, **kwargs):  # type: ignore[call-arg]
TypeError: 'int' object is not iterable


[2026-03-24 16:21:26] (Worker  2) Traceback (most recent call last):
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 228, in _gather_fn
    for x in fn(*args, **kwargs):  # type: ignore[call-arg]
TypeError: 'int' object is not iterable

[2026-03-24 16:21:26] (Worker  5) Traceback (most recent call last):
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 228, in _gather_fn
    for x in fn(*args, **kwargs):  # type: ignore[call-arg]
TypeError: 'int' object is not iterable

[2026-03-24 16:21:26] (Worker  4) <TypeError> 'int' object is not iterable[2026-03-24 16:21:26] (Worker  3) <TypeError> 'int' object is not iterable

[2026-03-24 16:21:26] (Worker  1) Traceback (most recent call last):
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 228, in _gather_fn
    for x in fn(*args, **kwargs):  # type: ignore[call-arg]
TypeError: 'int' object is not iterable

[2026-03-24 16:21:26] (Worker  2) <TypeError> 'int' object is not iterable
[2026-03-24 16:21:26] (Worker  5) <TypeError> 'int' object is not iterable
[2026-03-24 16:21:26] (Worker  1) <TypeError> 'int' object is not iterable
[2026-03-24 16:21:26] (Worker  3) Traceback (most recent call last):
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 228, in _gather_fn
    for x in fn(*args, **kwargs):  # type: ignore[call-arg]
TypeError: 'int' object is not iterable

[2026-03-24 16:21:26] (Worker  3) <TypeError> 'int' object is not iterable
[2026-03-24 16:21:26] (Worker  4) Traceback (most recent call last):
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 228, in _gather_fn
    for x in fn(*args, **kwargs):  # type: ignore[call-arg]
TypeError: 'int' object is not iterable

[2026-03-24 16:21:26] (Worker  2) Traceback (most recent call last):
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 228, in _gather_fn
    for x in fn(*args, **kwargs):  # type: ignore[call-arg]
TypeError: 'int' object is not iterable

[2026-03-24 16:21:26] (Worker  4) <TypeError> 'int' object is not iterable
[2026-03-24 16:21:26] (Worker  2) <TypeError> 'int' object is not iterable
[2026-03-24 16:21:26] (Worker  5) Traceback (most recent call last):
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 228, in _gather_fn
    for x in fn(*args, **kwargs):  # type: ignore[call-arg]
TypeError: 'int' object is not iterable

[2026-03-24 16:21:26] (Worker  5) <TypeError> 'int' object is not iterable
[2026-03-24 16:21:26] (Worker  1) Traceback (most recent call last):
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py", line 228, in _gather_fn
    for x in fn(*args, **kwargs):  # type: ignore[call-arg]
TypeError: 'int' object is not iterable

[2026-03-24 16:21:26] (Worker  1) <TypeError> 'int' object is not iterable
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper_gather_0_test_edge_cases.py::test_gather
============================== 1 failed in 0.31s ===============================
"""