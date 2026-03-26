
from isort.deprecated.finders import RequirementsFinder
import pytest
from unittest.mock import patch

def test_get_names_invalid_input():
    finder = RequirementsFinder()
    
    with pytest.raises(TypeError):
        list(finder._get_names("invalid_path"))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_RequirementsFinder__get_names_0_test_invalid_input
isort/Test4DT_tests/test_isort_deprecated_finders_RequirementsFinder__get_names_0_test_invalid_input.py:7:13: E1120: No value for argument 'config' in constructor call (no-value-for-parameter)


"""