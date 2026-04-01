
from unittest.mock import MagicMock
import pytest
from isort.deprecated.finders import ReqsBaseFinder
from config import Config

# Mocking the Config class since it's not defined in the provided scenario
class MockConfig(Config):
    def __init__(self, enabled=False):
        self.enabled = enabled

def test_disabled_case():
    # Create a mock instance of ReqsBaseFinder with disabled state
    config = MockConfig(enabled=False)
    finder = ReqsBaseFinder(config=config, path=".")
    
    # Test the find method when finder is disabled
    result = finder.find('requests')
    assert result is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_ReqsBaseFinder_find_0_test_disabled_case
isort/Test4DT_tests/test_isort_deprecated_finders_ReqsBaseFinder_find_0_test_disabled_case.py:5:0: E0401: Unable to import 'config' (import-error)
isort/Test4DT_tests/test_isort_deprecated_finders_ReqsBaseFinder_find_0_test_disabled_case.py:15:13: E0110: Abstract class 'ReqsBaseFinder' with abstract methods instantiated (abstract-class-instantiated)


"""