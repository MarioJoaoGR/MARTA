
import pytest
from ansible.utils.collection_loader._collection_finder import _get_collection_resource_path

# Test scenario 1: Fully qualified role name
def test_valid_case_fully_qualified():
    role_name = 'ansible.demo.my_role'
    result = _get_collection_role_path(role_name)
    assert result is not None
    assert isinstance(result, tuple), "Result should be a tuple"
    assert len(result) == 3, "Result tuple should have exactly three elements"
    role, path, collection_ref = result
    assert role == 'my_role', f"Expected role name to be 'my_role', but got '{role}'"
    assert '/path/to/ansible/collections/ansible/demo/roles/my_role' in path, f"Expected path to include '/path/to/ansible/collections/ansible/demo/roles/my_role'"
    assert collection_ref.collection == 'ansible.demo', f"Expected collection reference to be 'ansible.demo'"

# Test scenario 2: Unqualified role name with collection list
def test_valid_case_unqualified():
    role_name = 'my_role'
    collection_list = ['ansible.demo']
    result = _get_collection_role_path(role_name, collection_list)
    assert result is not None
    assert isinstance(result, tuple), "Result should be a tuple"
    assert len(result) == 3, "Result tuple should have exactly three elements"
    role, path, collection_ref = result
    assert role == 'my_role', f"Expected role name to be 'my_role', but got '{role}'"
    assert '/path/to/ansible/collections/ansible/demo/roles/my_role' in path, f"Expected path to include '/path/to/ansible/collections/ansible/demo/roles/my_role'"
    assert collection_ref.collection == 'ansible.demo', f"Expected collection reference to be 'ansible.demo'"

# Test scenario 3: Unqualified role name without collection list, expecting None result
def test_invalid_case_unqualified_no_collection():
    role_name = 'my_role'
    result = _get_collection_role_path(role_name)
    assert result is None, "Expected result to be None when no collection list is provided"
