
from isort.core import Config  # Importing from isort.core module as per instructions
import pytest

def test_invalid_input():
    with pytest.raises(TypeError):
        _indented_config("not a Config object", "    ")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_core__indented_config_1_test_invalid_input
isort/Test4DT_tests/test_isort_core__indented_config_1_test_invalid_input.py:7:8: E0602: Undefined variable '_indented_config' (undefined-variable)


"""