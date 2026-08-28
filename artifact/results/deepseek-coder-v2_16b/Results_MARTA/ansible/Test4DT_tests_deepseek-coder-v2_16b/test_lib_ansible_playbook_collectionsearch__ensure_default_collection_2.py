
import pytest
from ansible.playbook.collectionsearch import _ensure_default_collection



def test_existing_collections():
    existing_collections = ['ansible.builtin', 'ansible.legacy', 'custom.collection']
    result = _ensure_default_collection(existing_collections)
    assert result == ['ansible.builtin', 'ansible.legacy', 'custom.collection']