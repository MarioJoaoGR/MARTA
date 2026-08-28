
import pytest
import logging
from semantic_release.helpers import LoggedFunction

# Set up a logger for testing
logger = logging.getLogger("test_logger")
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

# Create an instance of LoggedFunction with the logger
logged_function = LoggedFunction(logger)

@logged_function
def example_function(a, b):
    """Example function to be decorated with debug logging."""
    return a + b

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_helpers_LoggedFunction___init___0.py F [100%]

=================================== FAILURES ===================================
_______________________ test_example_function_execution ________________________

    def test_example_function_execution():
        result = example_function(3, 4)
        assert result == 7
>       assert "Input arguments: a=3, b=4" in logger.handlers[0].stream.getvalue()
E       AttributeError: 'EncodedFile' object has no attribute 'getvalue'

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_helpers_LoggedFunction___init___0.py:26: AttributeError
----------------------------- Captured stderr call -----------------------------
2026-07-26 06:51:29,549 - test_logger - DEBUG - example_function(3, 4)
2026-07-26 06:51:29,549 - test_logger - DEBUG - example_function -> 7
------------------------------ Captured log call -------------------------------
DEBUG    test_logger:helpers.py:59 example_function(3, 4)
DEBUG    test_logger:helpers.py:74 example_function -> 7
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_helpers_LoggedFunction___init___0.py::test_example_function_execution
============================== 1 failed in 0.11s ===============================
"""