
import pytest
from flutes.multiproc import ProgressBarManager

@pytest.fixture
def setup_progress_bar():
    manager = ProgressBarManager(verbose=True)
    yield manager
    # Ensure the progress bar is closed after the test
    manager.__exit__(None, None, None)

def test_edge_cases(setup_progress_bar):
    manager = setup_progress_bar
    data = [1, 2, 3, 4, 5]  # Example data
    
    def run(xs: list, *, bar):
        bar.new(total=len(xs), desc="Worker {flutes.get_worker_id()}")
        result = 0
        for idx, x in enumerate(xs):
            result += x
            time.sleep(random.uniform(0.01, 0.2))
            bar.update(1, postfix={"sum": result})  # update progress
            if (idx + 1) % 100 == 0:
                flutes.log(f"Processed {idx + 1} samples")
        return result
    
    def run2(xs: list, *, bar):
        result = 0
        for idx, x in enumerate(bar.iter(xs)):
            result += x
            time.sleep(random.uniform(0.01, 0.2))
            bar.update(postfix={"sum": result})  # update progress
            if (idx + 1) % 100 == 0:
                flutes.log(f"Processed {idx + 1} samples")
        return result
    
    manager = flutes.ProgressBarManager()
    run_fn = functools.partial(run, bar=manager.proxy)
    with flutes.safe_pool(4) as pool:
        for idx, _ in enumerate(pool.imap_unordered(run_fn, data)):
            flutes.log(f"Processed {idx + 1} arrays")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_ProgressBarManager___exit___1_test_edge_cases
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___exit___1_test_edge_cases.py:21:12: E0602: Undefined variable 'time' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___exit___1_test_edge_cases.py:21:23: E0602: Undefined variable 'random' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___exit___1_test_edge_cases.py:24:16: E0602: Undefined variable 'flutes' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___exit___1_test_edge_cases.py:31:12: E0602: Undefined variable 'time' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___exit___1_test_edge_cases.py:31:23: E0602: Undefined variable 'random' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___exit___1_test_edge_cases.py:34:16: E0602: Undefined variable 'flutes' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___exit___1_test_edge_cases.py:37:14: E0602: Undefined variable 'flutes' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___exit___1_test_edge_cases.py:38:13: E0602: Undefined variable 'functools' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___exit___1_test_edge_cases.py:39:9: E0602: Undefined variable 'flutes' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___exit___1_test_edge_cases.py:41:12: E0602: Undefined variable 'flutes' (undefined-variable)


"""