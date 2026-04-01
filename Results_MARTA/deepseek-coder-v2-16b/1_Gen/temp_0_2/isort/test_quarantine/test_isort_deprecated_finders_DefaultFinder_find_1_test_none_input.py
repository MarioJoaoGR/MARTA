
from isort.deprecated.finders import DefaultFinder
import pytest

@pytest.fixture
def default_finder():
    return DefaultFinder()

def test_none_input(default_finder):
    with pytest.raises(TypeError) as excinfo:
        default_finder.find(None)
    assert "missing 1 required positional argument: 'module_name'" in str(excinfo.value)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_DefaultFinder_find_1_test_none_input
isort/Test4DT_tests/test_isort_deprecated_finders_DefaultFinder_find_1_test_none_input.py:7:11: E1120: No value for argument 'config' in constructor call (no-value-for-parameter)


"""