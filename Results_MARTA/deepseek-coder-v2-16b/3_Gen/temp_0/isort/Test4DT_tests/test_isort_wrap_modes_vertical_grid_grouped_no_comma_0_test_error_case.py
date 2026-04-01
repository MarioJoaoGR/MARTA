
import pytest

from isort.wrap_modes import vertical_grid_grouped_no_comma


def test_vertical_grid_grouped_no_comma():
    with pytest.raises(NotImplementedError):
        result = vertical_grid_grouped_no_comma()
