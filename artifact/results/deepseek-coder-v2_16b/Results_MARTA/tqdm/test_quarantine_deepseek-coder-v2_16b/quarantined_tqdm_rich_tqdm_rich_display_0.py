
import pytest
from tqdm_rich import tqdm_rich
import time

def test_tqdm_rich_basic():
    progress_bar = tqdm_rich(total=100)
    assert hasattr(progress_bar, 'n'), "Progress bar should have a `n` attribute"
    for i in range(100):
        time.sleep(0.1)
        progress_bar.update(1)
    assert progress_bar.n == 100, f"Expected n to be 100 but got {progress_bar.n}"
    progress_bar.close()

def test_tqdm_rich_custom_config():
    progress_bar = tqdm_rich(total=100, progress=(
        "[progress.description]{task.description}",
        BarColumn(),
        " [", TimeElapsedColumn(), "<", TimeRemainingColumn(), ",", RateColumn(), "]"
    ))
    assert hasattr(progress_bar, 'n'), "Progress bar should have a `n` attribute"
    for i in range(100):
        time.sleep(0.1)
        progress_bar.update(1)
    assert progress_bar.n == 100, f"Expected n to be 100 but got {progress_bar.n}"
    progress_bar.close()

def test_tqdm_rich_disable():
    progress_bar = tqdm_rich(total=100, disable=True)
    assert hasattr(progress_bar, 'disable'), "Progress bar should have a `disable` attribute"
    for i in range(100):
        time.sleep(0.1)
        progress_bar.update(1)
    assert not hasattr(progress_bar, 'n'), "If disable is True, the progress bar should not have an `n` attribute"

def test_tqdm_rich_with_loop():
    with tqdm_rich(total=100) as progress_bar:
        assert hasattr(progress_bar, 'n'), "Progress bar should have a `n` attribute when used in a context manager"
        for i in range(100):
            time.sleep(0.1)
            progress_bar.update(1)
        assert progress_bar.n == 100, f"Expected n to be 100 but got {progress_bar.n}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
____________ ERROR collecting test_tqdm_rich_tqdm_rich_display_0.py ____________
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b/test_tqdm_rich_tqdm_rich_display_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b/test_tqdm_rich_tqdm_rich_display_0.py:3: in <module>
    from tqdm_rich import tqdm_rich
E   ModuleNotFoundError: No module named 'tqdm_rich'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b/test_tqdm_rich_tqdm_rich_display_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.11s ===============================
"""