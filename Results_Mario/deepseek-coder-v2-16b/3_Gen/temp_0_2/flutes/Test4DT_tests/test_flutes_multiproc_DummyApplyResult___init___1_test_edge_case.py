
from flutes.multiproc import DummyApplyResult

def test_edge_case():
    value = "test_value"
    dummy_apply_result = DummyApplyResult(value)
    assert dummy_apply_result._value == value
