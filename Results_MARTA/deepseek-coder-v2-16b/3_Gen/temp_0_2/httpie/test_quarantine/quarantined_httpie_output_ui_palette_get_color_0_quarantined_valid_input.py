
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

# Test case with mocking
def test_valid_input():
    with patch('httpie.output.ui.palette.COLOR_PALETTE', {PieColor.RED: {'50': '#ff0000'}}):
        result = get_color(PieColor.RED, '50')
        assert result == '#ff0000'

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_ui_palette_get_color_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        with patch('httpie.output.ui.palette.COLOR_PALETTE', {PieColor.RED: {'50': '#ff0000'}}):
            result = get_color(PieColor.RED, '50')
>           assert result == '#ff0000'
E           AssertionError: assert '#FFE0DE' == '#ff0000'
E             
E             - #ff0000
E             + #FFE0DE

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_ui_palette_get_color_0_test_valid_input.py:21: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_ui_palette_get_color_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.08s ===============================
"""