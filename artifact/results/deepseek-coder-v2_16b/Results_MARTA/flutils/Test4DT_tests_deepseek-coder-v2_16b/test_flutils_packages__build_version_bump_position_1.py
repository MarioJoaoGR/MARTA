
import pytest
from flutils.packages import _build_version_bump_position

def test_valid_position():
    position = 0
    result = _build_version_bump_position(position)
    assert result == position, f"Expected {position} for valid position {position}, but got {result}"


def test_out_of_range_position():
    with pytest.raises(ValueError):
        position = 5
        _build_version_bump_position(position)