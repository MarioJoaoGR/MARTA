
import pytest
from isort.settings import _STR_BOOLEAN_MAPPING

def test_valid_case_false():
    assert not _as_bool('false')
    assert not _as_bool('False')
    assert not _as_bool('FALSE')
    assert not _as_bool('off')
    assert not _as_bool('Off')
    assert not _as_bool('OFF')
    assert not _as_bool('0')
    
    with pytest.raises(ValueError) as excinfo:
        _as_bool('maybe')
    assert str(excinfo.value) == "invalid truth value maybe"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_settings__as_bool_1_test_valid_case_false
isort/Test4DT_tests/test_isort_settings__as_bool_1_test_valid_case_false.py:6:15: E0602: Undefined variable '_as_bool' (undefined-variable)
isort/Test4DT_tests/test_isort_settings__as_bool_1_test_valid_case_false.py:7:15: E0602: Undefined variable '_as_bool' (undefined-variable)
isort/Test4DT_tests/test_isort_settings__as_bool_1_test_valid_case_false.py:8:15: E0602: Undefined variable '_as_bool' (undefined-variable)
isort/Test4DT_tests/test_isort_settings__as_bool_1_test_valid_case_false.py:9:15: E0602: Undefined variable '_as_bool' (undefined-variable)
isort/Test4DT_tests/test_isort_settings__as_bool_1_test_valid_case_false.py:10:15: E0602: Undefined variable '_as_bool' (undefined-variable)
isort/Test4DT_tests/test_isort_settings__as_bool_1_test_valid_case_false.py:11:15: E0602: Undefined variable '_as_bool' (undefined-variable)
isort/Test4DT_tests/test_isort_settings__as_bool_1_test_valid_case_false.py:12:15: E0602: Undefined variable '_as_bool' (undefined-variable)
isort/Test4DT_tests/test_isort_settings__as_bool_1_test_valid_case_false.py:15:8: E0602: Undefined variable '_as_bool' (undefined-variable)


"""