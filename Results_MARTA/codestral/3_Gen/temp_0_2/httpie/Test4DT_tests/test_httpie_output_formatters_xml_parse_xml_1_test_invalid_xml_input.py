
import pytest
from unittest.mock import patch
from defusedxml.minidom import parseString

def parse_xml(data: str):
    """Parse given XML `data` string into an appropriate :class:`~xml.dom.minidom.Document` object."""
    from defusedxml.minidom import parseString
    return parseString(data)

@pytest.mark.parametrize("invalid_xml", [
    "<root><element>value</element>",  # Valid XML but not well-formed
    "<?xml version='1.0'?><root><element>value</element>",  # Well-formed but invalid XML
    "This is not XML at all!",  # Completely non-XML content
])
def test_invalid_xml_input(invalid_xml):
    with pytest.raises(Exception):
        parse_xml(invalid_xml)
