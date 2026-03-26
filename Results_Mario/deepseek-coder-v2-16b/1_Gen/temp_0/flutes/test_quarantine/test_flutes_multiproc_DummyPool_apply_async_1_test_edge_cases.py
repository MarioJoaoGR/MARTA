
import multiprocessing as mp
from typing import Callable, Iterable, Dict, Any, Optional

class DummyPool(mp.pool.Pool):
    """A wrapper over ``multiprocessing.Pool`` that uses single-threaded execution when :attr:`processes` is zero."""
    
    def __init__(self, processes: Optional[int] = None, initializer: Optional[Callable[..., None]] = None,
                 initargs: Iterable[Any] = (), maxtasksperchild: Optional[int] = None):
        super().__init__(processes=processes, initializer=initializer, initargs=initargs, maxtasksperchild=maxtasksperchild)
    
    def apply_async(self, fn: Callable[..., 'mp.pool.ApplyResult'], args: Iterable[Any] = (), kwds: Dict[str, Any] = {}) -> 'mp.pool.ApplyResult':
        return super().apply_async(fn, args, kwds)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_ ERROR collecting Test4DT_tests/test_flutes_multiproc_DummyPool_apply_async_1_test_edge_cases.py _
flutes/Test4DT_tests/test_flutes_multiproc_DummyPool_apply_async_1_test_edge_cases.py:5: in <module>
    class DummyPool(mp.pool.Pool):
E   AttributeError: module 'multiprocessing' has no attribute 'pool'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR flutes/Test4DT_tests/test_flutes_multiproc_DummyPool_apply_async_1_test_edge_cases.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.13s ===============================
"""