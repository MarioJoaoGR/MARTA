
import pytest
from lib.ansible.cli.doc import RoleMixin

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
    assert fqcn == 'example_collection.example_role', "FQCN should include the collection name"
    assert summary['collection'] == 'example_collection', "Summary should contain the collection name"
    assert summary['entry_points'] == {
        'entry_point1': 'Description 1',
        'entry_point2': 'Description 2'
    }, "Summary entry points should match provided argspec"

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
    assert fqcn == 'example_role', "FQCN should not include the collection name if it's empty"
    assert summary['collection'] == '', "Summary should contain an empty string for collection name"
    assert summary['entry_points'] == {
        'entry_point3': 'Description 3'
    }, "Summary entry points should match provided argspec"
