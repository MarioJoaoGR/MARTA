
import pytest
from unittest.mock import patch
from ansible.cli.doc import add_collection_plugins

def test_valid_input():
    plugin_list = []
    add_collection_plugins(plugin_list, 'module')
    assert isinstance(plugin_list, list), "Expected plugin_list to be a list"
    assert len(plugin_list) == 0, "Expected no plugins in the list for valid input without filter"

def test_edge_case_none():
    with pytest.raises(TypeError):
        add_collection_plugins(None, 'module')

def test_invalid_input():
    plugin_list = []
    with pytest.raises(ValueError):
        add_collection_plugins(plugin_list, 'invalid_type')
