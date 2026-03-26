
import pytest
from flutes.log import log
from logging import LoggingLevel

def test_edge_case_none():
    with pytest.raises(TypeError):
        log(None)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_log_log_0_test_edge_case_none
flutes/Test4DT_tests/test_flutes_log_log_0_test_edge_case_none.py:4:0: E0611: No name 'LoggingLevel' in module 'logging' (no-name-in-module)


"""