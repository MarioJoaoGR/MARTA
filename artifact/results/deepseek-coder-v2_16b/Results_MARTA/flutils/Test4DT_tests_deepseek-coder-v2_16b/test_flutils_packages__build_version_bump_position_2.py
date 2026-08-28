
import pytest
from flutils.packages import _build_version_bump_position

def test_valid_position():
    assert _build_version_bump_position(0) == 0


def test_out_of_range_position():
    with pytest.raises(ValueError):
        _build_version_bump_position(5)