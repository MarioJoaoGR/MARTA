
import pytest
from isort.deprecated.finders import ForcedSeparateFinder

@pytest.fixture
def finder():
    return ForcedSeparateFinder()

def test_error_case(finder):
    with pytest.raises(TypeError) as excinfo:
        finder.find("some_module")
    assert "missing 1 required positional argument: 'config'" in str(excinfo.value)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_ForcedSeparateFinder_find_0_test_error_case
isort/Test4DT_tests/test_isort_deprecated_finders_ForcedSeparateFinder_find_0_test_error_case.py:7:11: E1120: No value for argument 'config' in constructor call (no-value-for-parameter)


"""