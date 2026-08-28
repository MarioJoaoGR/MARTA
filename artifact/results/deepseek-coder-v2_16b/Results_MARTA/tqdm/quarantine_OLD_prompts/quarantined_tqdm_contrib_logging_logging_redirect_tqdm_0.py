
import pytest
from tqdm.contrib.logging import logging_redirect_tqdm
import logging
from tqdm import trange, std_tqdm

# Create a logger for testing
logger = logging.getLogger('test_logger')

def test_logging_redirect_tqdm_default():
    with patch('builtins.print', new=lambda *args: None):  # Mock print to avoid output in tests
        logging.basicConfig(level=logging.INFO)
        with logging_redirect_tqdm():
            for i in trange(9):
                if i == 4:
                    logger.info("console logging redirected to `tqdm.write()`")
    # Check that the log message was captured by tqdm.write()
    assert "console logging redirected to `tqdm.write()`" in std_tqdm.get().__str__()

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
____ ERROR collecting test_tqdm_contrib_logging_logging_redirect_tqdm_0.py _____
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b/test_tqdm_contrib_logging_logging_redirect_tqdm_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b/test_tqdm_contrib_logging_logging_redirect_tqdm_0.py:5: in <module>
    from tqdm import trange, std_tqdm
E   ImportError: cannot import name 'std_tqdm' from 'tqdm' (/opt/marta/baselines/codamosa/replication/test-apps/tqdm/tqdm/__init__.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b/test_tqdm_contrib_logging_logging_redirect_tqdm_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.12s ===============================
"""