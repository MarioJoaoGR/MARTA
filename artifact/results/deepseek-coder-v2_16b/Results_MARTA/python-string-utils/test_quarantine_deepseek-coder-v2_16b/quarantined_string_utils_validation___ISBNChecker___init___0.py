
import pytest
from string_utils.__ISBNChecker import __ISBNChecker, InvalidInputError

# Test for initializing __ISBNChecker with a valid ISBN-13 number and normalization enabled
def test_valid_isbn_normalization():
    checker = __ISBNChecker("978-0-13-235088-4", normalize=True)
    assert checker.input_string == "9780132350884"

# Test for initializing __ISBNChecker with a valid ISBN-13 number and normalization disabled
def test_valid_isbn_no_normalization():
    checker = __ISBNChecker("9780132350884", normalize=False)
    assert checker.input_string == "9780132350884"

# Test for initializing __ISBNChecker with an invalid ISBN-13 number, should raise InvalidInputError
def test_invalid_isbn():
    with pytest.raises(InvalidInputError):
        checker = __ISBNChecker("978045145052")

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
__ ERROR collecting test_string_utils_validation___ISBNChecker___init___0.py ___
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_validation___ISBNChecker___init___0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_validation___ISBNChecker___init___0.py:3: in <module>
    from string_utils.__ISBNChecker import __ISBNChecker, InvalidInputError
E   ModuleNotFoundError: No module named 'string_utils.__ISBNChecker'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_validation___ISBNChecker___init___0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.12s ===============================
"""