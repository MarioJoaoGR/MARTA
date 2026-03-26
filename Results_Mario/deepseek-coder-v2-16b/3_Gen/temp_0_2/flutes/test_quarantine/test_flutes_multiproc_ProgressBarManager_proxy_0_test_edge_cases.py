
import pytest
import multiprocessing as mp
import time
import random
from typing import List, Iterable, Optional, Dict, Any, Iterator, Union, Literal, Callable
from flutes.multiproc import ProgressBarManager

def test_edge_cases():
    manager = ProgressBarManager(verbose=False)
    
    # Test with empty list
    def run_empty(xs: List[int], *, bar):
        result = 0
        if xs:
            bar.new(total=len(xs), desc="Worker {flutes.get_worker_id()}")
            for idx, x in enumerate(xs):
                result += x
                time.sleep(random.uniform(0.01, 0.2))
                bar.update(1, postfix={"sum": result})
        return result
    
    with mp.Pool(1) as pool:
        for idx, _ in enumerate(pool.imap_unordered(run_empty, [[]])):
            pass

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

flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager_proxy_0_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        manager = ProgressBarManager(verbose=False)
    
        # Test with empty list
        def run_empty(xs: List[int], *, bar):
            result = 0
            if xs:
                bar.new(total=len(xs), desc="Worker {flutes.get_worker_id()}")
                for idx, x in enumerate(xs):
                    result += x
                    time.sleep(random.uniform(0.01, 0.2))
                    bar.update(1, postfix={"sum": result})
            return result
    
        with mp.Pool(1) as pool:
>           for idx, _ in enumerate(pool.imap_unordered(run_empty, [[]])):

flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager_proxy_0_test_edge_cases.py:24: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/usr/local/lib/python3.11/multiprocessing/pool.py:873: in next
    raise value
/usr/local/lib/python3.11/multiprocessing/pool.py:540: in _handle_tasks
    put(task)
/usr/local/lib/python3.11/multiprocessing/connection.py:206: in send
    self._send_bytes(_ForkingPickler.dumps(obj))
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

cls = <class 'multiprocessing.reduction.ForkingPickler'>
obj = (0, 0, <function test_edge_cases.<locals>.run_empty at 0x7f9feb44b1a0>, ([],), {})
protocol = None

    @classmethod
    def dumps(cls, obj, protocol=None):
        buf = io.BytesIO()
>       cls(buf, protocol).dump(obj)
E       AttributeError: Can't pickle local object 'test_edge_cases.<locals>.run_empty'

/usr/local/lib/python3.11/multiprocessing/reduction.py:51: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager_proxy_0_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.13s ===============================
"""