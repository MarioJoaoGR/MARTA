
import pytest
from unittest.mock import patch
from xml.etree.ElementTree import ParseError
from httpie.output.formatters.xml import parse_declaration, XML_DECLARATION_OPEN, XML_DECLARATION_CLOSE

def test_invalid_xml_declaration():
    with patch('httpie.output.formatters.xml.XML_DECLARATION_OPEN', '<?xml'):
        with patch('httpie.output.formatters.xml.XML_DECLARATION_CLOSE', '?>'):
            raw_body = '<?xml something else?>'
            result = parse_declaration(raw_body)
            assert result == '<?xml something else?>'
