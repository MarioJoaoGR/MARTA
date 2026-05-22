
import pytest
from defusedxml.minidom import parseString
from unittest.mock import patch

def parse_xml(data: str) -> 'Document':
    """Parse given XML `data` string into an appropriate :class:`~xml.dom.minidom.Document` object."""
    from defusedxml.minidom import parseString
    return parseString(data)

@pytest.mark.parametrize("data", ["<root><element>value</element></root>"])
def test_valid_xml_input(data):
    with patch('defusedxml.minidom.parseString') as mock_parse:
        # Mock the return value of parseString to be a Document object
        mock_doc = mock_parse.return_value
        
        # Call the function under test
        result = parse_xml(data)
        
        # Assert that parseString was called with the correct data
        mock_parse.assert_called_once_with(data)
        
        # Add more assertions if needed to verify the output or behavior of the function
        assert isinstance(result, mock_doc.__class__)
