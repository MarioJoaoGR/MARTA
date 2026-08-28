
import pytest
from ansible.utils._junit_xml import TestSuites, TestSuite, _pretty_xml
from unittest.mock import patch


def test_to_pretty_xml_with_suite():
    suite1 = TestSuite(name="Example Suite")
    suites = TestSuites()
    suites.suites.append(suite1)
    xml_string = suites.to_pretty_xml()
    assert xml_string == _pretty_xml(suites.get_xml_element())

def test_to_pretty_xml_with_properties():
    suite1 = TestSuite(name="Example Suite", properties={"env": "test"})
    suites = TestSuites()
    suites.suites.append(suite1)
    xml_string = suites.to_pretty_xml()
    assert xml_string == _pretty_xml(suites.get_xml_element())
