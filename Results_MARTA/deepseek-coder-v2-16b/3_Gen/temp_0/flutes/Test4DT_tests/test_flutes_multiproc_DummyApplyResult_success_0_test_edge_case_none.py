
import pytest
from flutes.multiproc import DummyApplyResult

def dummy_apply_result(value):
    return DummyApplyResult(value)

@pytest.mark.parametrize("test_input, expected", [
    (None, True),  # Test edge case where value is None
])
def test_edge_case_none(test_input, expected):
    result = dummy_apply_result(test_input)
    assert result._value == test_input
