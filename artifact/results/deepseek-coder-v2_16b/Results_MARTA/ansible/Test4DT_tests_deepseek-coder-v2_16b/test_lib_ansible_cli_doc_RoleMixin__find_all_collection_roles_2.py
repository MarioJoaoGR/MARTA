
import pytest
from ansible.cli.doc import RoleMixin
import os

@pytest.fixture(scope="module")
def custom_mixin():
    return RoleMixin()

def test_find_all_collection_roles_no_filters_or_collection_filter(custom_mixin):
    found_roles = custom_mixin._find_all_collection_roles()
    assert isinstance(found_roles, set)

def test_find_all_collection_roles_with_name_filters(custom_mixin):
    name_filters = ('roleA', 'community.general.roleB')
    found_roles = custom_mixin._find_all_collection_roles(name_filters=name_filters)
    assert isinstance(found_roles, set)

def test_find_all_collection_roles_with_collection_filter(custom_mixin):
    collection_filter = 'community.general'
    found_roles = custom_mixin._find_all_collection_roles(collection_filter=collection_filter)
    assert isinstance(found_roles, set)

def test_find_all_collection_roles_with_both_filters(custom_mixin):
    name_filters = ('roleA', 'community.general.roleB')
    collection_filter = 'community.general'
    found_roles = custom_mixin._find_all_collection_roles(name_filters=name_filters, collection_filter=collection_filter)
    assert isinstance(found_roles, set)
