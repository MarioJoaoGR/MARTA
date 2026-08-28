
import pytest
from string_utils.generation import validate

# Test valid positive integer within the range 1-3999
def test_valid_positive_integer():
    with pytest.raises(ValueError) as excinfo:
        validate(2500, 'number')
    assert str(excinfo.value) == '"number" must be an integer in the range 1-3999'

# Test valid negative number allowed, converting it to its absolute value before validation
def test_valid_negative_integer_allowed():
    with pytest.raises(ValueError) as excinfo:
        validate(-5, 'number', allow_negative=True)
    assert str(excinfo.value) == '"number" must be an integer in the range 1-3999'

# Test that raises ValueError because the argument is not an integer
def test_invalid_argument_type():
    with pytest.raises(ValueError) as excinfo:
        validate('not an integer', 'number')
    assert str(excinfo.value) == '"number" must be an integer in the range 1-3999'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_________ ERROR collecting test_string_utils_generation_validate_0.py __________
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_generation_validate_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_generation_validate_0.py:3: in <module>
    from string_utils.generation import validate
E   ImportError: cannot import name 'validate' from 'string_utils.generation' (/opt/marta/baselines/codamosa/replication/test-apps/python-string-utils/string_utils/generation.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_generation_validate_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.13s ===============================
"""