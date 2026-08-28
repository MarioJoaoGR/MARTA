
# Module: ansible.cli.doc
import pytest
from ansible.cli.doc import RoleMixin

# Assuming `self` is an instance of a class that includes this mixin
@pytest.fixture
def role_mixin():
    return RoleMixin()

# Test case for _build_summary method
def test_build_summary(role_mixin):
    role = 'MyRole'
    collection = 'my_collection'
    argspec = {'entry_point1': {'short_description': 'Description1'}, 'entry_point2': {'short_description': 'Description2'}}
    
    result = role_mixin._build_summary(role, collection, argspec)
    expected_result = ('my_collection.MyRole', {'collection': 'my_collection', 'entry_points': {'entry_point1': 'Description1', 'entry_point2': 'Description2'}})
    
    assert result == expected_result
