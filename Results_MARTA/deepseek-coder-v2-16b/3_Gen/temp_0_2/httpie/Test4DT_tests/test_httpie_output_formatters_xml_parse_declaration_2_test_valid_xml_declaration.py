
import unittest
from unittest.mock import patch
from httpie.output.formatters.xml import parse_declaration, XML_DECLARATION_OPEN, XML_DECLARATION_CLOSE
from typing import Optional

class TestHttpieOutputFormattersXmlParseDeclaration2TestValidXmlDeclaration(unittest.TestCase):
    
    def test_valid_xml_declaration(self):
        with patch('httpie.output.formatters.xml.XML_DECLARATION_OPEN', '<?xml'):
            with patch('httpie.output.formatters.xml.XML_DECLARATION_CLOSE', '?>'):
                # Test case for valid XML declaration
                raw_body = '<?xml version="1.0" encoding="UTF-8"?>'
                result = parse_declaration(raw_body)
                self.assertEqual(result, '<?xml version="1.0" encoding="UTF-8"?>')
                
                # Test case for string without XML declaration
                raw_body = '<root>content</root>'
                result = parse_declaration(raw_body)
                self.assertIsNone(result)
                
                # Test case for string with invalid XML declaration
                raw_body = '<?xml something else?>'
                result = parse_declaration(raw_body)
                self.assertEqual(result, '<?xml something else?>')
