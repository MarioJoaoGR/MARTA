
import pytest
from unittest.mock import patch
from defusedxml.minidom import parseString, Document
from httpie.output.formatters.xml import parse_xml

def test_valid_xml_input():
    xml_data = '<root><element>value</element></root>'
    with patch('httpie.output.formatters.xml.parse_xml', return_value=parseString(xml_data)):
        doc = parse_xml(xml_data)
        assert isinstance(doc, Document), f"Expected type: {Document}, but got: {type(doc)}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_output_formatters_xml_parse_xml_0_test_valid_xml_input
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_formatters_xml_parse_xml_0_test_valid_xml_input.py:4:0: E0611: No name 'Document' in module 'defusedxml.minidom' (no-name-in-module)


"""