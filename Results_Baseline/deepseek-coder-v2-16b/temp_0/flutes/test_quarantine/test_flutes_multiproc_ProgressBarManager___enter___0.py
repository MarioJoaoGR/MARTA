
import pytest
from flutes.multiproc import ProgressBarManager
import functools
import time
import random
import multiprocessing as mp
from typing import List, Iterable, Dict, Any, Optional, Union, Literal, Iterator, overload

# Helper function to simulate data for testing
def generate_data(size: int):
    return [random.randint(1, 100) for _ in range(size)]

@pytest.fixture
def manager():
    return ProgressBarManager(verbose=True)

def test_new_progress_bar(manager):
    xs = generate_data(200)
    bar = manager.proxy()  # Correctly call the proxy method
    iterable = iter(xs)
    wrapped_iterable = bar.new(iterable, update_frequency=10, total=len(xs))
    
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

flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___0.py F [100%]

=================================== FAILURES ===================================
____________________________ test_new_progress_bar _____________________________

manager = <flutes.multiproc.ProgressBarManager object at 0x7f0920a84610>

    def test_new_progress_bar(manager):
        xs = generate_data(200)
>       bar = manager.proxy()  # Correctly call the proxy method
E       TypeError: 'Proxy' object is not callable

flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___0.py:20: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___0.py::test_new_progress_bar
============================== 1 failed in 0.12s ===============================
"""