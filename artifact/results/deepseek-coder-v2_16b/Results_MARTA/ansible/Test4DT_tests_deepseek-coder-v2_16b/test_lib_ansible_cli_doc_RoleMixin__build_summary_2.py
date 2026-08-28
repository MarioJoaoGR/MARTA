
import pytest
from ansible.cli.doc import RoleMixin

def test_build_summary_with_collection():
    role_mixin = RoleMixin()
    role = 'example_role'
    collection = 'example_collection'
    argspec = {
        'entry_point1': {'short_description': 'Description 1'},
        'entry_point2': {'short_description': 'Description 2'}
    }
    result = role_mixin._build_summary(role, collection, argspec)
    assert isinstance(result, tuple), "Result should be a tuple"
    fqcn, summary = result
    assert fqcn == 'example_collection.example_role', "FQCN should match the collection and role name"
    assert summary['collection'] == 'example_collection', "Summary should contain the correct collection name"
    assert summary['entry_points'] == {
        'entry_point1': 'Description 1',
        'entry_point2': 'Description 2'
    }, "Entry points in summary should match the provided argspec"

def test_build_summary_without_collection():
    role_mixin = RoleMixin()
    role = 'example_role'
    collection = ''
    argspec = {
        'entry_point3': {'short_description': 'Description 3'}
    }
    result = role_mixin._build_summary(role, collection, argspec)
    assert isinstance(result, tuple), "Result should be a tuple"
    fqcn, summary = result
    assert fqcn == 'example_role', "FQCN should match the role name when no collection is provided"
    assert summary['collection'] == '', "Summary should contain an empty string for collection when not applicable"
    assert summary['entry_points'] == {
        'entry_point3': 'Description 3'
    }, "Entry points in summary should match the provided argspec without a collection"
