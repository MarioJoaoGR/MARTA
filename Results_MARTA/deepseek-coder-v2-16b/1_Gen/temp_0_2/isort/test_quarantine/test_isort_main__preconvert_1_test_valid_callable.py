
from isort.main import _preconvert
from isort import WrapModes
import pytest

def test__preconvert_enum():
    assert _preconvert(WrapModes.MODE_A) == 'MODE_A'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_main__preconvert_1_test_valid_callable
isort/Test4DT_tests/test_isort_main__preconvert_1_test_valid_callable.py:3:0: E0611: No name 'WrapModes' in module 'isort' (no-name-in-module)


"""