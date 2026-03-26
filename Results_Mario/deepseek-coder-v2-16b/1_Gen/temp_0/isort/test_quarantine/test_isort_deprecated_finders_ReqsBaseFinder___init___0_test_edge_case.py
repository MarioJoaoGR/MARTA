
import pytest
from isort.deprecated.finders import ReqsBaseFinder
from unittest.mock import MagicMock, patch

@pytest.fixture(autouse=True)
def mock_config():
    # Create a mock Config object
    config = MagicMock()
    config.enabled = True  # Assuming the finder should be enabled for this test
    return config

@patch('isort.deprecated.finders.ReqsBaseFinder._load_mapping')
@patch('isort.deprecated.finders.ReqsBaseFinder._load_names')
def test_init(mock_load_names, mock_load_mapping, mock_config):
    # Mock the return values of _load_names and _load_mapping methods
    mock_load_names.return_value = ['module1', 'module2']
    mock_load_mapping.return_value = {'file1': {}, 'file2': {}}

    finder = ReqsBaseFinder(config=mock_config, path=".")

    assert finder.enabled is True
    assert finder.path == "."
    assert finder.mapping == {'file1': {}, 'file2': {}}
    assert finder.names == ['module1', 'module2']

    # Check if the abstract methods were called during initialization
    mock_load_mapping.assert_called_once()
    mock_load_names.assert_called_once()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_ReqsBaseFinder___init___0_test_edge_case
isort/Test4DT_tests/test_isort_deprecated_finders_ReqsBaseFinder___init___0_test_edge_case.py:20:13: E0110: Abstract class 'ReqsBaseFinder' with abstract methods instantiated (abstract-class-instantiated)


"""