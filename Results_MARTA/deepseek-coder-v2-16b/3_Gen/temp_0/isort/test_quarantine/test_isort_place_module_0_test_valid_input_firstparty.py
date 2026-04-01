
import pytest
from isort.place import module as isort_module
from isort.config import Config, DEFAULT_CONFIG

def test_valid_input_firstparty():
    config = Config()
    assert isort_module("example", config) == 'FIRSTPARTY'
    
    another_config = Config()
    another_config.forced_separate = ["*.log"]
    assert isort_module("app.log", another_config) == 'FIRSTPARTY'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_place_module_0_test_valid_input_firstparty
isort/Test4DT_tests/test_isort_place_module_0_test_valid_input_firstparty.py:4:0: E0401: Unable to import 'isort.config' (import-error)
isort/Test4DT_tests/test_isort_place_module_0_test_valid_input_firstparty.py:4:0: E0611: No name 'config' in module 'isort' (no-name-in-module)


"""