
import pytest
from ansible.module_utils.facts.other import facter
from ansible.module_utils import basic

# Fixture to create a mock module for testing
@pytest.fixture(scope="module")
def valid_module():
    module = basic.AnsibleModule(argument_spec={})
    return module

# Test case to check if the FacterFactCollector can collect facts with valid input

# Test case to check if the FacterFactCollector returns an empty dictionary when no module is provided
def test_no_module():
    facter_collector = facter.FacterFactCollector()
    collected_facts = facter_collector.collect(module=None)
    assert isinstance(collected_facts, dict), "Collected facts should be a dictionary"
    assert len(collected_facts) == 0, "Collected facts should be empty when no module is provided"