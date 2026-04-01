
from isort.deprecated.finders import ReqsBaseFinder
import pytest
from unittest.mock import MagicMock

@pytest.fixture
def finder():
    config = MagicMock()
    return ReqsBaseFinder(config=config, path=".")

def test_valid_case(finder):
    # Since _get_names is an abstract method, we cannot directly instantiate the class without mocking it.
    with pytest.raises(NotImplementedError):
        list(finder._get_names("dummy_path"))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_ReqsBaseFinder__get_names_0_test_valid_case
isort/Test4DT_tests/test_isort_deprecated_finders_ReqsBaseFinder__get_names_0_test_valid_case.py:9:11: E0110: Abstract class 'ReqsBaseFinder' with abstract methods instantiated (abstract-class-instantiated)


"""