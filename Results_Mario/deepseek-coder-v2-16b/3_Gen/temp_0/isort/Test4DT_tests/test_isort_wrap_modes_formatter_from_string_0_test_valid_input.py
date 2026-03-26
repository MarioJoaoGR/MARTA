
import pytest

from isort.wrap_modes import formatter_from_string


# Mocking the grid function since it's not defined in this scope
def test_valid_input():
    assert callable(formatter_from_string('GRID'))
    assert callable(formatter_from_string('TABLE'))
    assert callable(formatter_from_string('INVALID')) is True
