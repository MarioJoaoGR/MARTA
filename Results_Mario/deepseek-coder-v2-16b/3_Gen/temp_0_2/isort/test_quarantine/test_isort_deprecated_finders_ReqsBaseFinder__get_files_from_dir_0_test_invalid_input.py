
import pytest
from isort.deprecated.finders import ReqsBaseFinder

# Mocking the Config class as it's not defined in this context
class Config:
    pass

def test_invalid_input():
    with pytest.raises(NotImplementedError):
        finder = ReqsBaseFinder(config=Config(), path=".")
        list(finder._get_files_from_dir("invalid_path"))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_ReqsBaseFinder__get_files_from_dir_0_test_invalid_input
isort/Test4DT_tests/test_isort_deprecated_finders_ReqsBaseFinder__get_files_from_dir_0_test_invalid_input.py:11:17: E0110: Abstract class 'ReqsBaseFinder' with abstract methods instantiated (abstract-class-instantiated)


"""