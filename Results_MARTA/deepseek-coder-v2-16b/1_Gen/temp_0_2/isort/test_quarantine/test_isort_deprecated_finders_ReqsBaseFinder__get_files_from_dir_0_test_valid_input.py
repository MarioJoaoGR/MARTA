
from isort.deprecated.finders import ReqsBaseFinder
import pytest
from unittest.mock import patch
from config import Config  # Assuming Config is defined in a module named 'config'

@pytest.fixture
def setup_finder():
    return ReqsBaseFinder(config=Config(), path=".")

def test_init(setup_finder):
    finder = setup_finder
    assert not finder.enabled
    assert finder.path == "."
    assert isinstance(finder.config, Config)
    assert finder.mapping == {}
    assert finder.names == []

@patch('isort.deprecated.finders.ReqsBaseFinder._load_mapping')
@patch('isort.deprecated.finders.ReqsBaseFinder._load_names')
def test_init_with_enabled(mock_load_names, mock_load_mapping, setup_finder):
    finder = ReqsBaseFinder(config=Config(), path=".")
    assert not finder.enabled
    assert finder.path == "."
    assert isinstance(finder.config, Config)
    assert finder.mapping == {}
    assert finder.names == []

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_ReqsBaseFinder__get_files_from_dir_0_test_valid_input
isort/Test4DT_tests/test_isort_deprecated_finders_ReqsBaseFinder__get_files_from_dir_0_test_valid_input.py:5:0: E0401: Unable to import 'config' (import-error)
isort/Test4DT_tests/test_isort_deprecated_finders_ReqsBaseFinder__get_files_from_dir_0_test_valid_input.py:9:11: E0110: Abstract class 'ReqsBaseFinder' with abstract methods instantiated (abstract-class-instantiated)
isort/Test4DT_tests/test_isort_deprecated_finders_ReqsBaseFinder__get_files_from_dir_0_test_valid_input.py:22:13: E0110: Abstract class 'ReqsBaseFinder' with abstract methods instantiated (abstract-class-instantiated)


"""