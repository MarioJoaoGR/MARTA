
import pytest
import functools
import time
import random
from typing import List, Iterable, Optional, Dict, Any, Union, Literal, Iterator
import multiprocessing as mp
import threading
from collections import defaultdict
from flutes.multiproc import ProgressBarManager

def test_edge_case():
    manager = ProgressBarManager(verbose=True)
    
    # Test None input
    with pytest.raises(ValueError):
        manager.proxy.new(iterable=None, update_frequency=0.1)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___init___0_test_edge_case.py F [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

    def test_edge_case():
        manager = ProgressBarManager(verbose=True)
    
        # Test None input
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___init___0_test_edge_case.py:16: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___init___0_test_edge_case.py::test_edge_case
============================== 1 failed in 0.15s ===============================


0it [00:00, ?it/s]
"""