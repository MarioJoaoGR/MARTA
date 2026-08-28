
import pytest
from ansible.vars.manager import VariableManager
from collections import defaultdict
from hashlib import sha1
import os
from unittest.mock import patch, MagicMock

# Test 1: Valid Input
def test_valid_input():
    vm = VariableManager()
    facts = {'key1': 'value1', 'key2': 'value2'}
    vm.set_nonpersistent_facts('example_host', facts)
    assert vm._nonpersistent_fact_cache['example_host'] == facts

# Test 2: Edge Case Input (None)
def test_edge_case():
    vm = VariableManager()
    with pytest.raises(AssertionError):
        vm.set_nonpersistent_facts('example_host', None)

# Test 3: Invalid Input Type (int)
def test_invalid_input():
    vm = VariableManager()
    with pytest.raises(AssertionError):
        vm.set_nonpersistent_facts('example_host', 123)
