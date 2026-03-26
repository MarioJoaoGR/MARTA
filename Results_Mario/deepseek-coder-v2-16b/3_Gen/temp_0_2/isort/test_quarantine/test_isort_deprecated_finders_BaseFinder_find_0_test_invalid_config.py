
from isort.deprecated.finders import BaseFinder
from config import Config
import pytest

def test_invalid_config():
    with pytest.raises(NotImplementedError):
        # Attempt to instantiate the abstract class should raise an error
        BaseFinder(Config())

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_BaseFinder_find_0_test_invalid_config
isort/Test4DT_tests/test_isort_deprecated_finders_BaseFinder_find_0_test_invalid_config.py:3:0: E0401: Unable to import 'config' (import-error)
isort/Test4DT_tests/test_isort_deprecated_finders_BaseFinder_find_0_test_invalid_config.py:9:8: E0110: Abstract class 'BaseFinder' with abstract methods instantiated (abstract-class-instantiated)


"""