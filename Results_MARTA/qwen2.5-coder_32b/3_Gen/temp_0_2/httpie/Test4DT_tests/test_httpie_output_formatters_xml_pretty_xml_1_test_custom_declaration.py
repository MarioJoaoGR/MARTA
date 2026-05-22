
import unittest
from xml.dom import minidom
from httpie.output.formatters.xml import pretty_xml

class TestHttpieOutputFormattersXmlPrettyXml1TestCustomDeclaration(unittest.TestCase):
    def test_custom_declaration(self):
        doc = minidom.parseString('<root>content</root>')
        custom_declaration = '<?xml version="1.0" encoding="ISO-8859-1"?>'
        
        result = pretty_xml(doc, declaration=custom_declaration)
        
        expected_lines = [
            '<?xml version="1.0" encoding="ISO-8859-1"?>',
            '<root>content</root>'
        ]
        self.assertEqual('\n'.join(expected_lines), result)
