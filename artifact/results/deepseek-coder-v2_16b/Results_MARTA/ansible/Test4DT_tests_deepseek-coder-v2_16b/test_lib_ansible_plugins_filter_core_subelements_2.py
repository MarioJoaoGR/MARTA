
import pytest
from ansible.plugins.filter.core import subelements
from ansible.errors import AnsibleFilterError, AnsibleFilterTypeError

# Test scenarios for subelements function

def test_valid_case_1():
    obj = [{"name": "alice", "groups": ["wheel"], "authorized": ["/tmp/alice/onekey.pub"]}]
    result = subelements(obj, 'groups')
    assert result == [({'name': 'alice', 'groups': ['wheel'], 'authorized': ['/tmp/alice/onekey.pub']}, 'wheel')]

def test_valid_case_2():
    obj = {"users": [{"name": "bob", "groups": ["wheel"], "authorized": ["/tmp/bob/onekey.pub"}]]}
    result = subelements(obj, 'users.groups')
    assert result == [({'name': 'bob', 'groups': ['wheel'], 'authorized': ['/tmp/bob/onekey.pub']}, 'wheel')]

def test_valid_case_3():
    obj = {"users": [{"name": "charlie", "groups": ["sudo"], "authorized": ["/tmp/charlie/onekey.pub"}]]}
    result = subelements(obj, ['users', 'groups'])
    assert result == [({'name': 'charlie', 'groups': ['sudo'], 'authorized': ['/tmp/charlie/onekey.pub']}, 'sudo')]

def test_edge_case_1():
    obj = None
    with pytest.raises(AnsibleFilterError):
        subelements(obj, 'groups')

def test_edge_case_2():
    obj = []
    result = subelements(obj, 'groups')
    assert result == []

def test_error_case_1():
    obj = "not a dictionary or list"
    with pytest.raises(AnsibleFilterError):
        subelements(obj, 'groups')

def test_error_case_2():
    obj = {"users": [{"name": "eve", "groups": ["wheel"], "authorized": ["/tmp/eve/onekey.pub"}]}}
    with pytest.raises(AnsibleFilterTypeError):
        subelements(obj, 'users.roles')
