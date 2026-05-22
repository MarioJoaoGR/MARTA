
import pytest
from unittest.mock import patch, MagicMock
from httpie.output.formatters.xml import XMLFormatter

@pytest.fixture(autouse=True)
def setup_formatter():
    formatter = XMLFormatter(format_options={'xml': {'format': True, 'indent': 2}})
    return formatter

def test_invalid_mime_type(setup_formatter):
    with patch('httpie.output.formatters.xml.parse_xml', side_effect=Exception("Mocked parse_xml error")):
        result = setup_formatter.format_body('<root>content</root>', 'application/json')
        assert result == '<root>content</root>'
