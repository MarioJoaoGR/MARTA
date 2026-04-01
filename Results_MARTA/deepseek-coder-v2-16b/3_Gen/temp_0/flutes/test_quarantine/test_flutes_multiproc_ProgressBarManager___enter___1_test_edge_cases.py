
import pytest
from flutes.multiproc import ProgressBarManager

@pytest.fixture
def progress_bar_manager():
    return ProgressBarManager()

def test_new(progress_bar_manager):
    iterable = [1, 2, 3, 4, 5]
    bar = progress_bar_manager.proxy.new(iterable=iterable)
    assert isinstance(bar, type(iterable)) or isinstance(bar, ProgressBarManager._DummyProxy)

def test_update(progress_bar_manager):
    iterable = [1, 2, 3, 4, 5]
    bar = progress_bar_manager.proxy.new(iterable=iterable)
    assert isinstance(bar, type(iterable)) or isinstance(bar, ProgressBarManager._DummyProxy)
    for _ in range(len(iterable)):
        bar.update(1)

def test_write(progress_bar_manager):
    message = "Test message"
    progress_bar_manager.proxy.write(message)

def test_close(progress_bar_manager):
    iterable = [1, 2, 3, 4, 5]
    bar = progress_bar_manager.proxy.new(iterable=iterable)
    assert isinstance(bar, type(iterable)) or isinstance(bar, ProgressBarManager._DummyProxy)
    for _ in range(len(iterable)):
        bar.update(1)
    bar.close()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 4 items

flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___1_test_edge_cases.py F [ 25%]
FTest message
.F                                                                      [100%]

=================================== FAILURES ===================================
___________________________________ test_new ___________________________________

progress_bar_manager = <flutes.multiproc.ProgressBarManager object at 0x7f8f746b23d0>

    def test_new(progress_bar_manager):
        iterable = [1, 2, 3, 4, 5]
        bar = progress_bar_manager.proxy.new(iterable=iterable)
>       assert isinstance(bar, type(iterable)) or isinstance(bar, ProgressBarManager._DummyProxy)
E       AssertionError: assert (False or False)
E        +  where False = isinstance(<generator object ProgressBarManager.Proxy._iter_per_elems at 0x7f8f74ade680>, <class 'list'>)
E        +    where <class 'list'> = type([1, 2, 3, 4, 5])
E        +  and   False = isinstance(<generator object ProgressBarManager.Proxy._iter_per_elems at 0x7f8f74ade680>, <class 'flutes.multiproc.ProgressBarManager._DummyProxy'>)
E        +    where <class 'flutes.multiproc.ProgressBarManager._DummyProxy'> = ProgressBarManager._DummyProxy

flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___1_test_edge_cases.py:12: AssertionError
_________________________________ test_update __________________________________

progress_bar_manager = <flutes.multiproc.ProgressBarManager object at 0x7f8f748ba110>

    def test_update(progress_bar_manager):
        iterable = [1, 2, 3, 4, 5]
        bar = progress_bar_manager.proxy.new(iterable=iterable)
>       assert isinstance(bar, type(iterable)) or isinstance(bar, ProgressBarManager._DummyProxy)
E       AssertionError: assert (False or False)
E        +  where False = isinstance(<generator object ProgressBarManager.Proxy._iter_per_elems at 0x7f8f748d4bf0>, <class 'list'>)
E        +    where <class 'list'> = type([1, 2, 3, 4, 5])
E        +  and   False = isinstance(<generator object ProgressBarManager.Proxy._iter_per_elems at 0x7f8f748d4bf0>, <class 'flutes.multiproc.ProgressBarManager._DummyProxy'>)
E        +    where <class 'flutes.multiproc.ProgressBarManager._DummyProxy'> = ProgressBarManager._DummyProxy

flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___1_test_edge_cases.py:17: AssertionError
__________________________________ test_close __________________________________

progress_bar_manager = <flutes.multiproc.ProgressBarManager object at 0x7f8f747f62d0>

    def test_close(progress_bar_manager):
        iterable = [1, 2, 3, 4, 5]
        bar = progress_bar_manager.proxy.new(iterable=iterable)
>       assert isinstance(bar, type(iterable)) or isinstance(bar, ProgressBarManager._DummyProxy)
E       AssertionError: assert (False or False)
E        +  where False = isinstance(<generator object ProgressBarManager.Proxy._iter_per_elems at 0x7f8f748d7120>, <class 'list'>)
E        +    where <class 'list'> = type([1, 2, 3, 4, 5])
E        +  and   False = isinstance(<generator object ProgressBarManager.Proxy._iter_per_elems at 0x7f8f748d7120>, <class 'flutes.multiproc.ProgressBarManager._DummyProxy'>)
E        +    where <class 'flutes.multiproc.ProgressBarManager._DummyProxy'> = ProgressBarManager._DummyProxy

flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___1_test_edge_cases.py:28: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___1_test_edge_cases.py::test_new
FAILED flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___1_test_edge_cases.py::test_update
FAILED flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___1_test_edge_cases.py::test_close
========================= 3 failed, 1 passed in 0.19s ==========================


  0%|          | 0/5 [00:00<?, ?it/s]
  0%|          | 0/5 [00:00<?, ?it/s]
                                     

                                     

  0%|          | 0/5 [00:00<?, ?it/s]
  0%|          | 0/5 [00:00<?, ?it/s]
  0%|          | 0/5 [00:00<?, ?it/s]
"""