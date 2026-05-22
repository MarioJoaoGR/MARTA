
from httpie.output.ui.palette import COLOR_PALETTE, PieColor
from unittest.mock import patch
import pytest

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

def test_invalid_shade():
    with patch('httpie.output.ui.palette.COLOR_PALETTE', {'red': {'50': '#ff5733'}, 'blue': {'70': '#0000FF'}}):
        result = get_color(PieColor.RED, '90')
        assert result is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_output_ui_palette_get_color_0_test_invalid_shade
httpie/Test4DT_tests_codestral/test_httpie_output_ui_palette_get_color_0_test_invalid_shade.py:8:5: E0602: Undefined variable 'Optional' (undefined-variable)


"""