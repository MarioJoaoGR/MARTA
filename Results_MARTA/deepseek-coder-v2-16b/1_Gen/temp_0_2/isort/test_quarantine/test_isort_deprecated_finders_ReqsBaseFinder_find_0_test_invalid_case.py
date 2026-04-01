
import pytest
from isort.deprecated.finders import ReqsBaseFinder
from config import Config

@pytest.fixture
def setup_finder():
    return ReqsBaseFinder(config=Config(), path=".")

def test_invalid_case(setup_finder):
    finder = setup_finder
    assert finder.find('requests') == sections.THIRDPARTY

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_ReqsBaseFinder_find_0_test_invalid_case
isort/Test4DT_tests/test_isort_deprecated_finders_ReqsBaseFinder_find_0_test_invalid_case.py:4:0: E0401: Unable to import 'config' (import-error)
isort/Test4DT_tests/test_isort_deprecated_finders_ReqsBaseFinder_find_0_test_invalid_case.py:8:11: E0110: Abstract class 'ReqsBaseFinder' with abstract methods instantiated (abstract-class-instantiated)
isort/Test4DT_tests/test_isort_deprecated_finders_ReqsBaseFinder_find_0_test_invalid_case.py:12:38: E0602: Undefined variable 'sections' (undefined-variable)


"""