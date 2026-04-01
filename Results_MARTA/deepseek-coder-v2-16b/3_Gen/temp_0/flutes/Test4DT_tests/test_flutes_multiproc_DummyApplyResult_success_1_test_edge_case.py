
# Assuming the module 'flutes.multiproc' has a class DummyApplyResult defined as follows:
from flutes.multiproc import DummyApplyResult

def dummy_apply_result(value):
    return DummyApplyResult(value)

import pytest

@pytest.mark.parametrize("test_input, expected", [
    (42, True),
    ("Success", True),
])
def test_dummy_apply_result_success(test_input, expected):
    result = dummy_apply_result(test_input)
    assert result.success() == expected
