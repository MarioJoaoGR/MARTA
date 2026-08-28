
import pytest
from datetime import datetime
import typing as t
import dataclasses
from ansible.utils._junit_xml import TestSuite, TestCase

@pytest.fixture
def setup_suite():
    suite = TestSuite()
    suite.name = "Example Suite"
    suite.hostname = "localhost"
    suite.id = "12345"
    suite.package = "example_package"
    suite.timestamp = datetime.now()
    suite.properties["env"] = "production"
    suite.cases = [TestCase(name="Test Case 1"), TestCase(name="Test Case 2")]
    suite.system_out = "Output from the system."
    return suite

def test_get_attributes_basic(setup_suite):
    attributes = setup_suite.get_attributes()
    assert 'disabled' not in attributes, "Disabled should not be included by default"
    assert attributes['errors'] == 0, "Errors should be zero by default"
    assert attributes['failures'] == 0, "Failures should be zero by default"
    assert attributes['hostname'] == 'localhost', "Hostname should match the set value"
    assert attributes['id'] == '12345', "ID should match the set value"
    assert attributes['name'] == 'Example Suite', "Name should match the set value"
    assert attributes['package'] == 'example_package', "Package should match the set value"
    assert attributes['skipped'] == 0, "Skipped tests should be zero by default"
    assert attributes['tests'] == 2, "Total tests should include all cases"
    assert isinstance(attributes['timestamp'], str), "Timestamp should be a string in ISO format"
    assert attributes['properties'] == {'env': 'production'}, "Properties should match the set values"
    assert len(attributes['cases']) == 2, "Cases should include all test cases"
    assert attributes['system_out'] == 'Output from the system.', "System output should match the set value"
    assert attributes['system_err'] is None, "System error should be omitted by default"
