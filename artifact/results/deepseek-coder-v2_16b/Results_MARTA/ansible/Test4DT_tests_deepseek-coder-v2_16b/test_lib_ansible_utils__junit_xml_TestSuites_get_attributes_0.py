
import pytest
from ansible.utils._junit_xml import TestSuites

def test_get_attributes_default():
    test_suites = TestSuites()
    attributes = test_suites.get_attributes()
    assert isinstance(attributes, dict)
    assert 'disabled' in attributes
    assert 'errors' in attributes
    assert 'failures' in attributes
    assert 'name' not in attributes  # name is None by default and should not be in the dictionary
    assert 'tests' in attributes
    assert 'time' in attributes
    assert attributes['disabled'] == '0'
    assert attributes['errors'] == '0'
    assert attributes['failures'] == '0'
    assert attributes['tests'] == '0'
    assert attributes['time'] == '0'
