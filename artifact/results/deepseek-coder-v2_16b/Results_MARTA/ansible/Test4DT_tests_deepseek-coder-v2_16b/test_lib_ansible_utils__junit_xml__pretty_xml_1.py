
import xml.etree.ElementTree as ET
from xml.dom import minidom
import pytest

def _pretty_xml(element: ET.Element) -> str:
    """Return a pretty formatted XML string representing the given element."""
    return minidom.parseString(ET.tostring(element, encoding='unicode')).toprettyxml()

# Test cases for _pretty_xml function


def test_valid_element():
    root = ET.Element('root')
    child1 = ET.SubElement(root, 'child1')
    child2 = ET.SubElement(root, 'child2')
    pretty_xml = _pretty_xml(root)
    assert isinstance(pretty_xml, str), "Expected a string representation of the XML"
    # Add more assertions to check specific parts of the XML if needed