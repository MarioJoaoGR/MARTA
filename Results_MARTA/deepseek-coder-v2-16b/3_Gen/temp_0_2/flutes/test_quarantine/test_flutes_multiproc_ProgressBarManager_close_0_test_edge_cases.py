
import pytest
from flutes.multiproc import ProgressBarManager

@pytest.fixture(scope="module")
def progress_bar_manager():
    manager = ProgressBarManager(verbose=True)
    yield manager
    manager.close()

def test_progress_bar_creation(progress_bar_manager):
    assert isinstance(progress_bar_manager._proxy, ProgressBarManager.Proxy)

def test_progress_bar_update(progress_bar_manager):
    xs = list(range(100))
    progress_bar_manager._proxy.new(iterable=xs, total=len(xs))
    assert len(progress_bar_manager.progress_bars) == 1
    progress_bar_manager._proxy.update(n=1)
    assert progress_bar_manager.progress_bars[None].n == 1

def test_progress_bar_write(progress_bar_manager):
    message = "Test message"
    progress_bar_manager._proxy.write(message)
    # Assuming the write method stores messages in a way that can be checked later
    assert len(progress_bar_manager.messages) == 1
    assert progress_bar_manager.messages[0] == message

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager_close_0_test_edge_cases.py . [ 33%]
FTest message
F                                                                       [100%]

=================================== FAILURES ===================================
___________________________ test_progress_bar_update ___________________________

progress_bar_manager = <flutes.multiproc.ProgressBarManager object at 0x7f92e0b66210>

    def test_progress_bar_update(progress_bar_manager):
        xs = list(range(100))
        progress_bar_manager._proxy.new(iterable=xs, total=len(xs))
>       assert len(progress_bar_manager.progress_bars) == 1
E       assert 0 == 1
E        +  where 0 = len({})
E        +    where {} = <flutes.multiproc.ProgressBarManager object at 0x7f92e0b66210>.progress_bars

flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager_close_0_test_edge_cases.py:17: AssertionError
___________________________ test_progress_bar_write ____________________________

progress_bar_manager = <flutes.multiproc.ProgressBarManager object at 0x7f92e0b66210>

    def test_progress_bar_write(progress_bar_manager):
        message = "Test message"
        progress_bar_manager._proxy.write(message)
        # Assuming the write method stores messages in a way that can be checked later
>       assert len(progress_bar_manager.messages) == 1
E       AttributeError: 'ProgressBarManager' object has no attribute 'messages'

flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager_close_0_test_edge_cases.py:25: AttributeError
--------------------------- Captured stderr teardown ---------------------------

                                       
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager_close_0_test_edge_cases.py::test_progress_bar_update
FAILED flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager_close_0_test_edge_cases.py::test_progress_bar_write
========================= 2 failed, 1 passed in 0.14s ==========================


  0%|          | 0/100 [00:00<?, ?it/s]
                                       

  0%|          | 0/100 [00:00<?, ?it/s]
"""