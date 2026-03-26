
from isort.deprecated.finders import RequirementsFinder
import pytest
from unittest.mock import patch

@pytest.fixture
def finder():
    return RequirementsFinder()

def test_get_names(finder):
    with patch('isort.deprecated.finders.parse_requirements', return_value=['package1', 'package2']):
        names_iterator = finder._get_names('dummy_path')
        names = list(names_iterator)
        assert names == ['package1', 'package2']

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_RequirementsFinder__get_names_0_test_valid_input
isort/Test4DT_tests/test_isort_deprecated_finders_RequirementsFinder__get_names_0_test_valid_input.py:8:11: E1120: No value for argument 'config' in constructor call (no-value-for-parameter)


"""