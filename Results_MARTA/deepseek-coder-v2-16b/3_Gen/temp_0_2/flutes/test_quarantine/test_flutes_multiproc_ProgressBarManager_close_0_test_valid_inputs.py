
import pytest
from flutes.multiproc import ProgressBarManager, run, run2
import time
import random
import functools
import multiprocessing as mp
from typing import List, Iterable, Dict, Optional, Any, Union, Literal

@pytest.fixture
def setup_manager():
    manager = ProgressBarManager(verbose=True)
    yield manager
    # Teardown code here if necessary

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_ProgressBarManager_close_0_test_valid_inputs
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager_close_0_test_valid_inputs.py:3:0: E0611: No name 'run' in module 'flutes.multiproc' (no-name-in-module)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager_close_0_test_valid_inputs.py:3:0: E0611: No name 'run2' in module 'flutes.multiproc' (no-name-in-module)


"""