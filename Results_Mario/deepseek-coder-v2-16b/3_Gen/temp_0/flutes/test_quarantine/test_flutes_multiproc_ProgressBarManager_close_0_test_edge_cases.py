
import pytest
from flutes.multiproc import ProgressBarManager

@pytest.fixture
def progress_bar_manager():
    return ProgressBarManager(verbose=True)

def test_progress_bar_creation(progress_bar_manager):
    assert isinstance(progress_bar_manager._proxy, ProgressBarManager.Proxy)

def test_new_progress_bar(progress_bar_manager):
    iterable = [1, 2, 3, 4, 5]
    bar = progress_bar_manager._proxy.new(iterable=iterable, total=len(iterable))
    assert isinstance(bar, ProgressBarManager.Proxy)

def test_update_progress_bar(progress_bar_manager):
    iterable = [1, 2, 3, 4, 5]
    bar = progress_bar_manager._proxy.new(iterable=iterable, total=len(iterable))
    assert isinstance(bar, ProgressBarManager.Proxy)
    bar.update(n=1)

def test_write_message(progress_bar_manager):
    message = "Test message"
    progress_bar_manager._proxy.write(message)
    # Assuming the implementation of write captures this message, you might need to mock it for a complete test.

def test_close_progress_bar(progress_bar_manager):
    iterable = [1, 2, 3, 4, 5]
    bar = progress_bar_manager._proxy.new(iterable=iterable, total=len(iterable))
    assert isinstance(bar, ProgressBarManager.Proxy)
    bar.close()
    # Assuming the implementation of close waits for the thread to finish and closes all bars.

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 5 items

flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager_close_0_test_edge_cases.py . [ 20%]
FFTest message
.F                                                                     [100%]

=================================== FAILURES ===================================
____________________________ test_new_progress_bar _____________________________

progress_bar_manager = <flutes.multiproc.ProgressBarManager object at 0x7f7760fed550>

    def test_new_progress_bar(progress_bar_manager):
        iterable = [1, 2, 3, 4, 5]
        bar = progress_bar_manager._proxy.new(iterable=iterable, total=len(iterable))
>       assert isinstance(bar, ProgressBarManager.Proxy)
E       AssertionError: assert False
E        +  where False = isinstance(<generator object ProgressBarManager.Proxy._iter_per_elems at 0x7f77610d4d00>, <class 'flutes.multiproc.ProgressBarManager.Proxy'>)
E        +    where <class 'flutes.multiproc.ProgressBarManager.Proxy'> = ProgressBarManager.Proxy

flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager_close_0_test_edge_cases.py:15: AssertionError
___________________________ test_update_progress_bar ___________________________

progress_bar_manager = <flutes.multiproc.ProgressBarManager object at 0x7f7760fefc50>

    def test_update_progress_bar(progress_bar_manager):
        iterable = [1, 2, 3, 4, 5]
        bar = progress_bar_manager._proxy.new(iterable=iterable, total=len(iterable))
>       assert isinstance(bar, ProgressBarManager.Proxy)
E       AssertionError: assert False
E        +  where False = isinstance(<generator object ProgressBarManager.Proxy._iter_per_elems at 0x7f77610d7010>, <class 'flutes.multiproc.ProgressBarManager.Proxy'>)
E        +    where <class 'flutes.multiproc.ProgressBarManager.Proxy'> = ProgressBarManager.Proxy

flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager_close_0_test_edge_cases.py:20: AssertionError
___________________________ test_close_progress_bar ____________________________

progress_bar_manager = <flutes.multiproc.ProgressBarManager object at 0x7f77610107d0>

    def test_close_progress_bar(progress_bar_manager):
        iterable = [1, 2, 3, 4, 5]
        bar = progress_bar_manager._proxy.new(iterable=iterable, total=len(iterable))
>       assert isinstance(bar, ProgressBarManager.Proxy)
E       AssertionError: assert False
E        +  where False = isinstance(<generator object ProgressBarManager.Proxy._iter_per_elems at 0x7f77610d7120>, <class 'flutes.multiproc.ProgressBarManager.Proxy'>)
E        +    where <class 'flutes.multiproc.ProgressBarManager.Proxy'> = ProgressBarManager.Proxy

flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager_close_0_test_edge_cases.py:31: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager_close_0_test_edge_cases.py::test_new_progress_bar
FAILED flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager_close_0_test_edge_cases.py::test_update_progress_bar
FAILED flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager_close_0_test_edge_cases.py::test_close_progress_bar
========================= 3 failed, 2 passed in 0.18s ==========================


  0%|          | 0/5 [00:00<?, ?it/s]
  0%|          | 0/5 [00:00<?, ?it/s]
                                     

                                     

  0%|          | 0/5 [00:00<?, ?it/s]
  0%|          | 0/5 [00:00<?, ?it/s]
  0%|          | 0/5 [00:00<?, ?it/s]
"""