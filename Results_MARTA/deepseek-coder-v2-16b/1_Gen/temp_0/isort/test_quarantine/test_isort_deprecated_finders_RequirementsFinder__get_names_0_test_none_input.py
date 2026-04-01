
import pytest
from unittest.mock import patch, MagicMock
from isort.deprecated.finders import RequirementsFinder

def test_none_input():
    finder = RequirementsFinder()
    
    with pytest.raises(TypeError):
        finder._get_names(None)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_RequirementsFinder__get_names_0_test_none_input
isort/Test4DT_tests/test_isort_deprecated_finders_RequirementsFinder__get_names_0_test_none_input.py:7:13: E1120: No value for argument 'config' in constructor call (no-value-for-parameter)


"""