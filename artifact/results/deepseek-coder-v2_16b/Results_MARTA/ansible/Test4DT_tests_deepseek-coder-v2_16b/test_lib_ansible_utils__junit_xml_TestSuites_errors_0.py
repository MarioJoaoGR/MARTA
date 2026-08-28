
import pytest
from ansible.utils._junit_xml import TestSuites, TestSuite
import typing as t
import xml.etree.ElementTree as ET
import decimal

# Helper function to create a pretty-printed XML string for assertions
def _pretty_xml(element: ET.Element) -> str:
    import xml.dom.minidom
    rough_string = ET.tostring(element, 'utf-8')
    reparsed = xml.dom.minidom.parseString(rough_string.decode('utf-8'))
    return reparsed.toprettyxml(indent="  ")

# Test initialization of TestSuites without suites
def test_test_suites_initialization():
    test_suites = TestSuites()
    assert test_suites.name is None
    assert len(test_suites.suites) == 0

# Test adding a suite to TestSuites

# Test counting errors in TestSuites with multiple suites

# Test counting failures in TestSuites with multiple suites

# Test counting tests in TestSuites with multiple suites

# Test counting total time in TestSuites with multiple suites