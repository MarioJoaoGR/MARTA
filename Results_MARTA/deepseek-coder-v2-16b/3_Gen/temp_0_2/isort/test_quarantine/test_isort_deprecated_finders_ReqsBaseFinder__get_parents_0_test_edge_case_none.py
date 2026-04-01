
from isort.deprecated.finders import ReqsBaseFinder
import os
import pytest

@pytest.fixture
def base_finder():
    return ReqsBaseFinder(config=None, path=".")

def test_get_parents_edge_case_none(base_finder):
    # Test that _get_parents returns an iterator when given a non-existent path
    with pytest.raises(StopIteration):
        list(_get_parents("non_existent_path"))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_ReqsBaseFinder__get_parents_0_test_edge_case_none
isort/Test4DT_tests/test_isort_deprecated_finders_ReqsBaseFinder__get_parents_0_test_edge_case_none.py:8:11: E0110: Abstract class 'ReqsBaseFinder' with abstract methods instantiated (abstract-class-instantiated)
isort/Test4DT_tests/test_isort_deprecated_finders_ReqsBaseFinder__get_parents_0_test_edge_case_none.py:13:13: E0602: Undefined variable '_get_parents' (undefined-variable)


"""