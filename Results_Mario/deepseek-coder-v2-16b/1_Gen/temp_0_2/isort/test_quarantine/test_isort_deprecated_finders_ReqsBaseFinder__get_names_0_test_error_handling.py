
import pytest
from unittest.mock import MagicMock, patch
from isort.deprecated.finders import ReqsBaseFinder
from config import Config

@pytest.fixture
def finder():
    return ReqsBaseFinder(config=Config(), path=".")

def test_error_handling(finder):
    with pytest.raises(NotImplementedError):
        list(finder._get_names("dummy/path"))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_ReqsBaseFinder__get_names_0_test_error_handling
isort/Test4DT_tests/test_isort_deprecated_finders_ReqsBaseFinder__get_names_0_test_error_handling.py:5:0: E0401: Unable to import 'config' (import-error)
isort/Test4DT_tests/test_isort_deprecated_finders_ReqsBaseFinder__get_names_0_test_error_handling.py:9:11: E0110: Abstract class 'ReqsBaseFinder' with abstract methods instantiated (abstract-class-instantiated)


"""