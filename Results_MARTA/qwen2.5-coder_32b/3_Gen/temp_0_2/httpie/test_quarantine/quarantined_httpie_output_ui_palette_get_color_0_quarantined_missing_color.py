
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
    def test_get_color_valid_shade(self):
        result = get_color(PieColor.RED, '50')
        self.assertEqual(result, '#ff0000')
    
    @patch('httpie.output.ui.palette.COLOR_PALETTE', {PieColor.BLUE: {'70': '#0000FF'}})
    def test_get_color_valid_shade_custom_palette(self):
        result = get_color(PieColor.BLUE, '70')
        self.assertEqual(result, '#0000FF')
    
    @patch('httpie.output.ui.palette.COLOR_PALETTE', {PieColor.GREEN: {'30': '#008000'}})
    def test_get_color_invalid_shade(self):
        result = get_color(PieColor.GREEN, '20')
        self.assertIsNone(result)
    
    @patch('httpie.output.ui.palette.COLOR_PALETTE', {})
    def test_get_color_missing_color(self):
        result = get_color(PieColor.RED, '50')
        self.assertIsNone(result)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 4 items

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_ui_palette_get_color_0_test_missing_color.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
__________________ TestGetColor.test_get_color_invalid_shade ___________________

self = <test_httpie_output_ui_palette_get_color_0_test_missing_color.TestGetColor testMethod=test_get_color_invalid_shade>

    @patch('httpie.output.ui.palette.COLOR_PALETTE', {PieColor.GREEN: {'30': '#008000'}})
    def test_get_color_invalid_shade(self):
        result = get_color(PieColor.GREEN, '20')
>       self.assertIsNone(result)
E       AssertionError: {'50': '#E3F7E8', '100': '#CCF2D6', '200': '#B5EDC4', '300': '#A1E8B0', '400': '#8AE09E', '500': '#73DC8C', '600': '#63C27A', '700': '#52AB66', '800': '#429154', '900': '#307842', 'DEFAULT': '#73DC8C'} is not None

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_ui_palette_get_color_0_test_missing_color.py:33: AssertionError
__________________ TestGetColor.test_get_color_missing_color ___________________

self = <test_httpie_output_ui_palette_get_color_0_test_missing_color.TestGetColor testMethod=test_get_color_missing_color>

    @patch('httpie.output.ui.palette.COLOR_PALETTE', {})
    def test_get_color_missing_color(self):
        result = get_color(PieColor.RED, '50')
>       self.assertIsNone(result)
E       AssertionError: '#FFE0DE' is not None

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_ui_palette_get_color_0_test_missing_color.py:38: AssertionError
___________________ TestGetColor.test_get_color_valid_shade ____________________

self = <test_httpie_output_ui_palette_get_color_0_test_missing_color.TestGetColor testMethod=test_get_color_valid_shade>

    @patch('httpie.output.ui.palette.COLOR_PALETTE', {PieColor.RED: {'50': '#ff0000'}})
    def test_get_color_valid_shade(self):
        result = get_color(PieColor.RED, '50')
>       self.assertEqual(result, '#ff0000')
E       AssertionError: '#FFE0DE' != '#ff0000'
E       - #FFE0DE
E       + #ff0000

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_ui_palette_get_color_0_test_missing_color.py:23: AssertionError
____________ TestGetColor.test_get_color_valid_shade_custom_palette ____________

self = <test_httpie_output_ui_palette_get_color_0_test_missing_color.TestGetColor testMethod=test_get_color_valid_shade_custom_palette>

    @patch('httpie.output.ui.palette.COLOR_PALETTE', {PieColor.BLUE: {'70': '#0000FF'}})
    def test_get_color_valid_shade_custom_palette(self):
        result = get_color(PieColor.BLUE, '70')
>       self.assertEqual(result, '#0000FF')
E       AssertionError: {'50': '#DBE3FA', '100': '#BFCFF5', '200'[155 chars]8E6'} != '#0000FF'

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_ui_palette_get_color_0_test_missing_color.py:28: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_ui_palette_get_color_0_test_missing_color.py::TestGetColor::test_get_color_invalid_shade
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_ui_palette_get_color_0_test_missing_color.py::TestGetColor::test_get_color_missing_color
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_ui_palette_get_color_0_test_missing_color.py::TestGetColor::test_get_color_valid_shade
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_ui_palette_get_color_0_test_missing_color.py::TestGetColor::test_get_color_valid_shade_custom_palette
============================== 4 failed in 0.09s ===============================
"""