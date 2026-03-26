
# Module: pytutils.timers
import pytest
from pytutils.timers import Timer
import time
import logging

# Configure a custom logger for testing purposes
_LOG = logging.getLogger('my_logger')
_LOG.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
_LOG.addHandler(handler)

@pytest.fixture
def timer():
    return Timer('test_operation', verbose=True)

def test_timer_basic(capsys):  # Added capsys parameter
    with Timer('test_operation', verbose=True) as t:
        time.sleep(1)  # Elapsed time should be more than 0 seconds but less than 2 seconds
    captured = capsys.readouterr()  # Corrected method call to read outerr
    assert "Elapsed time for 'test_operation': " in captured.out

def test_timer_default_settings():
    with Timer('default_operation') as t:
        time.sleep(1)  # Elapsed time should be more than 0 seconds but less than 2 seconds
    assert hasattr(t, 'secs') and hasattr(t, 'msecs')

def test_timer_multiple_operations():
    with Timer('operation1', verbose=True) as t1:
        time.sleep(3)
    with Timer('operation2') as t2:
        time.sleep(2)
    captured = capsys.readouterr()  # Corrected method call to read outerr
    assert "Elapsed time for 'operation1': " in captured.out
    assert "Elapsed time for 'operation2': " not in captured.out  # operation2 is not verbose

def test_timer_custom_logging(capsys):  # Added capsys parameter
    with Timer('custom_log', verbose=True) as t:
        time.sleep(4)
    captured = capsys.readouterr()  # Corrected method call to read outerr
    assert "Elapsed time for 'custom_log': " in captured.out

def test_timer_context_manager(timer):
    with timer:
        time.sleep(1)  # Elapsed time should be more than 0 seconds but less than 2 seconds
    captured = capsys.readouterr()  # Corrected method call to read outerr
    assert "Elapsed time for 'test_operation': " in captured.out

def test_timer_no_verbose():
    with Timer('no_verbose_operation', verbose=False) as t:
        time.sleep(1)  # Elapsed time should be more than 0 seconds but less than 2 seconds
    assert hasattr(t, 'secs') and hasattr(t, 'msecs')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_timers_Timer___exit___0
pytutils/Test4DT_tests/test_pytutils_timers_Timer___exit___0.py:36:15: E0602: Undefined variable 'capsys' (undefined-variable)
pytutils/Test4DT_tests/test_pytutils_timers_Timer___exit___0.py:49:15: E0602: Undefined variable 'capsys' (undefined-variable)


"""