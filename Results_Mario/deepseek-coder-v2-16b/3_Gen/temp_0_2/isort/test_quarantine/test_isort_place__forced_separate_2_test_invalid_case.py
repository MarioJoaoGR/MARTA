
import pytest
from isort.place import Config
from fnmatch import fnmatch

def test_invalid_case():
    config = Config({'forced_separate': ['*.log', 'data.*']})
    result = _forced_separate('example.log', config)
    assert result == ('*.log', 'Matched forced_separate (*).log config value.')
    
    another_result = _forced_separate('structure/data.csv', config)
    assert another_result is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_place__forced_separate_2_test_invalid_case
isort/Test4DT_tests/test_isort_place__forced_separate_2_test_invalid_case.py:8:13: E0602: Undefined variable '_forced_separate' (undefined-variable)
isort/Test4DT_tests/test_isort_place__forced_separate_2_test_invalid_case.py:11:21: E0602: Undefined variable '_forced_separate' (undefined-variable)


"""