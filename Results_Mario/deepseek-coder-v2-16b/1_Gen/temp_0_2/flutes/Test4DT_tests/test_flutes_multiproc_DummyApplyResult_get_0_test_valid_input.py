
import pytest
from flutes.multiproc import DummyApplyResult  # Assuming the correct import path

@pytest.fixture
def dummy_result():
    return DummyApplyResult(42)  # Create a fixture with an initial value of 42

def test_get_without_timeout(dummy_result):
    assert dummy_result.get() == 42

def test_get_with_timeout(dummy_result):
    assert dummy_result.get(timeout=0.1) == 42
