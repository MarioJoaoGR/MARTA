
import unittest
from unittest.mock import patch, MagicMock
from defusedxml.minidom import parseString

def parse_xml(data: str) -> 'Document':
    """Parse given XML `data` string into an appropriate :class:`~xml.dom.minidom.Document` object."""
    from defusedxml.minidom import parseString
    return parseString(data)

class TestHttpieOutputFormattersXmlParseXml1TestInvalidXmlInput(unittest.TestCase):
    
    @patch('defusedxml.minidom.parseString')
    def test_invalid_xml_input(self, mock_parse_string):
        # Mock the parseString function to raise an exception for invalid XML input
        mock_parse_string.side_effect = Exception("Invalid XML")
        
        data = "<root><element>value</element></root>"  # Valid XML string
        with self.assertRaises(Exception) as context:
            parse_xml(data)
        self.assertEqual(str(context.exception), "Invalid XML")
