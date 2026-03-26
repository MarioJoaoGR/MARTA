
import pytest
from pytutils.excs import ok

def test_edge_case_none():
    with pytest.raises(TypeError) as exc_info:
        with ok():
            raise TypeError("Test exception")
    assert str(exc_info.value) == "Test exception"
