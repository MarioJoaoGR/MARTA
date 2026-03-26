
import pytest
from flutes.multiproc import ProgressBarManager
import multiprocessing as mp
import functools
import time
import random
from typing import List, Iterable, Dict, Any, Optional, Union, Literal, Iterator, overload

@pytest.fixture(scope="module")
def progress_bar_manager():
    return ProgressBarManager()

def test_proxy_creation(progress_bar_manager):
    proxy = progress_bar_manager.proxy()
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

flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager_proxy_0.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_proxy_creation ______________________________

progress_bar_manager = <flutes.multiproc.ProgressBarManager object at 0x7f26d898b690>

    def test_proxy_creation(progress_bar_manager):
>       proxy = progress_bar_manager.proxy()
E       TypeError: 'Proxy' object is not callable

flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager_proxy_0.py:15: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager_proxy_0.py::test_proxy_creation
============================== 1 failed in 0.13s ===============================
"""