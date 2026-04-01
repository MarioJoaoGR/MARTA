
from isort.deprecated.finders import BaseFinder
from config import Config
import pytest

def test_invalid_config():
    with pytest.raises(TypeError):
        # Attempting to instantiate an abstract class should raise a TypeError
        BaseFinder(config=Config())

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_BaseFinder___init___0_test_invalid_config
isort/Test4DT_tests/test_isort_deprecated_finders_BaseFinder___init___0_test_invalid_config.py:3:0: E0401: Unable to import 'config' (import-error)
isort/Test4DT_tests/test_isort_deprecated_finders_BaseFinder___init___0_test_invalid_config.py:9:8: E0110: Abstract class 'BaseFinder' with abstract methods instantiated (abstract-class-instantiated)


"""