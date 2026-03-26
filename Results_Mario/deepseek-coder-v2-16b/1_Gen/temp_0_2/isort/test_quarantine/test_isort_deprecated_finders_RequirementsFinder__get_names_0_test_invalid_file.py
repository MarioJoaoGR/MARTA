
import pytest
from isort.deprecated.finders import RequirementsFinder

@pytest.fixture
def requirements_finder():
    return RequirementsFinder()

def test_invalid_file(requirements_finder):
    with pytest.raises(TypeError) as excinfo:
        requirements_finder._get_names("invalid/path")
    assert "missing 1 required positional argument" in str(excinfo.value)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_RequirementsFinder__get_names_0_test_invalid_file
isort/Test4DT_tests/test_isort_deprecated_finders_RequirementsFinder__get_names_0_test_invalid_file.py:7:11: E1120: No value for argument 'config' in constructor call (no-value-for-parameter)


"""