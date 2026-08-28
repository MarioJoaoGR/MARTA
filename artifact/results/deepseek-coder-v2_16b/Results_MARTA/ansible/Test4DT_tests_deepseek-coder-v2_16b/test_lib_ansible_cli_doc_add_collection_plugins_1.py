
import pytest
from ansible.cli.doc import add_collection_plugins
import os

def list_collection_dirs(coll_filter=None):
    # Mock implementation for testing purposes
    return ['/path/to/collection1', '/path/to/collection2']

def test_add_collection_plugins_basic():
    plugin_list = []
    add_collection_plugins(plugin_list, 'module')
    assert len(plugin_list) == 0, f"Expected empty list, got {plugin_list}"

def test_add_collection_plugins_specific_filter():
    plugin_list = []
    add_collection_plugins(plugin_list, 'module', coll_filter='specific_type')
    assert len(plugin_list) == 0, f"Expected empty list, got {plugin_list}"

def test_add_collection_plugins_default_filter():
    plugin_list = []
    add_collection_plugins(plugin_list, 'module')
    assert len(plugin_list) == 0, f"Expected empty list, got {plugin_list}"
