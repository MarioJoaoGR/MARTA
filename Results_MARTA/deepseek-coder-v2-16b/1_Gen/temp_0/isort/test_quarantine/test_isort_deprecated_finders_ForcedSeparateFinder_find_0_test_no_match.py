
import pytest
from isort.deprecated.finders import ForcedSeparateFinder

@pytest.fixture
def setup_finder():
    return ForcedSeparateFinder()

def test_no_match(setup_finder):
    finder = setup_finder
    result = finder.find("some_module")
    assert result is None

def test_match_first_pattern(setup_finder):
    finder = setup_finder
    result = finder.find("mod1_test_module")  # This should match "mod1*"
    assert result == "mod1*"

def test_match_second_pattern(setup_finder):
    finder = setup_finder
    result = finder.find("mod2_test_module")  # This should match "mod2*"
    assert result == "mod2*"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_ForcedSeparateFinder_find_0_test_no_match
isort/Test4DT_tests/test_isort_deprecated_finders_ForcedSeparateFinder_find_0_test_no_match.py:7:11: E1120: No value for argument 'config' in constructor call (no-value-for-parameter)


"""