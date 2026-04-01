
import pytest
import functools
import time
import random
from typing import List, Iterable, Optional, Dict, Any, Union, Literal, Iterator
import multiprocessing as mp
import threading
from collections import defaultdict
from tqdm import tqdm
from flutes.multiproc import ProgressBarManager

# Assuming data is defined somewhere in the test module or imported from a fixture
data = [1, 2, 3, 4, 5] * 100

@pytest.fixture
def progress_bar_manager():
    manager = ProgressBarManager(verbose=True)
    yield manager
    manager.close()

def test_invalid_inputs(progress_bar_manager):
    with pytest.raises(ValueError):
        # Test invalid iterable type
        progress_bar_manager.proxy.new(iterable="not an iterable")  # This should raise a ValueError

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager_close_2_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

progress_bar_manager = <flutes.multiproc.ProgressBarManager object at 0x7ff06b677390>

    def test_invalid_inputs(progress_bar_manager):
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager_close_2_test_invalid_inputs.py:23: Failed
--------------------------- Captured stderr teardown ---------------------------

                                      
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager_close_2_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.13s ===============================

"""