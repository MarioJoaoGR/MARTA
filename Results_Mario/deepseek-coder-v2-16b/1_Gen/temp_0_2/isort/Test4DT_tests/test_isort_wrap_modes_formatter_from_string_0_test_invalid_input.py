
import pytest
from isort.wrap_modes import formatter_from_string, grid

def test_invalid_input():
    # Test when an invalid mode is provided
    assert callable(formatter_from_string('INVALID'))
    # Ensure the default 'grid' formatter is returned for an unknown mode
    assert formatter_from_string('INVALID') == grid
