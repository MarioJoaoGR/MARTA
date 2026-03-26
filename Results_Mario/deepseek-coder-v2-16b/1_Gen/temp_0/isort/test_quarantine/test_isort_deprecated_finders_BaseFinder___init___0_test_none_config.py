
from isort.deprecated.finders import BaseFinder
from config import Config
import pytest

@pytest.fixture
def create_basefinder():
    def _create_basefinder(config=None):
        return BaseFinder(config)
    return _create_basefinder

def test_none_config(create_basefinder):
    finder = create_basefinder()
    assert isinstance(finder.config, Config)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_BaseFinder___init___0_test_none_config
isort/Test4DT_tests/test_isort_deprecated_finders_BaseFinder___init___0_test_none_config.py:3:0: E0401: Unable to import 'config' (import-error)
isort/Test4DT_tests/test_isort_deprecated_finders_BaseFinder___init___0_test_none_config.py:9:15: E0110: Abstract class 'BaseFinder' with abstract methods instantiated (abstract-class-instantiated)


"""