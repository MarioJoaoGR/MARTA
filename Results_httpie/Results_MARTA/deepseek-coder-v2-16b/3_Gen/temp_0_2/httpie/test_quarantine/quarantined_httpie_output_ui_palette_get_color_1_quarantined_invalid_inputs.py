
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

# Test case for invalid inputs
@patch('httpie.output.ui.palette.COLOR_PALETTE', {'red': {'50': '#ff0000'}})
def test_invalid_inputs(self):
    # Test case for invalid color input
    self.assertIsNone(get_color(PieColor.GREEN, '50'))  # GREEN is not in COLOR_PALETTE

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_ui_palette_get_color_1_test_invalid_inputs.py E [100%]

==================================== ERRORS ====================================
____________________ ERROR at setup of test_invalid_inputs _____________________
file /projects/F202407648IACDCF2/mario/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_ui_palette_get_color_1_test_invalid_inputs.py, line 18
  @patch('httpie.output.ui.palette.COLOR_PALETTE', {'red': {'50': '#ff0000'}})
  def test_invalid_inputs(self):
E       fixture 'self' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/projects/F202407648IACDCF2/mario/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_ui_palette_get_color_1_test_invalid_inputs.py:18
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_ui_palette_get_color_1_test_invalid_inputs.py::test_invalid_inputs
=============================== 1 error in 0.15s ===============================
"""