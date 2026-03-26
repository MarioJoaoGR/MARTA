
# Importing the get_logging_levels function from the flutes module
from flute import get_logging_levels  # Corrected import statement
import logging
from typing import List

def test_get_logging_levels():
    levels = get_logging_levels()
    expected_levels = list(logging.Logger.manager.loggerDict.keys())
    assert set(levels) == set(expected_levels), f"Expected {expected_levels}, but got {levels}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_log_get_logging_levels_0_test_edge_case
flutes/Test4DT_tests/test_flutes_log_get_logging_levels_0_test_edge_case.py:3:0: E0401: Unable to import 'flute' (import-error)


"""