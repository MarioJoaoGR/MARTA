
from flutes.multiproc import DummyApplyResult

def test_valid_input():
    value = 42
    result = DummyApplyResult(value)
    assert result._value == value
