
import pytest
from httpie.output.formatters.xml import parse_xml
from defusedxml.minidom import parseString, Document
from unittest.mock import patch

def test_invalid_xml_input():
    xml_data = '<root><element>value</invalid>'
    with pytest.raises(Exception):
        with patch('defusedxml.minidom.parseString', side_effect=Exception("Invalid XML")):
            doc = parse_xml(xml_data)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_output_formatters_xml_parse_xml_1_test_invalid_xml_input
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_formatters_xml_parse_xml_1_test_invalid_xml_input.py:4:0: E0611: No name 'Document' in module 'defusedxml.minidom' (no-name-in-module)


"""