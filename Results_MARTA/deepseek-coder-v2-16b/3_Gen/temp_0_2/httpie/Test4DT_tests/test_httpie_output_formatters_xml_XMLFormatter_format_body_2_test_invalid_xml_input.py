
import pytest
from unittest.mock import patch, MagicMock
from xml.parsers.expat import ExpatError
from defusedxml.common import DefusedXmlException
from httpie.output.formatters.xml import XMLFormatter

def test_invalid_xml_input():
    with patch('httpie.output.formatters.xml.parse_xml', side_effect=ExpatError("Invalid XML")):
        formatter = XMLFormatter(format_options={'xml': {'format': True, 'indent': 2}})
        result = formatter.format_body('<?xml version="1.0"?><root>content</root>', 'application/xml')
        assert result == '<?xml version="1.0"?><root>content</root>'
