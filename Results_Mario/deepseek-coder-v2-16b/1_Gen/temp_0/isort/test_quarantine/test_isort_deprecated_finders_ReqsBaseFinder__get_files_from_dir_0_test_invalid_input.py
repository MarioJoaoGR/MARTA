
import pytest
from isort.deprecated.finders import ReqsBaseFinder
from unittest.mock import MagicMock

def test_invalid_input():
    config = MagicMock()
    finder = ReqsBaseFinder(config=config, path="invalid/path")
    
    with pytest.raises(NotImplementedError):
        list(finder._get_files_from_dir("invalid/path"))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_ReqsBaseFinder__get_files_from_dir_0_test_invalid_input
isort/Test4DT_tests/test_isort_deprecated_finders_ReqsBaseFinder__get_files_from_dir_0_test_invalid_input.py:8:13: E0110: Abstract class 'ReqsBaseFinder' with abstract methods instantiated (abstract-class-instantiated)


"""