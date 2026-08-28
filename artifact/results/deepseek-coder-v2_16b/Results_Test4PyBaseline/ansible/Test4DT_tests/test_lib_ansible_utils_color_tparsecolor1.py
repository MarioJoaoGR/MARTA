
import pytest
from ansible.utils.color import parsecolor, C
import re

# Test cases for named colors
def test_parsecolor_named_colors():
    assert parsecolor('color256') == '38;5;256'

# Additional test cases to cover uncovered lines 58-70
@pytest.mark.parametrize("input_color, expected", [
    ('invalidcolor', None),
    ('color256', '38;5;256'),
    ('rgb345', f'38;5;{16 + 36 * int("3") + 6 * int("4") + int("5")}'),
    ('gray23', f'38;5;{232 + int("23")}')
])
def test_parsecolor_invalid_input(input_color, expected):
    if input_color == 'invalidcolor':
        with pytest.raises(KeyError):
            parsecolor(input_color)
    else:
        assert parsecolor(input_color) == expected
