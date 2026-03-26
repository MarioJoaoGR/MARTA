
from unittest.mock import patch
import pytest
from string_utils.validation import is_string, InvalidInputError
from Test4DT_tests.test_string_utils_validation___ISBNChecker_is_isbn_13_1_test_invalid_isbn_13 import __ISBNChecker

def test_invalid_isbn_13():
    with pytest.raises(InvalidInputError):
        checker = __ISBNChecker("978-0-470-05902-9", normalize=False)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_ ERROR collecting Test4DT_tests/test_string_utils_validation___ISBNChecker_is_isbn_13_1_test_invalid_isbn_13.py _
ImportError while importing test module '/Users/mario/Desktop/GECAD/Test4Py/python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker_is_isbn_13_1_test_invalid_isbn_13.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/homebrew/Caskroom/miniconda/base/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker_is_isbn_13_1_test_invalid_isbn_13.py:5: in <module>
    from Test4DT_tests.test_string_utils_validation___ISBNChecker_is_isbn_13_1_test_invalid_isbn_13 import __ISBNChecker
E   ImportError: cannot import name '__ISBNChecker' from partially initialized module 'Test4DT_tests.test_string_utils_validation___ISBNChecker_is_isbn_13_1_test_invalid_isbn_13' (most likely due to a circular import) (/Users/mario/Desktop/GECAD/Test4Py/python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker_is_isbn_13_1_test_invalid_isbn_13.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker_is_isbn_13_1_test_invalid_isbn_13.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.07s ===============================

"""