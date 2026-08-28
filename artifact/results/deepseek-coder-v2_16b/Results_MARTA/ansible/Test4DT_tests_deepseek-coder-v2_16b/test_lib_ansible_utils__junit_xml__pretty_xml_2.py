
import xml.etree.ElementTree as ET
from xml.dom import minidom
import pytest

def _pretty_xml(element: ET.Element) -> str:
    """Return a pretty formatted XML string representing the given element."""
    return minidom.parseString(ET.tostring(element, encoding='unicode')).toprettyxml()

# Test Scenario 1: Test standard input with a simple XML structure
def test_valid_input():
    root = ET.Element('root')
    child1 = ET.SubElement(root, 'child1')
    child2 = ET.SubElement(root, 'child2')
    
    expected_output = '<root>\n  <child1/>\n  <child2/>\n</root>'
    assert _pretty_xml(root) == expected_output

# Test Scenario 2: Test with None input to check error handling
def test_edge_case():
    element = None
    with pytest.raises(TypeError):
        _pretty_xml(element)

# Test Scenario 3: Test with invalid type input (e.g., int) to check error handling
def test_invalid_input():
    element = 123
    with pytest.raises(TypeError):
        _pretty_xml(element)
