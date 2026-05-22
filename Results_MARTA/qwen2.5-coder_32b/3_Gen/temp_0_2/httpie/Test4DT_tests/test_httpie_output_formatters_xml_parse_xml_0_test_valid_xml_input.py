
import unittest
from unittest.mock import patch, MagicMock
from defusedxml.minidom import parseString

def parse_xml(data: str) -> 'Document':
    """Parse given XML `data` string into an appropriate :class:`~xml.dom.minidom.Document` object."""
    from defusedxml.minidom import parseString
    return parseString(data)

class TestHttpieOutputFormattersXmlParseXml0TestValidXmlInput(unittest.TestCase):
    
    @patch('defusedxml.minidom.parseString')
    def test_valid_xml_input(self, mock_parse_string):
        # Mock the parseString function to return a Document object
        mock_document = MagicMock()
        mock_parse_string.return_value = mock_document
        
        # Example XML data
        xml_data = '<root><element>value</element></root>'
        
        # Call the function under test
        result = parse_xml(xml_data)
        
        # Assert that parseString was called with the correct argument
        mock_parse_string.assert_called_once_with(xml_data)
        
        # Assert that the result is the mocked Document object
        self.assertEqual(result, mock_document)
