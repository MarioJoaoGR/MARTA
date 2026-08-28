
import pytest
from ansible.plugins.inventory.constructed import InventoryModule

def test_valid_inputs():
    inventory_module = InventoryModule()
    host_object = {'host': 'example.com'}
    loader_object = {}
    sources_list = ['source1', 'source2']
    combined_vars = inventory_module.get_all_host_vars(host_object, loader_object, sources_list)
    
    assert isinstance(combined_vars, dict), "Expected a dictionary"
    assert len(combined_vars) > 0, "Expected non-empty dictionary"

def test_edge_cases():
    inventory_module = InventoryModule()
    host_object = None
    loader_object = {}
    sources_list = []
    combined_vars = inventory_module.get_all_host_vars(host_object, loader_object, sources_list)
    
    assert isinstance(combined_vars, dict), "Expected a dictionary"
    assert len(combined_vars) == 0, "Expected empty dictionary"

def test_invalid_inputs():
    inventory_module = InventoryModule()
    host_object = 'not a dict'
    loader_object = {}
    sources_list = 123
    with pytest.raises(TypeError):
        combined_vars = inventory_module.get_all_host_vars(host_object, loader_object, sources_list)
