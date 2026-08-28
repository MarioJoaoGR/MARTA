
import pytest
from ansible.vars.manager import VariableManager
from collections import defaultdict
from unittest.mock import MagicMock, patch

# Test initialization without parameters

# Test initialization with loader, inventory, and version_info

# Test getting extra vars

# Test setting inventory
def test_set_inventory():
    vm = VariableManager()
    inventory = MagicMock()
    vm.set_inventory(inventory)
    assert vm._inventory == inventory

# Test getting delegated vars

# Test setting host facts

# Test setting non-persistent facts
def test_set_nonpersistent_facts():
    vm = VariableManager()
    vm.set_nonpersistent_facts("example_host", {"key1": "value1", "key2": "value2"})
    assert vm._nonpersistent_fact_cache["example_host"] == {"key1": "value1", "key2": "value2"}

# Test setting a host variable
def test_set_host_variable():
    vm = VariableManager()
    vm.set_host_variable("example_host", "memory", 1024)
    assert vm._vars_cache["example_host"]["memory"] == 1024