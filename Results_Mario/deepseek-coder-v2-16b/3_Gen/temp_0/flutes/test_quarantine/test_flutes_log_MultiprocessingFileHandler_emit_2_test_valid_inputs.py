
import pytest
from unittest.mock import MagicMock, patch
import logging
import multiprocessing
from pathlib import Path
from flutes.log import MultiprocessingFileHandler

def worker(queue):
    logger = logging.getLogger('test_logger')
    handler = MultiprocessingFileHandler(Path("logs/app.log"))
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    logger.debug('Test message from process')
    queue.put(handler)

@pytest.fixture(scope="module")
def log_queue():
    queue = multiprocessing.Queue()
    return queue

@pytest.fixture(scope="module")
def setup_logging():
    # Set up logging configuration if needed
    pass

@pytest.mark.skipif(not hasattr(multiprocessing, 'get_context'), reason="requires the multiprocessing module from python stdlib")
def test_valid_inputs(log_queue):
    ctx = multiprocessing.get_context('spawn')
    p = ctx.Process(target=worker, args=(log_queue,))
    p.start()
    p.join()
    
    handler = log_queue.get()
    assert isinstance(handler, MultiprocessingFileHandler)
    
    # Check if the logger wrote to the file
    with open("logs/app.log", "r") as f:
        logs = f.readlines()
    assert len(logs) == 1
    assert "Test message from process" in logs[0]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_emit_2_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

log_queue = <multiprocessing.queues.Queue object at 0x7fe931f46dd0>

    @pytest.mark.skipif(not hasattr(multiprocessing, 'get_context'), reason="requires the multiprocessing module from python stdlib")
    def test_valid_inputs(log_queue):
        ctx = multiprocessing.get_context('spawn')
        p = ctx.Process(target=worker, args=(log_queue,))
>       p.start()

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_emit_2_test_valid_inputs.py:31: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/usr/local/lib/python3.11/multiprocessing/process.py:121: in start
    self._popen = self._Popen(self)
/usr/local/lib/python3.11/multiprocessing/context.py:288: in _Popen
    return Popen(process_obj)
/usr/local/lib/python3.11/multiprocessing/popen_spawn_posix.py:32: in __init__
    super().__init__(process_obj)
/usr/local/lib/python3.11/multiprocessing/popen_fork.py:19: in __init__
    self._launch(process_obj)
/usr/local/lib/python3.11/multiprocessing/popen_spawn_posix.py:47: in _launch
    reduction.dump(process_obj, fp)
/usr/local/lib/python3.11/multiprocessing/reduction.py:60: in dump
    ForkingPickler(file, protocol).dump(obj)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <Lock(owner=None)>

    def __getstate__(self):
        context.assert_spawning(self)
        sl = self._semlock
        if sys.platform == 'win32':
            h = context.get_spawning_popen().duplicate_for_child(sl.handle)
        else:
            if self._is_fork_ctx:
>               raise RuntimeError('A SemLock created in a fork context is being '
                                   'shared with a process in a spawn context. This is '
                                   'not supported. Please use the same context to create '
                                   'multiprocessing objects and Process.')
E               RuntimeError: A SemLock created in a fork context is being shared with a process in a spawn context. This is not supported. Please use the same context to create multiprocessing objects and Process.

/usr/local/lib/python3.11/multiprocessing/synchronize.py:107: RuntimeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_emit_2_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.14s ===============================
"""