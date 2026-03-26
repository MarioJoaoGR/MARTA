
import pytest
from flutes.multiproc import ProgressBarManager

@pytest.fixture
def progress_bar_manager():
    return ProgressBarManager(verbose=True)

def test_valid_case(progress_bar_manager):
    manager = progress_bar_manager
    run_fn = functools.partial(run, bar=manager.proxy)
    with flutes.safe_pool(4) as pool:
        for idx, _ in enumerate(pool.imap_unordered(run_fn, data)):
            flutes.log(f"Processed {idx + 1} arrays")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_ProgressBarManager___exit___0_test_valid_case
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___exit___0_test_valid_case.py:11:13: E0602: Undefined variable 'functools' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___exit___0_test_valid_case.py:11:31: E0602: Undefined variable 'run' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___exit___0_test_valid_case.py:12:9: E0602: Undefined variable 'flutes' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___exit___0_test_valid_case.py:13:60: E0602: Undefined variable 'data' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___exit___0_test_valid_case.py:14:12: E0602: Undefined variable 'flutes' (undefined-variable)


"""