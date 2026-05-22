
from xml.dom import minidom
from httpie.output.formatters.xml import pretty_xml, parse_declaration
from unittest.mock import patch

class TestHttpieOutputFormattersXmlPrettyXml0TestCustomDeclaration(object):
    @patch('httpie.output.formatters.xml.parse_declaration', return_value=True)
    def test_custom_declaration(self, mock_parse_declaration):
        # Create a sample XML document
        doc = minidom.parseString('<root>content</root>')
    
        # Define custom declaration
        custom_declaration = '<?xml version="1.0" encoding="ISO-8859-1"?>'
    
        # Call the function with the custom declaration
        result = pretty_xml(doc, declaration=custom_declaration)
    
        # Check that the custom declaration is included in the output
        expected_lines = [custom_declaration] + [line for line in doc.toprettyxml().decode('UTF-8').splitlines() if line.strip()]
        
        assert result == '\n'.join(expected_lines)

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

httpie/Test4DT_tests_codestral/test_httpie_output_formatters_xml_pretty_xml_0_test_custom_declaration.py F [100%]

=================================== FAILURES ===================================
_ TestHttpieOutputFormattersXmlPrettyXml0TestCustomDeclaration.test_custom_declaration _

self = <Test4DT_tests_codestral.test_httpie_output_formatters_xml_pretty_xml_0_test_custom_declaration.TestHttpieOutputFormattersXmlPrettyXml0TestCustomDeclaration object at 0x7f95e48e85d0>
mock_parse_declaration = <MagicMock name='parse_declaration' id='140281755352848'>

    @patch('httpie.output.formatters.xml.parse_declaration', return_value=True)
    def test_custom_declaration(self, mock_parse_declaration):
        # Create a sample XML document
        doc = minidom.parseString('<root>content</root>')
    
        # Define custom declaration
        custom_declaration = '<?xml version="1.0" encoding="ISO-8859-1"?>'
    
        # Call the function with the custom declaration
        result = pretty_xml(doc, declaration=custom_declaration)
    
        # Check that the custom declaration is included in the output
>       expected_lines = [custom_declaration] + [line for line in doc.toprettyxml().decode('UTF-8').splitlines() if line.strip()]
E       AttributeError: 'str' object has no attribute 'decode'

httpie/Test4DT_tests_codestral/test_httpie_output_formatters_xml_pretty_xml_0_test_custom_declaration.py:19: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_output_formatters_xml_pretty_xml_0_test_custom_declaration.py::TestHttpieOutputFormattersXmlPrettyXml0TestCustomDeclaration::test_custom_declaration
============================== 1 failed in 0.17s ===============================
"""