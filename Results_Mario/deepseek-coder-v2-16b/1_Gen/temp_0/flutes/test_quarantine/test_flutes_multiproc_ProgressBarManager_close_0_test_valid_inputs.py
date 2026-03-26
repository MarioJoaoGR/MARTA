
import pytest
from flutes.Test4DT_tests import log  # Assuming this is the correct module path
from flutes.multiproc import ProgressBarManager, Event, NewEvent, UpdateEvent, WriteEvent, CloseEvent, QuitEvent
import functools
import time
import random
from typing import List, Iterable, Optional, Dict, Any, Union, Literal, Iterator, overload
import multiprocessing as mp
import threading
from collections import defaultdict

class TestProgressBarManager:
    def test_valid_inputs(self):
        # Assuming data is defined somewhere in the scope of this test
        data = [list(range(100)) for _ in range(4)]  # Example data

        manager = ProgressBarManager()
        
        def run(xs: List[int], *, bar):
            bar.new(total=len(xs), desc="Worker {flutes.get_worker_id()}")
            result = 0
            for idx, x in enumerate(xs):
                result += x
                time.sleep(random.uniform(0.01, 0.2))
                bar.update(1, postfix={"sum": result})
                if (idx + 1) % 100 == 0:
                    flutes.log(f"Processed {idx + 1} samples")
            return result
        
        def run2(xs: List[int], *, bar):
            result = 0
            for idx, x in enumerate(bar.iter(xs)):
                result += x
                time.sleep(random.uniform(0.01, 0.2))
                bar.update(1, postfix={"sum": result})
                if (idx + 1) % 100 == 0:
                    flutes.log(f"Processed {idx + 1} samples")
            return result
        
        run_fn = functools.partial(run, bar=manager.proxy)
        with mp.Pool(4) as pool:
            for idx, _ in enumerate(pool.imap_unordered(run_fn, data)):
                flutes.log(f"Processed {idx + 1} arrays")
        
        manager.close()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_ProgressBarManager_close_0_test_valid_inputs
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager_close_0_test_valid_inputs.py:3:0: E0401: Unable to import 'flutes.Test4DT_tests' (import-error)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager_close_0_test_valid_inputs.py:3:0: E0611: No name 'Test4DT_tests' in module 'flutes' (no-name-in-module)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager_close_0_test_valid_inputs.py:28:20: E0602: Undefined variable 'flutes' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager_close_0_test_valid_inputs.py:38:20: E0602: Undefined variable 'flutes' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager_close_0_test_valid_inputs.py:44:16: E0602: Undefined variable 'flutes' (undefined-variable)


"""