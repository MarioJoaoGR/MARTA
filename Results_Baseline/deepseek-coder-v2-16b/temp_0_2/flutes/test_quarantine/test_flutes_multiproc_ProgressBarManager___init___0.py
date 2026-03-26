
# Module: flutes.multiproc
import pytest
from flutes.multiproc import ProgressBarManager
import functools
import multiprocessing as mp
import threading
import time
import random
from typing import List, Iterable, Optional, Dict, Any, Union, Literal, Iterator

# Assuming the following imports are available in the module:
# from tqdm import tqdm
# import flutes
# from .log import set_console_logging_function, _get_console_logging_function

def run(xs: List[int], *, bar) -> int:
    # Create a new progress bar for the current worker.
    bar.new(total=len(xs), desc="Worker {flutes.get_worker_id()}")
    # Compute-intensive stuff!
    result = 0
    for idx, x in enumerate(xs):
        result += x
        time.sleep(random.uniform(0.01, 0.2))
        bar.update(1, postfix={"sum": result})  # update progress
        if (idx + 1) % 100 == 0:
            # Logging works without messing up terminal output.
            flutes.log(f"Processed {idx + 1} samples")
    return result

def run2(xs: List[int], *, bar) -> int:
    # An alternative way to achieve the same functionalities (though slightly slower):
    result = 0
    for idx, x in enumerate(bar.iter(xs)):
        result += x
        time.sleep(random.uniform(0.01, 0.2))
        bar.update(postfix={"sum": result})  # update progress
        if (idx + 1) % 100 == 0:
            # Logging works without messing up terminal output.
            flutes.log(f"Processed {idx + 1} samples")
    return result

@pytest.fixture
def manager():
    return ProgressBarManager(verbose=True)

def test_ProgressBarManager_initialization(manager):
    assert isinstance(manager, ProgressBarManager)
    assert manager.verbose is True
    assert hasattr(manager, 'proxy')

def test_run_function(manager):
    xs = list(range(1000))
    run_fn = functools.partial(run, bar=manager.proxy)
    with mp.Pool(4) as pool:
        results = list(pool.imap_unordered(run_fn, [xs]*4))
        assert all([result == sum(xs) for result in results])

def test_run2_function(manager):
    xs = list(range(1000))
    run_fn = functools.partial(run2, bar=manager.proxy)
    with mp.Pool(4) as pool:
        results = list(pool.imap_unordered(run_fn, [xs]*4))
        assert all([result == sum(xs) for result in results])

def test_verbose_false(capsys):
    manager = ProgressBarManager(verbose=False)
    assert isinstance(manager._proxy, ProgressBarManager._DummyProxy)
    captured = capsys.readouterr()
    assert "Processed" not in captured.out

@pytest.mark.parametrize("update_frequency", [0.01, 10])
def test_new_with_float_update_frequency(manager, update_frequency):
    xs = list(range(1000))
    iterable = bar.iter(xs)
    wrapped_iterable = manager._proxy.new(iterable=iterable, update_frequency=update_frequency)
    assert isinstance(wrapped_iterable, Iterator)

def test_new_with_none_iterable():
    with pytest.raises(ValueError):
        manager._proxy.new()

def test_update_progress_bar():
    xs = list(range(1000))
    bar = manager._proxy.new(total=len(xs), desc="Test Bar")
    assert isinstance(bar, tqdm)
    for idx in range(len(xs)):
        manager._proxy.update(n=1, postfix={"sum": idx + 1})
    assert bar.n == len(xs)

def test_write_message():
    message = "Test Message"
    manager._proxy.write(message)
    captured = capsys.readouterr()
    assert message in captured.out

def test_close_progress_bar():
    xs = list(range(1000))
    bar = manager._proxy.new(total=len(xs), desc="Test Bar")
    manager._proxy.close()
    assert not bar.is_enabled()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_ProgressBarManager___init___0
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___init___0.py:28:12: E0602: Undefined variable 'flutes' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___init___0.py:40:12: E0602: Undefined variable 'flutes' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___init___0.py:75:15: E0602: Undefined variable 'bar' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___init___0.py:86:27: E0602: Undefined variable 'tqdm' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___init___0.py:94:15: E0602: Undefined variable 'capsys' (undefined-variable)


"""