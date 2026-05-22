
import unittest
from xml.dom import minidom
from httpie.output.formatters.xml import pretty_xml
from unittest.mock import patch, MagicMock

class TestHttpieOutputFormattersXmlPrettyXml0TestCustomDeclaration(unittest.TestCase):
    @patch('httpie.output.formatters.xml.parse_declaration', return_value=True)
    def test_custom_declaration(self, mock_parse_declaration):
        doc = minidom.parseString('<root>content</root>')
        custom_declaration = '<?xml version="1.0" encoding="ISO-8859-1"?>'
        
        result = pretty_xml(doc, declaration=custom_declaration)
        
        expected_lines = [
            '<?xml version="1.0" encoding="ISO-8859-1"?>',
            '<root>content</root>'
        ]
        self.assertEqual('\n'.join(expected_lines), result)
