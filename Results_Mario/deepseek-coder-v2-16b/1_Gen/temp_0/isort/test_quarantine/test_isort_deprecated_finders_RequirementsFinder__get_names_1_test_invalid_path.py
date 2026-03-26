
from isort.deprecated.finders import RequirementsFinder
import pytest
from unittest.mock import patch, MagicMock

@pytest.fixture
def finder():
    return RequirementsFinder()

@patch('isort.deprecated.finders.parse_requirements')
def test_get_names_invalid_path(mock_parse_requirements, finder):
    mock_parse_requirements.return_value = MagicMock()
    
    with pytest.raises(FileNotFoundError):
        names_iterator = finder._get_names('invalid/path')
        for name in names_iterator:
            print(name)  # This will not be reached due to the expected error

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_RequirementsFinder__get_names_1_test_invalid_path
isort/Test4DT_tests/test_isort_deprecated_finders_RequirementsFinder__get_names_1_test_invalid_path.py:8:11: E1120: No value for argument 'config' in constructor call (no-value-for-parameter)


"""