
import pytest
from ansible.playbook.collectionsearch import _ensure_default_collection

def test_no_collection_provided():
    result = _ensure_default_collection()
    assert result == ['ansible.legacy']

def test_custom_collection_provided():
    result = _ensure_default_collection(['custom_collection'])
    assert result == ['ansible.builtin', 'ansible.legacy', 'custom_collection']

def test_existing_collections_provided():
    result = _ensure_default_collection(['ansible.builtin', 'ansible.legacy'])
    assert result == ['ansible.builtin', 'ansible.legacy']

def test_none_provided():
    result = _ensure_default_collection(None)
    assert result == ['ansible.legacy']

def test_empty_list_provided():
    result = _ensure_default_collection([])
    assert result == ['ansible.legacy']
