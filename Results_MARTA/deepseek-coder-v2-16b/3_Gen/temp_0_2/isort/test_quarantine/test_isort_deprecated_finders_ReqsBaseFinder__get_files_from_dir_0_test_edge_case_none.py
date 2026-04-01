
import pytest
from isort.deprecated.finders import ReqsBaseFinder

# Mock Config class for testing purposes
class Config:
    pass

def test_edge_case_none():
    finder = ReqsBaseFinder(config=Config(), path=".")
    assert not finder.enabled  # Assuming enabled is False by default in the base class
    with pytest.raises(NotImplementedError):
        list(finder._get_files_from_dir("dummy_path"))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_ReqsBaseFinder__get_files_from_dir_0_test_edge_case_none
isort/Test4DT_tests/test_isort_deprecated_finders_ReqsBaseFinder__get_files_from_dir_0_test_edge_case_none.py:10:13: E0110: Abstract class 'ReqsBaseFinder' with abstract methods instantiated (abstract-class-instantiated)


"""