
import pytest
from xml.etree.ElementTree import Element as ET_Element
from ansible.utils._junit_xml import TestSuites, TestSuite

# Helper function to create a simple test suite for testing purposes
def create_simple_test_suite(name):
    suite = TestSuite(name)
    return suite

@pytest.fixture
def empty_test_suites():
    return TestSuites()

@pytest.fixture
def test_suites_with_two_suites():
    suite1 = create_simple_test_suite("Suite 1")
    suite2 = create_simple_test_suite("Suite 2")
    suites = [suite1, suite2]
    return TestSuites(suites=suites)

def test_empty_test_suites_get_xml_element(empty_test_suites):
    """Test that an empty TestSuites instance generates an empty testsuites XML element."""
    xml_element = empty_test_suites.get_xml_element()
    assert xml_element.tag == 'testsuites'
    assert len(xml_element) == 0

def test_test_suites_with_two_suites_get_xml_element(test_suites_with_two_suites):
    """Test that a TestSuites instance with two suites generates a testsuites XML element with nested suite elements."""
    xml_element = test_suites_with_two_suites.get_xml_element()
    assert xml_element.tag == 'testsuites'
    assert len(xml_element) == 2
    for i, suite in enumerate(test_suites_with_two_suites.suites):
        assert xml_element[i].tag == 'testsuite'
        assert xml_element[i].attrib['name'] == suite.name

def test_get_xml_element_attributes():
    """Test that the get_xml_element method includes attributes derived from the TestSuites instance."""
    test_suites = TestSuites()
    test_suites.name = "Example Suite"
    suite1 = create_simple_test_suite("Suite 1")
    suite2 = create_simple_test_suite("Suite 2")
    test_suites.suites = [suite1, suite2]
    
    xml_element = test_suites.get_xml_element()
    assert xml_element.attrib['name'] == "Example Suite"

def test_get_xml_element_no_suites():
    """Test that the get_xml_element method handles the case where there are no suites."""
    test_suites = TestSuites(suites=[])
    xml_element = test_suites.get_xml_element()
    assert xml_element.tag == 'testsuites'
    assert len(xml_element) == 0

def test_get_xml_element_with_properties():
    """Test that the get_xml_element method includes properties in the XML element."""
    test_suites = TestSuites()
    test_suites.name = "Example Suite"
    property1 = ET_Element('property', {'name': 'prop1', 'value': 'value1'})
    property2 = ET_Element('property', {'name': 'prop2', 'value': 'value2'})
    test_suites.properties = [property1, property2]
    
    xml_element = test_suites.get_xml_element()