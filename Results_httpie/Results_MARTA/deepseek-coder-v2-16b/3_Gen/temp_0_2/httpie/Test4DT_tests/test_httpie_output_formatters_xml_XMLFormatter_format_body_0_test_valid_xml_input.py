
import pytest
from unittest.mock import patch, MagicMock
from xml.parsers.expat import ExpatError
from defusedxml.common import DefusedXmlException
from httpie.output.formatters.xml import XMLFormatter

def test_valid_xml_input():
    formatter = XMLFormatter(format_options={'xml': {'format': True, 'indent': 2}})
    
    with patch('httpie.output.formatters.xml.parse_xml', return_value=MagicMock()):
        with patch('httpie.output.formatters.xml.pretty_xml', return_value='<root>content</root>'):
            with patch('httpie.output.formatters.xml.parse_declaration', return_value='<?xml version="1.0"?>'):
                result = formatter.format_body('<?xml version="1.0"?><root>content</root>', 'application/xml')
                assert result == '<root>content</root>'
