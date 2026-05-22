
import pytest
from unittest.mock import patch, MagicMock
from httpie.output.formatters.xml import XMLFormatter, parse_xml, pretty_xml, parse_declaration

def test_valid_xml_input():
    with patch('httpie.output.formatters.xml.parse_xml', return_value=MagicMock(encoding='UTF-8')):
        formatter = XMLFormatter(format_options={'xml': {'format': True, 'indent': 2}})
        body = '<?xml version="1.0"?><root>content</root>'
        mime = 'application/xml'

        formatted_body = formatter.format_body(body, mime)

        assert formatted_body == '<?xml version="1.0" encoding="UTF-8"?>\n<root>content</root>'

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

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_formatters_xml_XMLFormatter_format_body_0_test_valid_xml_input.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_valid_xml_input _____________________________

    def test_valid_xml_input():
        with patch('httpie.output.formatters.xml.parse_xml', return_value=MagicMock(encoding='UTF-8')):
            formatter = XMLFormatter(format_options={'xml': {'format': True, 'indent': 2}})
            body = '<?xml version="1.0"?><root>content</root>'
            mime = 'application/xml'
    
            formatted_body = formatter.format_body(body, mime)
    
>           assert formatted_body == '<?xml version="1.0" encoding="UTF-8"?>\n<root>content</root>'
E           assert '' == '<?xml versio...ontent</root>'
E             
E             - <?xml version="1.0" encoding="UTF-8"?>
E             - <root>content</root>

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_formatters_xml_XMLFormatter_format_body_0_test_valid_xml_input.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_formatters_xml_XMLFormatter_format_body_0_test_valid_xml_input.py::test_valid_xml_input
============================== 1 failed in 0.09s ===============================
"""