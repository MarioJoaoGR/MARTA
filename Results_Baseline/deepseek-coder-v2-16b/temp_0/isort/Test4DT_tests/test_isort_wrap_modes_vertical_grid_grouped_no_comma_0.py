# Module: isort.wrap_modes
# test_isort_wrap_modes.py
import pytest

from isort.wrap_modes import vertical_grid_grouped_no_comma


def test_vertical_grid_grouped_no_comma_raises_not_implemented_error():
    with pytest.raises(NotImplementedError):
        vertical_grid_grouped_no_comma()

def test_vertical_grid_grouped_no_comma_incorrect_usage():
    with pytest.raises(NotImplementedError):
        vertical_grid_grouped_no_comma(param1="value1", param2="value2")
