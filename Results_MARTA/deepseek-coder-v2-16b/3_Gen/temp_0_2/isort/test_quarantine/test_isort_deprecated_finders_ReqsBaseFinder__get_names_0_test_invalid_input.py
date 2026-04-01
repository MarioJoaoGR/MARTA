
from isort.deprecated.finders import ReqsBaseFinder
import pytest
from config import Config

@pytest.fixture
def base_finder():
    return ReqsBaseFinder(config=Config(), path=".")

def test_invalid_input(base_finder):
    with pytest.raises(NotImplementedError):
        base_finder._get_names("some_directory")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_ReqsBaseFinder__get_names_0_test_invalid_input
isort/Test4DT_tests/test_isort_deprecated_finders_ReqsBaseFinder__get_names_0_test_invalid_input.py:4:0: E0401: Unable to import 'config' (import-error)
isort/Test4DT_tests/test_isort_deprecated_finders_ReqsBaseFinder__get_names_0_test_invalid_input.py:8:11: E0110: Abstract class 'ReqsBaseFinder' with abstract methods instantiated (abstract-class-instantiated)


"""