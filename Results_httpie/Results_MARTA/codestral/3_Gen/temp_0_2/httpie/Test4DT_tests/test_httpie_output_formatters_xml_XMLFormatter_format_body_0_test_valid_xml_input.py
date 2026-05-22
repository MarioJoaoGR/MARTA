
import pytest
from unittest.mock import patch, MagicMock
from xml.parsers.expat import ExpatError
from defusedxml.common import DefusedXmlException
from httpie.output.formatters.xml import XMLFormatter

def test_valid_xml_input():
    formatter = XMLFormatter(format_options={'xml': {'format': True, 'indent': 2}})
    
    # Test with valid XML content
    body = '<?xml version="1.0"?><root>content</root>'
    mime = 'application/xml'
    
    with patch('httpie.output.formatters.xml.parse_xml', return_value=MagicMock(encoding='UTF-8')):
        with patch('httpie.output.formatters.xml.pretty_xml', return_value=body):
            assert formatter.format_body(body, mime) == body
