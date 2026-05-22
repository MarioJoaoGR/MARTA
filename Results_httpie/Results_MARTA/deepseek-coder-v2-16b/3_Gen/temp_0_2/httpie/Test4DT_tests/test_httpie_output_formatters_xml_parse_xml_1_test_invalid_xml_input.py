
import pytest
from unittest.mock import patch
from httpie.output.formatters.xml import parse_xml
from xml.dom.minidom import Document

def test_invalid_xml_input():
    with patch('httpie.output.formatters.xml.parse_xml') as mock_parse_xml:
        # Mock the behavior of parse_xml to raise an exception for invalid XML
        mock_parse_xml.side_effect = Exception("Invalid XML")
        
        xml_data = '<root><element>value</>'
        with pytest.raises(Exception):
            parse_xml(xml_data)
