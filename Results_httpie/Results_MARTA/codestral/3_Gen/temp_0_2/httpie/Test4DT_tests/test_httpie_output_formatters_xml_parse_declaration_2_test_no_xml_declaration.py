
import unittest
from unittest.mock import patch
from httpie.output.formatters.xml import parse_declaration, XML_DECLARATION_OPEN, XML_DECLARATION_CLOSE

class TestHttpieOutputFormattersXmlParseDeclaration2TestCase(unittest.TestCase):
    def test_no_xml_declaration(self):
        with patch('httpie.output.formatters.xml.XML_DECLARATION_OPEN', '<?xml'):
            with patch('httpie.output.formatters.xml.XML_DECLARATION_CLOSE', '?>'):
                result = parse_declaration('<root>content</root>')
                self.assertIsNone(result)
