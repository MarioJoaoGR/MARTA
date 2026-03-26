
import pytest
from flutes.multiproc import DummyApplyResult

@pytest.fixture
def dummy_apply_result():
    return DummyApplyResult(value=42)

def test_dummy_apply_result(dummy_apply_result):
    assert dummy_apply_result._value == 42
    assert dummy_apply_result.ready() is True
