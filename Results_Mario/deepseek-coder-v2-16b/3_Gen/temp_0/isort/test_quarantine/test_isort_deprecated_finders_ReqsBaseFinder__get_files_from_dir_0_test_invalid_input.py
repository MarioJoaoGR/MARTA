
import pytest
from isort.deprecated.finders import ReqsBaseFinder
from isort.config import Config  # Importing from isort.config as per pylint error suggestion

def test_invalid_input():
    with pytest.raises(NotImplementedError):
        config = Config()
        finder = ReqsBaseFinder(config=config, path=".")
        next(finder._get_files_from_dir("invalid_path"))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_ReqsBaseFinder__get_files_from_dir_0_test_invalid_input
isort/Test4DT_tests/test_isort_deprecated_finders_ReqsBaseFinder__get_files_from_dir_0_test_invalid_input.py:4:0: E0401: Unable to import 'isort.config' (import-error)
isort/Test4DT_tests/test_isort_deprecated_finders_ReqsBaseFinder__get_files_from_dir_0_test_invalid_input.py:4:0: E0611: No name 'config' in module 'isort' (no-name-in-module)
isort/Test4DT_tests/test_isort_deprecated_finders_ReqsBaseFinder__get_files_from_dir_0_test_invalid_input.py:9:17: E0110: Abstract class 'ReqsBaseFinder' with abstract methods instantiated (abstract-class-instantiated)


"""