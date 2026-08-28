
import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase
import sys
from types import ModuleType

# Test valid input scenario
def test_valid_input():
    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.somens.somodule', ['/path/to/collection'])
    module = loader.load_module('ansible_collections.somens.somodule')
    assert isinstance(module, ModuleType), "Expected a module type"
    assert module.__name__ == 'ansible_collections.somens.somodule', "Module name does not match expected value"

# Test edge case scenario with None path_list
def test_edge_case():
    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.somens.somodule', None)
    with pytest.raises(ImportError):
        loader.load_module('ansible_collections.somens.somodule')

# Test invalid input scenario
def test_invalid_input():
    try:
        loader = _AnsibleCollectionPkgLoaderBase('invalid.fullname')
    except ImportError as e:
        assert str(e) == "Only modules from 'ansible_collections' package can be loaded", "Expected specific ImportError message"
