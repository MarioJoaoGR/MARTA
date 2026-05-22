
import unittest
from unittest.mock import patch
from httpie.output.formatters.xml import parse_declaration, XML_DECLARATION_OPEN, XML_DECLARATION_CLOSE
from typing import Optional

class TestHttpieOutputFormattersXmlParseDeclaration(unittest.TestCase):
    
    def test_valid_xml_declaration(self):
        with patch('httpie.output.formatters.xml.XML_DECLARATION_OPEN', '<?xml'):
            with patch('httpie.output.formatters.xml.XML_DECLARATION_CLOSE', '?>'):
                self.assertEqual(parse_declaration('<?xml version="1.0" encoding="UTF-8"?>'), '<?xml version="1.0" encoding="UTF-8"?>')
                self.assertIsNone(parse_declaration('<root>content</root>'))
                self.assertEqual(parse_declaration('<?xml something else?>'), '<?xml something else?>')
