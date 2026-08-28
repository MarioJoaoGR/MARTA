# Module: ansible.playbook.collectionsearch
import pytest
from ansible.playbook.collectionsearch import CollectionSearch

# Test Case 1: Loading Collections with Default Behavior
def test_load_collections_default():
    instance = CollectionSearch()
    result = instance._load_collections('attr', ['ansible.builtin'])
    assert result == ['ansible.builtin', 'ansible.legacy'] or result is None, f"Expected default collections or None, but got {result}"

# Test Case 2: Loading Collections with No Input (Default Behavior)
def test_load_collections_no_input():
    instance = CollectionSearch()
    result = instance._load_collections('attr', [])
    assert result is None, f"Expected None for no input, but got {result}"

# Test Case 3: Loading Collections with Custom Collection
def test_load_collections_custom_collection():
    instance = CollectionSearch()
    result = instance._load_collections('attr', ['custom_collection'])
    assert result == ['ansible.builtin', 'ansible.legacy', 'custom_collection'], f"Expected specific collections including custom, but got {result}"

# Test Case 4: Loading Collections with Templated Collection (Warning Issued)
def test_load_collections_templated_collection():
    instance = CollectionSearch()
    with pytest.warns(UserWarning):
        result = instance._load_collections('attr', ['{{ templated_collection }}'])
    assert result == ['ansible.builtin', 'ansible.legacy', '{{ templated_collection }}'], f"Expected specific collections including templated, but got {result}"
