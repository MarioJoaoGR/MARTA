
from unittest.mock import patch
import httpie.output.ui.palette
from httpie.output.ui.palette import PieColor, COLOR_PALETTE

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

def test_valid_input():
    with patch('httpie.output.ui.palette.COLOR_PALETTE', {PieColor.RED: {'50': '#ff0000'}}):
        assert get_color(PieColor.RED, '50') == '#ff0000'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_output_ui_palette_get_color_0_test_valid_input
httpie/Test4DT_tests_codestral/test_httpie_output_ui_palette_get_color_0_test_valid_input.py:8:5: E0602: Undefined variable 'Optional' (undefined-variable)


"""