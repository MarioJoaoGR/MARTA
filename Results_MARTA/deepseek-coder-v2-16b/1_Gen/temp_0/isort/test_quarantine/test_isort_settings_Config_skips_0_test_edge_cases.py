
import pytest
from isort.settings import Config

def test_skips():
    config = Config()
    assert isinstance(config.skips(), frozenset)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_settings_Config_skips_0_test_edge_cases
isort/Test4DT_tests/test_isort_settings_Config_skips_0_test_edge_cases.py:7:22: E1102: config.skips is not callable (not-callable)


"""