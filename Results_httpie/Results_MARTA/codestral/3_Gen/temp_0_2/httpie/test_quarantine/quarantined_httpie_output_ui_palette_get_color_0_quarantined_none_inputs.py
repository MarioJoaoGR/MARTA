
import unittest
from unittest.mock import patch
from httpie.output.ui.palette import COLOR_PALETTE, PieColor
from typing import Optional

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

class TestGetColor(unittest.TestCase):
    
    @patch('httpie.output.ui.palette.COLOR_PALETTE', {PieColor.RED: {'50': '#ff0000'}})
    def test_none_inputs(self):
        # Test when color is not in palette
        result = get_color(PieColor.BLUE, '70')
        self.assertIsNone(result)
        
        # Test when shade is not in the dictionary of the specified color
        result = get_color(PieColor.RED, '60')
        self.assertEqual(result, '#ff0000')  # Assuming '60' should be a valid shade of red in COLOR_PALETTE
        
        # Test when both color and shade are correct
        result = get_color(PieColor.RED, '50')
        self.assertEqual(result, '#ff0000')
        
        # Test with custom palette
        custom_palette = {PieColor.BLUE: {'70': '#0000FF'}}
        result = get_color(PieColor.BLUE, '70', palette=custom_palette)
        self.assertEqual(result, '#0000FF')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

httpie/Test4DT_tests_codestral/test_httpie_output_ui_palette_get_color_0_test_none_inputs.py F [100%]

=================================== FAILURES ===================================
________________________ TestGetColor.test_none_inputs _________________________

self = <Test4DT_tests_codestral.test_httpie_output_ui_palette_get_color_0_test_none_inputs.TestGetColor testMethod=test_none_inputs>

    @patch('httpie.output.ui.palette.COLOR_PALETTE', {PieColor.RED: {'50': '#ff0000'}})
    def test_none_inputs(self):
        # Test when color is not in palette
        result = get_color(PieColor.BLUE, '70')
>       self.assertIsNone(result)
E       AssertionError: {'50': '#DBE3FA', '100': '#BFCFF5', '200': '#A1B8F2', '300': '#85A3ED', '400': '#698FEB', '500': '#4B78E6', '600': '#426BD1', '700': '#3B5EBA', '800': '#3354A6', '900': '#2B478F', 'DEFAULT': '#4B78E6'} is not None

httpie/Test4DT_tests_codestral/test_httpie_output_ui_palette_get_color_0_test_none_inputs.py:24: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_output_ui_palette_get_color_0_test_none_inputs.py::TestGetColor::test_none_inputs
============================== 1 failed in 0.16s ===============================
"""