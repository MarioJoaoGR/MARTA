
import pytest
from isort.place import Config

@pytest.fixture
def config():
    config = Config()
    config.known_patterns = [("os.path", "placement1"), ("sys.modules", "placement2")]
    return config

def test__known_pattern_basic(config):
    result = _known_pattern("os.path", config)
    assert result == ('placement1', 'Matched configured known pattern os.path')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_place__known_pattern_0_test__known_pattern_basic
isort/Test4DT_tests/test_isort_place__known_pattern_0_test__known_pattern_basic.py:12:13: E0602: Undefined variable '_known_pattern' (undefined-variable)


"""