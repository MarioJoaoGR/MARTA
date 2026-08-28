# Module: ansible.cli.doc
import pytest
from ansible.cli.doc import RoleMixin

# Test cases for _build_doc method
def test_build_doc_with_collection():
    role_mixin = RoleMixin()
    role = "example_role"
    path = "path/to/role"
    collection = "example_collection"
    argspec = {'entry1': {'arg1': 'value1'}}
    entry_point = None
    
    fqcn, doc = role_mixin._build_doc(role, path, collection, argspec, entry_point)
    assert fqcn == "example_collection.example_role"
    assert doc['path'] == path
    assert doc['collection'] == collection
    assert 'entry1' in doc['entry_points']
    assert doc['entry_points']['entry1'] == {'arg1': 'value1'}

def test_build_doc_without_collection():
    role_mixin = RoleMixin()
    role = "example_role"
    path = "path/to/role"
    collection = None
    argspec = {'entry1': {'arg1': 'value1'}}
    entry_point = None
    
    fqcn, doc = role_mixin._build_doc(role, path, collection, argspec, entry_point)
    assert fqcn == "example_role"
    assert doc['path'] == path
    assert doc['collection'] is None
    assert 'entry1' in doc['entry_points']
    assert doc['entry_points']['entry1'] == {'arg1': 'value1'}

def test_build_doc_with_specific_entry_point():
    role_mixin = RoleMixin()
    role = "example_role"
    path = "path/to/role"
    collection = "example_collection"
    argspec = {'entry1': {'arg1': 'value1'}, 'entry2': {'arg2': 'value2'}}
    entry_point = 'entry2'
    
    fqcn, doc = role_mixin._build_doc(role, path, collection, argspec, entry_point)
    assert fqcn == "example_collection.example_role"
    assert doc['path'] == path
    assert doc['collection'] == collection
    assert 'entry2' in doc['entry_points']
    assert doc['entry_points']['entry2'] == {'arg2': 'value2'}
    assert not ('entry1' in doc['entry_points'])

def test_build_doc_with_no_entry_points():
    role_mixin = RoleMixin()
    role = "example_role"
    path = "path/to/role"
    collection = "example_collection"
    argspec = {}
    entry_point = None
    
    fqcn, doc = role_mixin._build_doc(role, path, collection, argspec, entry_point)
    assert fqcn == "example_collection.example_role"
    assert doc is None
