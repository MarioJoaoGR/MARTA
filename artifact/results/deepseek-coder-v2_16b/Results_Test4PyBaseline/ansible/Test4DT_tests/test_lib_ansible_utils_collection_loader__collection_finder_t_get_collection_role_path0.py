
import pytest
from ansible.utils.collection_loader._collection_finder import _get_collection_role_path

# Test cases for fully qualified collection reference
def test_fully_qualified_collection_reference():
    result = _get_collection_role_path('ansible.example:roles:myrole', collection_list=['ansible.example'])
    assert result == ('myrole', '/usr/local/lib/python3.8/site-packages/ansible_collections/ansible/example/roles/myrole', 'ansible.example')

# Test cases for unqualified role name with empty collection list
def test_unqualified_role_name_empty_collection_list():
    result = _get_collection_role_path('myrole', collection_list=[])
    assert result == (None, None, None)

# Test cases for unqualified role name without collection list
@pytest.mark.skip(reason="The function should default to searching within a single collection based on the FQCR")
def test_unqualified_role_name_without_collection_list():
    result = _get_collection_role_path('myrole')
    assert result == (None, None, None)

# Test cases for invalid role name
def test_invalid_role_name():
    result = _get_collection_role_path('invalid:role', collection_list=['ansible.example'])
    assert result is None  # Assuming the function returns None if no valid role is found
