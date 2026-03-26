
import pytest
import functools
import time
import random
from typing import List, Iterable, Dict, Optional, Union, Iterator, Any
import multiprocessing as mp
import threading
from flutes.multiproc import ProgressBarManager, Event, NewEvent, UpdateEvent, WriteEvent, CloseEvent, QuitEvent
from tqdm import tqdm

def test_invalid_inputs():
    manager = ProgressBarManager()
    
    # Test invalid iterable type
    with pytest.raises(ValueError):
        manager.proxy.new("not an iterable")  # This should raise a ValueError because "not an iterable" is not iterable

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

flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager__run_0_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        manager = ProgressBarManager()
    
        # Test invalid iterable type
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager__run_0_test_invalid_inputs.py:16: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager__run_0_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.12s ===============================


  0%|          | 0/15 [00:00<?, ?it/s]
"""