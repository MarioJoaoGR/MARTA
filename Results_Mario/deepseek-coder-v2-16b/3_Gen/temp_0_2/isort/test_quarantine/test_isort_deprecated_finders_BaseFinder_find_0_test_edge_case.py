
from isort.deprecated.finders import ModuleFinder
from config import Config
from base_finder import BaseFinder
import pytest

@pytest.fixture
def setup_base_finder():
    # Create a mock configuration for the test
    config = Config()
    return BaseFinder(config)

def test_init(setup_base_finder):
    finder = setup_base_finder
    assert isinstance(finder.config, Config)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_BaseFinder_find_0_test_edge_case
isort/Test4DT_tests/test_isort_deprecated_finders_BaseFinder_find_0_test_edge_case.py:2:0: E0611: No name 'ModuleFinder' in module 'isort.deprecated.finders' (no-name-in-module)
isort/Test4DT_tests/test_isort_deprecated_finders_BaseFinder_find_0_test_edge_case.py:3:0: E0401: Unable to import 'config' (import-error)
isort/Test4DT_tests/test_isort_deprecated_finders_BaseFinder_find_0_test_edge_case.py:4:0: E0401: Unable to import 'base_finder' (import-error)


"""