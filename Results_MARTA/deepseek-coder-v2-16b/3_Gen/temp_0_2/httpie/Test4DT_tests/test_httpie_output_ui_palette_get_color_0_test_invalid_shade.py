
from httpie.output.ui.palette import COLOR_PALETTE
from unittest.mock import patch
from typing import Optional
from enum import Enum  # Assuming PieColor is an Enum

class PieColor(Enum):
    RED = 'red'
    BLUE = 'blue'
    # Define other colors as needed

def get_color(
    color: PieColor, shade: str, *, palette=COLOR_PALETTE
) -> Optional[str]:
    if color not in palette:
        return None
    color_code = palette[color]
    if isinstance(color_code, dict) and shade in color_code:
        return color_code[shade]
    else:
        return color_code

# Test case to fix the error
def test_invalid_shade():
    with patch('httpie.output.ui.palette.COLOR_PALETTE', {'red': {'50': '#ff0000'}}):
        result = get_color(PieColor.RED, '90')
        assert result is None
