
from isort.deprecated.finders import ReqsBaseFinder
from config import Config
import pytest

# Test to ensure that the _get_files method is not implemented in the base class
def test_ReqsBaseFinder_abstract_methods():
    with pytest.raises(NotImplementedError):
        finder = ReqsBaseFinder(config=Config(), path=".")
        list(finder._get_files())

# Test to ensure that the _get_names method is not implemented in the base class
def test_ReqsBaseFinder_abstract_methods_2():
    with pytest.raises(NotImplementedError):
        finder = ReqsBaseFinder(config=Config(), path=".")
        list(finder._get_names("dummy_path"))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_ReqsBaseFinder__load_names_0_test_valid_case
isort/Test4DT_tests/test_isort_deprecated_finders_ReqsBaseFinder__load_names_0_test_valid_case.py:3:0: E0401: Unable to import 'config' (import-error)
isort/Test4DT_tests/test_isort_deprecated_finders_ReqsBaseFinder__load_names_0_test_valid_case.py:9:17: E0110: Abstract class 'ReqsBaseFinder' with abstract methods instantiated (abstract-class-instantiated)
isort/Test4DT_tests/test_isort_deprecated_finders_ReqsBaseFinder__load_names_0_test_valid_case.py:15:17: E0110: Abstract class 'ReqsBaseFinder' with abstract methods instantiated (abstract-class-instantiated)


"""