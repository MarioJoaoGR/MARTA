
import pytest
from flutes.multiproc import PoolType
from typing import Callable, Iterator, Iterable, Any, Mapping

def example_fn(x):
    yield x * 2
    yield x * 3

class TestPoolTypeGatherInvalidInput:
    
    @pytest.mark.parametrize("chunksize", [0, -1])
    def test_invalid_input(self, chunksize):
        pool = PoolType()
        with pytest.raises(ValueError):
            list(pool.gather(example_fn, [1, 2, 3], chunksize=chunksize))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

flutes/Test4DT_tests/test_flutes_multiproc_PoolType_gather_1_test_invalid_input.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_____________ TestPoolTypeGatherInvalidInput.test_invalid_input[0] _____________

self = <Test4DT_tests.test_flutes_multiproc_PoolType_gather_1_test_invalid_input.TestPoolTypeGatherInvalidInput object at 0x7f77d12a4ad0>
chunksize = 0

    @pytest.mark.parametrize("chunksize", [0, -1])
    def test_invalid_input(self, chunksize):
        pool = PoolType()
        with pytest.raises(ValueError):
>           list(pool.gather(example_fn, [1, 2, 3], chunksize=chunksize))
E           TypeError: 'NoneType' object is not iterable

flutes/Test4DT_tests/test_flutes_multiproc_PoolType_gather_1_test_invalid_input.py:16: TypeError
____________ TestPoolTypeGatherInvalidInput.test_invalid_input[-1] _____________

self = <Test4DT_tests.test_flutes_multiproc_PoolType_gather_1_test_invalid_input.TestPoolTypeGatherInvalidInput object at 0x7f77d05967d0>
chunksize = -1

    @pytest.mark.parametrize("chunksize", [0, -1])
    def test_invalid_input(self, chunksize):
        pool = PoolType()
        with pytest.raises(ValueError):
>           list(pool.gather(example_fn, [1, 2, 3], chunksize=chunksize))
E           TypeError: 'NoneType' object is not iterable

flutes/Test4DT_tests/test_flutes_multiproc_PoolType_gather_1_test_invalid_input.py:16: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_PoolType_gather_1_test_invalid_input.py::TestPoolTypeGatherInvalidInput::test_invalid_input[0]
FAILED flutes/Test4DT_tests/test_flutes_multiproc_PoolType_gather_1_test_invalid_input.py::TestPoolTypeGatherInvalidInput::test_invalid_input[-1]
============================== 2 failed in 0.39s ===============================

Exception ignored in: <function Pool.__del__ at 0x7f77d033a020>
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 271, in __del__
    self._change_notifier.put(None)
  File "/usr/local/lib/python3.11/multiprocessing/queues.py", line 377, in put
    self._writer.send_bytes(obj)
  File "/usr/local/lib/python3.11/multiprocessing/connection.py", line 200, in send_bytes
    self._send_bytes(m[offset:offset + size])
  File "/usr/local/lib/python3.11/multiprocessing/connection.py", line 427, in _send_bytes
    self._send(header + buf)
  File "/usr/local/lib/python3.11/multiprocessing/connection.py", line 384, in _send
    n = write(self._handle, buf)
        ^^^^^^^^^^^^^^^^^^^^^^^^
OSError: [Errno 9] Bad file descriptor
"""