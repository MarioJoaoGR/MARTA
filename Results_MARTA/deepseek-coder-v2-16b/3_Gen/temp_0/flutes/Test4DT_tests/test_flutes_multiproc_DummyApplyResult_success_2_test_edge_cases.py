
import pytest
from flutes.multiproc import DummyApplyResult

@pytest.mark.parametrize("value", [42, "Hello, World!"])
def test_edge_cases(value):
    result = DummyApplyResult(value)
    assert result.success() is True
