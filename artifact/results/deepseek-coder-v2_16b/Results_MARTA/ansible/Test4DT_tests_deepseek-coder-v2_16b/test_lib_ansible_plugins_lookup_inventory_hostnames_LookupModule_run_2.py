
import pytest
from ansible.plugins.lookup import inventory_hostnames
from unittest.mock import patch, MagicMock

# Fixture to create a mock LookupModule instance for testing
@pytest.fixture
def lookup_module():
    lm = inventory_hostnames.LookupModule()
    lm._loader = MagicMock()
    return lm

# Test scenario 1: Valid input with a single group specified
def test_valid_input_single_group(lookup_module):
    terms = ['webservers']
    variables = {'groups': {'webservers': ['host1', 'host2']}}
    result = lookup_module.run(terms, variables=variables)
    assert result == ['host1', 'host2'], f"Expected ['host1', 'host2'], but got {result}"

# Test scenario 2: Valid input with multiple terms specified
def test_valid_input_multiple_terms(lookup_module):
    terms = ['webservers', 'dbservers']
    variables = {'groups': {'webservers': ['host1', 'host2'], 'dbservers': ['host3', 'host4']}}
    result = lookup_module.run(terms, variables=variables)
    assert result == ['host1', 'host2', 'host3', 'host4'], f"Expected ['host1', 'host2', 'host3', 'host4'], but got {result}"

# Test scenario 3: Invalid input with a nonexistent group
def test_invalid_input_nonexistent_group(lookup_module):
    terms = ['nonexistentgroup']
    variables = {'groups': {'webservers': ['host1', 'host2'], 'dbservers': ['host3', 'host4']}}
    result = lookup_module.run(terms, variables=variables)
    assert result == [], f"Expected an empty list for a nonexistent group, but got {result}"
