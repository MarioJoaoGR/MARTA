
import pytest
from isort.place import Config
from fnmatch import fnmatch

@pytest.fixture
def config():
    cfg = Config()
    cfg.forced_separate = ["*.log", "backup.*"]
    return cfg

def test_valid_input(config):
    result = _forced_separate("example.log", config)
    assert result == ('*.log', 'Matched forced_separate (*).log config value.')

def test_no_match(config):
    result = _forced_separate("example", config)
    assert result is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_place__forced_separate_0_test_valid_input
isort/Test4DT_tests/test_isort_place__forced_separate_0_test_valid_input.py:13:13: E0602: Undefined variable '_forced_separate' (undefined-variable)
isort/Test4DT_tests/test_isort_place__forced_separate_0_test_valid_input.py:17:13: E0602: Undefined variable '_forced_separate' (undefined-variable)


"""