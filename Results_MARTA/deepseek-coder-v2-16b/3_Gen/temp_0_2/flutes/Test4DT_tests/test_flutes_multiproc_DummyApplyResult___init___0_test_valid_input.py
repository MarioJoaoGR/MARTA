
from flutes.multiproc import DummyApplyResult
import pytest

@pytest.fixture(name="dummy")
def fixture_dummy():
    return DummyApplyResult("initial value")

def test_valid_input(dummy):
    assert dummy._value == "initial value"
