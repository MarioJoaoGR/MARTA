
from isort.deprecated.finders import BaseFinder
from config import Config
import pytest

def test_find_method_not_implemented():
    with pytest.raises(NotImplementedError):
        finder = BaseFinder(Config())
        finder.find("module_name")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_BaseFinder_find_0_test_find_method_not_implemented
isort/Test4DT_tests/test_isort_deprecated_finders_BaseFinder_find_0_test_find_method_not_implemented.py:3:0: E0401: Unable to import 'config' (import-error)
isort/Test4DT_tests/test_isort_deprecated_finders_BaseFinder_find_0_test_find_method_not_implemented.py:8:17: E0110: Abstract class 'BaseFinder' with abstract methods instantiated (abstract-class-instantiated)


"""