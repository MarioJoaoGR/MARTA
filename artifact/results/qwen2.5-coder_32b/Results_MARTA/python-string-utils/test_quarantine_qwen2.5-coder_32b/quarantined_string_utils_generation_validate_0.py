
import pytest
from string_utils.generation import validate

def test_validate_positive_integer_within_range():
    validate(2023, 'year')
    # No exception should be raised

def test_validate_negative_integer_with_allow_negative_true():
    validate(-456, 'value', True)
    # No exception should be raised and it should internally convert to 456

def test_validate_value_outside_range_raises_error():
    with pytest.raises(ValueError) as excinfo:
        validate(4000, 'number')
    assert str(excinfo.value) == '"number" must be an integer in the range 1-3999'

def test_validate_non_integer_input_raises_error():
    with pytest.raises(ValueError) as excinfo:
        validate('2023', 'year')
    assert str(excinfo.value) == '"year" must be an integer in the range 1-3999'

def test_validate_zero_value_raises_error():
    with pytest.raises(ValueError) as excinfo:
        validate(0, 'zero_value')
    assert str(excinfo.value) == '"zero_value" must be an integer in the range 1-3999'

def test_validate_negative_integer_with_allow_negative_false_raises_error():
    with pytest.raises(ValueError) as excinfo:
        validate(-456, 'negative_value', False)
    assert str(excinfo.value) == '"negative_value" must be an integer in the range 1-3999'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_________ ERROR collecting test_string_utils_generation_validate_0.py __________
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_generation_validate_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_generation_validate_0.py:3: in <module>
    from string_utils.generation import validate
E   ImportError: cannot import name 'validate' from 'string_utils.generation' (/opt/marta/baselines/codamosa/replication/test-apps/python-string-utils/string_utils/generation.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_qwen2.5-coder_32b/test_string_utils_generation_validate_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.13s ===============================
"""