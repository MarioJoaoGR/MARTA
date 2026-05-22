
import pytest
from unittest.mock import patch
from httpie.output.formatters.xml import parse_declaration, XML_DECLARATION_OPEN, XML_DECLARATION_CLOSE

def test_malformed_xml_declaration():
    raw_body = '<?xml something else?>'
    with patch('httpie.output.formatters.xml.XML_DECLARATION_OPEN', '<?xml'):
        with patch('httpie.output.formatters.xml.XML_DECLARATION_CLOSE', '?>'):
            result = parse_declaration(raw_body)
            assert result == raw_body
