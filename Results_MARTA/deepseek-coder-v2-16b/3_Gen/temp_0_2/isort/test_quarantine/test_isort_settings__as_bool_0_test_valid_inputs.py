
import pytest
from isort.settings import _STR_BOOLEAN_MAPPING

def test_valid_inputs():
    assert _as_bool('true') == True
    assert _as_bool('false') == False
    assert _as_bool('yes') == True
    assert _as_bool('no') == False
    assert _as_bool('on') == True
    assert _as_bool('off') == False
    assert _as_bool('1') == True
    assert _as_bool('0') == False
    
    with pytest.raises(ValueError) as excinfo:
        _as_bool('maybe')
    assert str(excinfo.value) == "invalid truth value maybe"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_settings__as_bool_0_test_valid_inputs
isort/Test4DT_tests/test_isort_settings__as_bool_0_test_valid_inputs.py:6:11: E0602: Undefined variable '_as_bool' (undefined-variable)
isort/Test4DT_tests/test_isort_settings__as_bool_0_test_valid_inputs.py:7:11: E0602: Undefined variable '_as_bool' (undefined-variable)
isort/Test4DT_tests/test_isort_settings__as_bool_0_test_valid_inputs.py:8:11: E0602: Undefined variable '_as_bool' (undefined-variable)
isort/Test4DT_tests/test_isort_settings__as_bool_0_test_valid_inputs.py:9:11: E0602: Undefined variable '_as_bool' (undefined-variable)
isort/Test4DT_tests/test_isort_settings__as_bool_0_test_valid_inputs.py:10:11: E0602: Undefined variable '_as_bool' (undefined-variable)
isort/Test4DT_tests/test_isort_settings__as_bool_0_test_valid_inputs.py:11:11: E0602: Undefined variable '_as_bool' (undefined-variable)
isort/Test4DT_tests/test_isort_settings__as_bool_0_test_valid_inputs.py:12:11: E0602: Undefined variable '_as_bool' (undefined-variable)
isort/Test4DT_tests/test_isort_settings__as_bool_0_test_valid_inputs.py:13:11: E0602: Undefined variable '_as_bool' (undefined-variable)
isort/Test4DT_tests/test_isort_settings__as_bool_0_test_valid_inputs.py:16:8: E0602: Undefined variable '_as_bool' (undefined-variable)


"""