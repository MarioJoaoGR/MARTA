
import unittest
from unittest.mock import patch
from httpie.output.ui.palette import PieColor, COLOR_PALETTE
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

class TestHttpieOutputUiPaletteGetColor0TestInvalidShade(unittest.TestCase):
    
    @patch('httpie.output.ui.palette.COLOR_PALETTE', {'red': {'50': '#ff0000'}})
    def test_invalid_shade(self):
        # Test when the color is not in the palette
        result = get_color(PieColor.RED, '90')
        self.assertIsNone(result)
        
        # Test when the shade does not exist for the given color
        result = get_color(PieColor.BLUE, '50')
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
collected 1 item

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_ui_palette_get_color_0_test_invalid_shade.py F [100%]

=================================== FAILURES ===================================
____ TestHttpieOutputUiPaletteGetColor0TestInvalidShade.test_invalid_shade _____

self = <test_httpie_output_ui_palette_get_color_0_test_invalid_shade.TestHttpieOutputUiPaletteGetColor0TestInvalidShade testMethod=test_invalid_shade>

    @patch('httpie.output.ui.palette.COLOR_PALETTE', {'red': {'50': '#ff0000'}})
    def test_invalid_shade(self):
        # Test when the color is not in the palette
        result = get_color(PieColor.RED, '90')
>       self.assertIsNone(result)
E       AssertionError: {'50': '#FFE0DE', '100': '#FFC7C4', '200': '#FFB0AB', '300': '#FF968F', '400': '#FF8075', '500': '#FF665B', '600': '#E34F45', '700': '#C7382E', '800': '#AD2117', '900': '#910A00', 'DEFAULT': '#FF665B'} is not None

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_ui_palette_get_color_0_test_invalid_shade.py:24: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_ui_palette_get_color_0_test_invalid_shade.py::TestHttpieOutputUiPaletteGetColor0TestInvalidShade::test_invalid_shade
============================== 1 failed in 0.10s ===============================
"""