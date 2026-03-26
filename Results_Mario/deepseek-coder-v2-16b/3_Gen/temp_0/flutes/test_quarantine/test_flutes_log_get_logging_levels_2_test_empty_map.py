
from flutes.log import get_logging_levels
from typing import List

def test_empty_map():
    # Assuming LEVEL_MAP is not defined or is empty for this test
    global LEVEL_MAP
    LEVEL_MAP = {}  # Define an empty dictionary to simulate no levels
    
    levels = get_logging_levels()
    assert not levels, "Expected an empty list of logging levels"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_log_get_logging_levels_2_test_empty_map.py F [100%]

=================================== FAILURES ===================================
________________________________ test_empty_map ________________________________

    def test_empty_map():
        # Assuming LEVEL_MAP is not defined or is empty for this test
        global LEVEL_MAP
        LEVEL_MAP = {}  # Define an empty dictionary to simulate no levels
    
        levels = get_logging_levels()
>       assert not levels, "Expected an empty list of logging levels"
E       AssertionError: Expected an empty list of logging levels
E       assert not ['success', 'warning', 'error', 'info', 'quiet']

flutes/Test4DT_tests/test_flutes_log_get_logging_levels_2_test_empty_map.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_log_get_logging_levels_2_test_empty_map.py::test_empty_map
============================== 1 failed in 0.09s ===============================

"""