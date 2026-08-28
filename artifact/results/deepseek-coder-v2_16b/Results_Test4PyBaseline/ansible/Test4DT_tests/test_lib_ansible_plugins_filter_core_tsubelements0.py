# Module: ansible.plugins.filter.core
import pytest
from ansible.plugins.filter import core

# Test cases for subelements function
def test_subelements_with_list_of_dicts():
    obj = [{"name": "alice", "groups": ["wheel"], "authorized": ["/tmp/alice/onekey.pub"]}]
    result = core.subelements(obj, 'groups')
    assert result == [({'name': 'alice', 'groups': ['wheel'], 'authorized': ['/tmp/alice/onekey.pub']}, 'wheel')]

def test_subelements_with_single_dict_and_different_subelements():
    obj = {"user": {"name": "bob", "roles": ["admin"], "permissions": ["read", "write"]}}
    result = core.subelements(obj, ['roles', 'permissions'])
    expected_result = [({'user': {'name': 'bob', 'roles': ['admin'], 'permissions': ['read', 'write']}}, 'admin'), 
                        ({'user': {'name': 'bob', 'roles': ['admin'], 'permissions': ['read', 'write']}}, 'read'), 
                        ({'user': {'name': 'bob', 'roles': ['admin'], 'permissions': ['read', 'write']}}, 'write')]
    assert result == expected_result

def test_subelements_with_list_of_dicts_skip_missing():
    obj = [{"name": "charlie", "groups": ["wheel"], "authorized": ["/tmp/charlie/onekey.pub"]}]
    result = core.subelements(obj, 'roles', skip_missing=True)
    assert result == [({'name': 'charlie', 'groups': ['wheel'], 'authorized': ['/tmp/charlie/onekey.pub']}, 'wheel')]

def test_subelements_with_string_representation_of_subelements():
    obj = {"user": {"name": "dave", "roles": ["editor"], "permissions": ["read"]}}
    result = core.subelements(obj, 'user.roles')
    assert result == [({'user': {'name': 'dave', 'roles': ['editor'], 'permissions': ['read']}}, 'editor')]

def test_subelements_with_incorrect_input_types():
    with pytest.raises(core.AnsibleFilterTypeError):
        core.subelements("not a dict or list", "invalid")

def test_subelements_with_missing_key_and_skip_missing():
    obj = {"user": {"name": "eve"}}
    result = core.subelements(obj, 'user.roles', skip_missing=True)
    assert result == []

def test_subelements_with_non_dict_or_list_input():
    with pytest.raises(core.AnsibleFilterTypeError):
        core.subelements("not a dict or list", "invalid")
