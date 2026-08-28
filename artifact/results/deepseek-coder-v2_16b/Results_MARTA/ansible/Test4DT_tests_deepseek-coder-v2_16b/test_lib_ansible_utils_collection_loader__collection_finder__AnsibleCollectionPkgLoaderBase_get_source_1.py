
import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

# Test Scenario 1: Test standard input with only fullname provided
def test_valid_case_fullname_only():
    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.somens.somodule')
    assert loader._fullname == 'ansible_collections.somens.somodule'
    assert loader._split_name == ['ansible_collections', 'somens', 'somodule']
    assert loader._rpart_name == ('ansible_collections', '', 'somens.somodule')
    assert loader._parent_package_name == 'ansible_collections'
    assert loader._package_to_load == 'somens.somodule'

# Test Scenario 2: Test edge case with None for path_list
def test_edge_case_none_path_list():
    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.somens.somodule', path_list=None)
    assert loader._candidate_paths == []
    assert loader._subpackage_search_paths == []

# Test Scenario 3: Test invalid input with wrong fullname format
def test_invalid_input_wrong_fullname():
    with pytest.raises(ValueError):
        _AnsibleCollectionPkgLoaderBase('wrong.format')
