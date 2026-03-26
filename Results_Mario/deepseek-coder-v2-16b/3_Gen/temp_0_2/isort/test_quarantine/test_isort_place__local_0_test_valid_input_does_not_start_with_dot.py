
from isort.place import _local, LOCAL
from isort.config import Config
import pytest

def test_valid_input_does_not_start_with_dot():
    result = _local("module_name", Config())
    assert result is None

def test_valid_input_starts_with_dot():
    result = _local(".module_name", Config())
    assert result == (LOCAL, "Module name started with a dot.")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_place__local_0_test_valid_input_does_not_start_with_dot
isort/Test4DT_tests/test_isort_place__local_0_test_valid_input_does_not_start_with_dot.py:3:0: E0401: Unable to import 'isort.config' (import-error)
isort/Test4DT_tests/test_isort_place__local_0_test_valid_input_does_not_start_with_dot.py:3:0: E0611: No name 'config' in module 'isort' (no-name-in-module)


"""