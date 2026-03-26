
from flutes.multiproc import DummyApplyResult
import pytest

@pytest.fixture
def dummy_apply_result():
    return DummyApplyResult(value=42)

def test_dummy_apply_result_success(dummy_apply_result):
    assert dummy_apply_result.success() is True
