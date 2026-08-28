
import pytest
from ansible.cli.doc import RoleMixin

# Test case for the scenario where collection is present
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

# Test case for the scenario where collection is not present
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

# Test case for the scenario where a specific entry point is provided
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

# Test case for the scenario where no entry points are found
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

# Test case for the scenario where no entry points are found and should set doc to None
def test_build_doc_with_no_entry_points_and_set_to_none():
    role_mixin = RoleMixin()
    role = "example_role"
    path = "path/to/role"
    collection = "example_collection"
    argspec = {}
    entry_point = None
    
    fqcn, doc = role_mixin._build_doc(role, path, collection, argspec, entry_point)
    assert fqcn == "example_collection.example_role"
    assert doc is None

# Test case to check the return type and structure of the function when a valid document is built
def test_build_doc_returns_valid_document():
    role_mixin = RoleMixin()
    role = "example_role"
    path = "path/to/role"
    collection = "example_collection"
    argspec = {'entry1': {'arg1': 'value1'}}
    entry_point = None
    
    fqcn, doc = role_mixin._build_doc(role, path, collection, argspec, entry_point)
    assert isinstance(fqcn, str)
    assert isinstance(doc, dict) or doc is None
