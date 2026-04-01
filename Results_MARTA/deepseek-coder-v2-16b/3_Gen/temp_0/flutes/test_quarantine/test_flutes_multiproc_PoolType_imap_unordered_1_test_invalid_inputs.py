
import pytest
from flutes.multiproc import PoolType
from typing import Callable, Iterable, Iterator, Any, Mapping

def square(x):
    return x ** 2

@pytest.fixture
def pool():
    return PoolType()

def test_invalid_inputs(pool):
    with pytest.raises(TypeError) as e:
        result_iterator = pool.imap_unordered(None, range(5), chunksize=1)
    assert str(e.value) == "Expected a callable function"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_multiproc_PoolType_imap_unordered_1_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

pool = <flutes.multiproc.PoolType state=RUN pool_size=128>

    def test_invalid_inputs(pool):
>       with pytest.raises(TypeError) as e:
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_multiproc_PoolType_imap_unordered_1_test_invalid_inputs.py:14: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_PoolType_imap_unordered_1_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.20s ===============================

Exception ignored in: <function Pool.__del__ at 0x7f108c979c60>
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