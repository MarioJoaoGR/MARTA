
import pytest
from isort import settings

def _as_bool(value: str) -> bool:
    """Given a string value that represents True or False, returns the Boolean equivalent.
    Heavily inspired from distutils strtobool.
    """
    try:
        return _STR_BOOLEAN_MAPPING[value.lower()]
    except KeyError:
        raise ValueError(f"invalid truth value {value}")

def test_invalid_input():
    with pytest.raises(ValueError) as excinfo:
        _as_bool('maybe')
    assert str(excinfo.value) == "invalid truth value maybe"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_settings__as_bool_1_test_invalid_input
isort/Test4DT_tests/test_isort_settings__as_bool_1_test_invalid_input.py:10:15: E0602: Undefined variable '_STR_BOOLEAN_MAPPING' (undefined-variable)


"""