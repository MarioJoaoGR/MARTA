
import pytest
from isort.settings import _STR_BOOLEAN_MAPPING

def test_invalid_input():
    with pytest.raises(ValueError) as excinfo:
        assert _as_bool('maybe')
    assert str(excinfo.value) == "invalid truth value maybe"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_settings__as_bool_1_test_invalid_input
isort/Test4DT_tests/test_isort_settings__as_bool_1_test_invalid_input.py:7:15: E0602: Undefined variable '_as_bool' (undefined-variable)


"""