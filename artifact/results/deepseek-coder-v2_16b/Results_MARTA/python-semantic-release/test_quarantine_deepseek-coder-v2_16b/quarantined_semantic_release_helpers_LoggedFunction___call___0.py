
import pytest
from semantic_release.helpers import LoggedFunction
import logging

# Configure a logger for testing
logger = logging.getLogger("test_logger")
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

# Define a function to be decorated with debug logging for testing
@LoggedFunction(logger)
def example_function(a, b):
    return a + b

# Test that the logged function logs its arguments correctly

# Test that the logged function logs its return value correctly
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_helpers_LoggedFunction___call___0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
________________________ test_logged_function_arguments ________________________

    def test_logged_function_arguments():
>       result = example_function(1, 2, c=3)

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_helpers_LoggedFunction___call___0.py:22: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

args = (1, 2), kwargs = {'c': 3}

    @functools.wraps(func)
    def logged_func(*args, **kwargs):
        # Log function name and arguments
        self.logger.debug(
            "{function}({args}{kwargs})".format(
                function=func.__name__,
                args=", ".join([format_arg(x) for x in args]),
                kwargs="".join(
                    [f", {k}={format_arg(v)}" for k, v in kwargs.items()]
                ),
            )
        )
    
        # Call function
>       result = func(*args, **kwargs)
E       TypeError: example_function() got an unexpected keyword argument 'c'

/opt/marta/baselines/codamosa/replication/test-apps/python-semantic-release/semantic_release/helpers.py:70: TypeError
----------------------------- Captured stderr call -----------------------------
2026-07-26 06:51:52,302 - test_logger - DEBUG - example_function(1, 2, c=3)
------------------------------ Captured log call -------------------------------
DEBUG    test_logger:helpers.py:59 example_function(1, 2, c=3)
_________________________ test_logged_function_return __________________________

    def test_logged_function_return():
        result = example_function(3, 4)
>       assert logger.debug.call_count == 2
E       AttributeError: 'function' object has no attribute 'call_count'

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_helpers_LoggedFunction___call___0.py:38: AttributeError
----------------------------- Captured stderr call -----------------------------
2026-07-26 06:51:52,329 - test_logger - DEBUG - example_function(3, 4)
2026-07-26 06:51:52,329 - test_logger - DEBUG - example_function -> 7
------------------------------ Captured log call -------------------------------
DEBUG    test_logger:helpers.py:59 example_function(3, 4)
DEBUG    test_logger:helpers.py:74 example_function -> 7
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_helpers_LoggedFunction___call___0.py::test_logged_function_arguments
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_helpers_LoggedFunction___call___0.py::test_logged_function_return
============================== 2 failed in 0.12s ===============================
"""