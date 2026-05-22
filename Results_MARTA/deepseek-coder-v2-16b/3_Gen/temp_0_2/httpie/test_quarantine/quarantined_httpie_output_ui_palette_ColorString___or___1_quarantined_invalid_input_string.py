
import pytest
from httpie.output.ui.palette import ColorString, GenericColor, _StyledGenericColor

def test_invalid_input_string():
    cs = ColorString(GenericColor.BLUE)
    with pytest.raises(TypeError):
        styled_cs = cs | "SOMETHING"

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_ui_palette_ColorString___or___1_test_invalid_input_string.py F [100%]

=================================== FAILURES ===================================
__________________________ test_invalid_input_string ___________________________

    def test_invalid_input_string():
        cs = ColorString(GenericColor.BLUE)
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_ui_palette_ColorString___or___1_test_invalid_input_string.py:7: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_ui_palette_ColorString___or___1_test_invalid_input_string.py::test_invalid_input_string
============================== 1 failed in 0.16s ===============================
"""