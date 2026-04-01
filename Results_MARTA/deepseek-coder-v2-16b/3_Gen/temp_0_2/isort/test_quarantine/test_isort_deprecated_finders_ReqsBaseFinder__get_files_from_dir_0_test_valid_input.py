
import pytest
from isort.deprecated.finders import ReqsBaseFinder
from unittest.mock import MagicMock

# Mocking Config class since it's not defined in the provided code
class Config:
    pass

@pytest.fixture
def setup_finder():
    config = Config()
    finder = ReqsBaseFinder(config=config, path=".")
    return finder

def test_valid_input(setup_finder):
    finder = setup_finder
    assert finder.enabled is False
    assert finder.path == "."
    assert finder.mapping is None
    assert finder.names is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_ReqsBaseFinder__get_files_from_dir_0_test_valid_input
isort/Test4DT_tests/test_isort_deprecated_finders_ReqsBaseFinder__get_files_from_dir_0_test_valid_input.py:13:13: E0110: Abstract class 'ReqsBaseFinder' with abstract methods instantiated (abstract-class-instantiated)


"""