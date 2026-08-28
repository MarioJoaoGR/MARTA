
import pytest
from ansible.inventory.manager import InventoryManager
from unittest.mock import patch

# Test Scenario 1: Test standard input for remove_restriction method
def test_valid_input():
    loader = "some_loader"
    sources = ["source1", "source2"]
    manager = InventoryManager(loader=loader, sources=sources)
    manager.restrict_to_hosts(["host1"])  # Restrict to some hosts for the sake of test
    
    assert manager._restriction == ["host1"]  # Initial restriction should be set
    
    manager.remove_restriction()
    
    assert manager._restriction is None  # After removing, it should be None

# Test Scenario 2: Test edge case where no restriction is initially present
def test_edge_case():
    loader = "some_loader"
    sources = ["source1", "source2"]
    manager = InventoryManager(loader=loader, sources=sources)
    
    assert manager._restriction is None  # No initial restriction should be set
    
    manager.remove_restriction()
    
    assert manager._restriction is None  # After removing, it should still be None

# Test Scenario 3: Test invalid input scenario for remove_restriction method
def test_invalid_input():
    with pytest.raises(TypeError):  # Expecting a TypeError since the method expects no arguments
        InventoryManager().remove_restriction()
