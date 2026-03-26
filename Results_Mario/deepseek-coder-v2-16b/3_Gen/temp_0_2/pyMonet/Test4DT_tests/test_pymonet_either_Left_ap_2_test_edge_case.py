
import pytest
from pymonet.either import Left

def test_left_ap():
    left = Left(None)
    result = left.ap(Left(None))
    assert isinstance(result, Left)
    assert result.value is None
