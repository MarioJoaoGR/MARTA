
import pytest
from ansible.utils.color import parsecolor

# Constants for testing
COLOR_CODES = {
    'color256': '38;5;256',
    'rgb246397': '38;5;190',
    'gray23': '38;5;23'
}

# Mocking the COLOR_CODES for testing
class C:
    COLOR_CODES = {
        'color256': '38;5;256',
        'rgb246397': '38;5;190',
        'gray23': '38;5;23'
    }

# Test valid named color input
def test_valid_color256():
    color = 'color256'
    assert parsecolor(color) == COLOR_CODES[color]

# Test valid RGB color input
def test_valid_rgb():
    color = 'rgb246397'
    expected_value = 16 + 36 * 24 + 6 * 6 + 39
    assert parsecolor(color) == f'38;5;{expected_value}'

# Test valid grayscale color input
def test_valid_gray():
    color = 'gray23'
    expected_value = 232 + 23
    assert parsecolor(color) == f'38;5;{expected_value}'

# Test invalid color input that raises ValueError
def test_invalid_color():
    color = 'unknown_color'
    with pytest.raises(ValueError):
        parsecolor(color)
