
import pytest
from isort.deprecated.finders import ReqsBaseFinder

# Mock Config class for testing purposes
class Config:
    pass

def test_valid_input():
    config = Config()
    finder = ReqsBaseFinder(config=config, path=".")
    
    assert not finder.enabled  # Assuming enabled is False by default in the actual implementation
    assert finder.path == "."
    assert finder.mapping is None
    assert finder.names is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_ReqsBaseFinder__get_parents_0_test_valid_input
isort/Test4DT_tests/test_isort_deprecated_finders_ReqsBaseFinder__get_parents_0_test_valid_input.py:11:13: E0110: Abstract class 'ReqsBaseFinder' with abstract methods instantiated (abstract-class-instantiated)


"""