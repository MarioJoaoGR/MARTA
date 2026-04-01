
import pytest
from flutes.multiproc import PoolWrapper

def test_valid_inputs():
    pool = PoolWrapper()
    
    # Test imap method with a lambda function
    result_list = list(pool.imap([1, 2, 3], lambda x: x * x))
    
    assert len(result_list) == 3
    for i, result in enumerate(result_list):
        assert result == (i + 1) ** 2

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

flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper__define_method_0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        pool = PoolWrapper()
    
        # Test imap method with a lambda function
>       result_list = list(pool.imap([1, 2, 3], lambda x: x * x))

flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper__define_method_0_test_valid_inputs.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <multiprocessing.pool.IMapIterator object at 0x7fea168fc750>
timeout = None

    def next(self, timeout=None):
        with self._cond:
            try:
                item = self._items.popleft()
            except IndexError:
                if self._index == self._length:
                    self._pool = None
                    raise StopIteration from None
                self._cond.wait(timeout)
                try:
                    item = self._items.popleft()
                except IndexError:
                    if self._index == self._length:
                        self._pool = None
                        raise StopIteration from None
                    raise TimeoutError from None
    
        success, value = item
        if success:
            return value
>       raise value
E       TypeError: 'function' object is not iterable

/usr/local/lib/python3.11/multiprocessing/pool.py:873: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper__define_method_0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.20s ===============================
"""