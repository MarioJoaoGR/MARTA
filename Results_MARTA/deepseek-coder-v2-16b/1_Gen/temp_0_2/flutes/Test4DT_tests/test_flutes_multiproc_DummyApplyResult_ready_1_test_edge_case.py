
import pytest
from flutes.multiproc import DummyApplyResult

@pytest.fixture
def dummy_apply_result():
    return DummyApplyResult(42)

def test_edge_case(dummy_apply_result):
    assert dummy_apply_result.ready() is True
