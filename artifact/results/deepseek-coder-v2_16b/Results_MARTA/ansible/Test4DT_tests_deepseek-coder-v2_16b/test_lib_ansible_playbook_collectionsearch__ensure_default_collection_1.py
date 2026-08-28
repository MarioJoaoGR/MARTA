
import pytest
from ansible.playbook.collectionsearch import _ensure_default_collection



def test_existing_defaults():
    existing_list = ['ansible.builtin', 'ansible.legacy']
    result = _ensure_default_collection(existing_list)
    assert result == existing_list