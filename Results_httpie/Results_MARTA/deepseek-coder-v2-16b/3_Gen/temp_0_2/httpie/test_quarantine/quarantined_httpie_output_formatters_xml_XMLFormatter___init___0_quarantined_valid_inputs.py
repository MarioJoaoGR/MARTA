
from httpie.output.formatters.xml import XMLFormatter
from unittest.mock import patch

def test_valid_inputs():
    with patch('httpie.output.formatters.xml.XMLFormatter.__init__', return_value=None):
        formatter = XMLFormatter(format_options={'xml': {'format': True}})
        assert formatter.enabled is True

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_formatters_xml_XMLFormatter___init___0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        with patch('httpie.output.formatters.xml.XMLFormatter.__init__', return_value=None):
            formatter = XMLFormatter(format_options={'xml': {'format': True}})
>           assert formatter.enabled is True
E           AttributeError: 'XMLFormatter' object has no attribute 'enabled'

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_formatters_xml_XMLFormatter___init___0_test_valid_inputs.py:8: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_formatters_xml_XMLFormatter___init___0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.11s ===============================
"""