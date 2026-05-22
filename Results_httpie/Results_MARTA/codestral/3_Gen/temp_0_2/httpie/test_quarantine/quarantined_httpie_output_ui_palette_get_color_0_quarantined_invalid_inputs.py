
from unittest.mock import patch
import pytest
from httpie.output.ui.palette import COLOR_PALETTE, PieColor
from httpie.output.ui.palette import get_color

def test_invalid_inputs():
    with patch('httpie.output.ui.palette.COLOR_PALETTE', {}):
        assert get_color(PieColor.RED, '50') is None

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

httpie/Test4DT_tests_codestral/test_httpie_output_ui_palette_get_color_0_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        with patch('httpie.output.ui.palette.COLOR_PALETTE', {}):
>           assert get_color(PieColor.RED, '50') is None
E           AssertionError: assert '#FFE0DE' is None
E            +  where '#FFE0DE' = get_color(<PieColor.RED: 'red'>, '50')
E            +    where <PieColor.RED: 'red'> = PieColor.RED

httpie/Test4DT_tests_codestral/test_httpie_output_ui_palette_get_color_0_test_invalid_inputs.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_output_ui_palette_get_color_0_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.15s ===============================
"""