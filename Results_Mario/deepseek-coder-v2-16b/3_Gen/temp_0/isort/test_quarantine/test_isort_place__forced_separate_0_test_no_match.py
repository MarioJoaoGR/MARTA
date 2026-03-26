
import pytest
from isort.place import Config
from fnmatch import fnmatch

def test_no_match():
    config = Config()
    config.forced_separate = ["*.log", "backup.*"]
    result = _forced_separate("example", config)
    assert result is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_place__forced_separate_0_test_no_match
isort/Test4DT_tests/test_isort_place__forced_separate_0_test_no_match.py:9:13: E0602: Undefined variable '_forced_separate' (undefined-variable)


"""