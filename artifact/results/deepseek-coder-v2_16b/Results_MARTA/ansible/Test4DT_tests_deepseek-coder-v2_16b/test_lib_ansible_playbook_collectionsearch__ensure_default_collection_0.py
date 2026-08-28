
import pytest
from ansible.playbook.collectionsearch import _ensure_default_collection

# Test scenarios
def test_valid_input_no_params():
    result = _ensure_default_collection()
    assert result == ['ansible.builtin', 'ansible.legacy']

def test_valid_input_empty_list():
    result = _ensure_default_collection([])
    assert result == ['ansible.builtin', 'ansible.legacy']

def test_valid_input_existing_collections():
    result = _ensure_default_collection(['ansible.builtin', 'ansible.legacy'])
    assert result == ['ansible.builtin', 'ansible.legacy']

def test_edge_case_none():
    result = _ensure_default_collection(None)
    assert result == ['ansible.builtin', 'ansible.legacy']

def test_edge_case_empty_list():
    result = _ensure_default_collection([])
    assert result == ['ansible.builtin', 'ansible.legacy']

def test_error_handling_invalid_type():
    with pytest.raises(TypeError):
        _ensure_default_collection(12345)
